#!/usr/bin/env python3
"""Execute one fail-closed P0 Lean verification run; preserve the raw outputs."""

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
POSITIVE = (ROOT / "Pilot/Core.lean", ROOT / "Pilot/Verification.lean")
SOURCE_PATHS = (
    "Pilot.lean", "Pilot/Core.lean", "Pilot/Verification.lean",
    "fixtures/InvalidProof.lean", "lean-toolchain", "lakefile.toml",
    "scripts/run_pilot.py",
)


def run_command(argv, timeout=300):
    start = time.monotonic()
    try:
        proc = subprocess.run(argv, cwd=ROOT, text=True, capture_output=True, timeout=timeout)
        return {"argv": argv, "exit_code": proc.returncode, "elapsed_seconds": round(time.monotonic() - start, 3),
                "stdout": proc.stdout, "stderr": proc.stderr, "timed_out": False}
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as exc:
        return {"argv": argv, "exit_code": None, "elapsed_seconds": round(time.monotonic() - start, 3),
                "stdout": "", "stderr": str(exc), "timed_out": isinstance(exc, subprocess.TimeoutExpired)}


def forbid_holes(paths=POSITIVE):
    """Supplementary lexical guard only, not a kernel soundness check."""
    return [str(p.relative_to(ROOT)) for p in paths if re.search(r"\b(sorry|admit)\b", p.read_text())]


def classify_positive(result, holes):
    if holes:
        return "FAIL_SOURCE_GUARD"
    if result["exit_code"] is None:
        return "BLOCKED_EXECUTION"
    return "PASS" if result["exit_code"] == 0 else "FAIL_PROOF"


def classify_negative(result):
    if result["exit_code"] is None or result["timed_out"]:
        return "BLOCKED_EXECUTION"
    if result["exit_code"] == 0:
        return "FAIL_NOT_REJECTED"
    log = result["stdout"] + result["stderr"]
    # Do not count missing imports or compiler setup errors as catching the planted false theorem.
    if "fixtures/InvalidProof.lean" in log and "Tactic `rfl` failed" in log:
        return "PASS"
    return "FAIL_UNEXPECTED_DIAGNOSTIC"


def execute():
    start_utc = dt.datetime.now(dt.timezone.utc).isoformat()
    git = run_command(["git", "rev-parse", "HEAD"], 10)
    version = run_command(["lean", "--version"], 30)
    holes = forbid_holes()
    if shutil.which("lake") and shutil.which("lean"):
        positive = run_command(["lake", "build", "Pilot"])
        negative = run_command(["lake", "env", "lean", "fixtures/InvalidProof.lean"])
        checker = (run_command(["lake", "env", "leanchecker", "Pilot"])
                   if positive["exit_code"] == 0 else None)
    else:
        positive = {"argv": ["lake", "build", "Pilot"], "exit_code": None, "stdout": "", "stderr": "Lean/Lake executable missing", "elapsed_seconds": 0, "timed_out": False}
        negative = {"argv": ["lake", "env", "lean", "fixtures/InvalidProof.lean"], "exit_code": None, "stdout": "", "stderr": "Lean/Lake executable missing", "elapsed_seconds": 0, "timed_out": False}
        checker = None
    positive_state = classify_positive(positive, holes)
    negative_state = classify_negative(negative)
    checker_state = (classify_positive(checker, []) if checker is not None
                     else "BLOCKED_UPSTREAM")
    states = (positive_state, negative_state)
    overall = ("PASS" if states == ("PASS", "PASS")
               else "BLOCKED" if any(x.startswith("BLOCKED") for x in states) else "FAIL")
    return {"protocol": "VSM-RES-001/P0-v0.1", "utc_started": start_utc,
            "host_platform": platform.platform(), "python": sys.version.split()[0],
            "git_sha": git["stdout"].strip() if git["exit_code"] == 0 else None,
            "source_sha256": {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for path in SOURCE_PATHS},
            "ci_run_url": os.getenv("GITHUB_SERVER_URL", "") + "/" + os.getenv("GITHUB_REPOSITORY", "") + "/actions/runs/" + os.getenv("GITHUB_RUN_ID", "") if os.getenv("GITHUB_RUN_ID") else None,
            "model_requested": "GPT-6 Sol", "model_runtime_attested": None,
            "input_tokens": None, "output_tokens": None, "model_cost_usd": None,
            "hole_guard": {"flagged_paths": holes, "passed": not holes},
            "lean_version": version, "positive": positive, "negative": negative, "checker": checker,
            "tasks": {"T01": positive_state, "T02": negative_state},
            "supplemental_P0_A01": {"checker_status": checker_state, "affects_primary_result": False},
            "overall": overall}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="Unique output directory; refuses to overwrite")
    args = parser.parse_args()
    out = Path(args.output)
    if out.exists():
        parser.error("output directory already exists; results must be immutable")
    out.mkdir(parents=True)
    receipt = execute()
    for key in ("positive", "negative", "lean_version", "checker"):
        if receipt[key] is not None:
            (out / f"{key}.stdout.log").write_text(receipt[key]["stdout"])
            (out / f"{key}.stderr.log").write_text(receipt[key]["stderr"])
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"overall": receipt["overall"], "tasks": receipt["tasks"],
                      "receipt": str(out / "receipt.json")}, sort_keys=True))
    return 0 if receipt["overall"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
