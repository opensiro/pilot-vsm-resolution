#!/usr/bin/env python3
"""Execute one fail-closed P0 Lean verification run; preserve the raw outputs."""

import argparse
import datetime as dt
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


def execute():
    start_utc = dt.datetime.now(dt.timezone.utc).isoformat()
    git = run_command(["git", "rev-parse", "HEAD"], 10)
    version = run_command(["lean", "--version"], 30)
    holes = forbid_holes()
    if shutil.which("lake") and shutil.which("lean"):
        positive = run_command(["lake", "build", "Pilot"])
        negative = run_command(["lake", "env", "lean", "fixtures/InvalidProof.lean"])
    else:
        positive = {"argv": ["lake", "build", "Pilot"], "exit_code": None, "stdout": "", "stderr": "Lean/Lake executable missing", "elapsed_seconds": 0, "timed_out": False}
        negative = {"argv": ["lake", "env", "lean", "fixtures/InvalidProof.lean"], "exit_code": None, "stdout": "", "stderr": "Lean/Lake executable missing", "elapsed_seconds": 0, "timed_out": False}
    positive_ok = not holes and positive["exit_code"] == 0
    negative_log = negative["stdout"] + negative["stderr"]
    negative_ok = (negative["exit_code"] is not None and negative["exit_code"] != 0
                   and not negative["timed_out"] and bool(re.search(r"\berror:", negative_log)))
    return {"protocol": "VSM-RES-001/P0-v0.1", "utc_started": start_utc,
            "host_platform": platform.platform(), "python": sys.version.split()[0],
            "git_sha": git["stdout"].strip() if git["exit_code"] == 0 else None,
            "ci_run_url": os.getenv("GITHUB_SERVER_URL", "") + "/" + os.getenv("GITHUB_REPOSITORY", "") + "/actions/runs/" + os.getenv("GITHUB_RUN_ID", "") if os.getenv("GITHUB_RUN_ID") else None,
            "model_requested": "GPT-6 Sol", "model_runtime_attested": None,
            "input_tokens": None, "output_tokens": None, "model_cost_usd": None,
            "hole_guard": {"flagged_paths": holes, "passed": not holes},
            "lean_version": version, "positive": positive, "negative": negative,
            "tasks": {"T01": "PASS" if positive_ok else "BLOCKED_OR_FAIL",
                      "T02": "PASS" if negative_ok else "BLOCKED_OR_FAIL"},
            "overall": "PASS" if positive_ok and negative_ok else "FAIL_OR_BLOCKED"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="Unique output directory; refuses to overwrite")
    args = parser.parse_args()
    out = Path(args.output)
    if out.exists():
        parser.error("output directory already exists; results must be immutable")
    out.mkdir(parents=True)
    receipt = execute()
    for key in ("positive", "negative", "lean_version"):
        (out / f"{key}.stdout.log").write_text(receipt[key]["stdout"])
        (out / f"{key}.stderr.log").write_text(receipt[key]["stderr"])
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"overall": receipt["overall"], "tasks": receipt["tasks"],
                      "receipt": str(out / "receipt.json")}, sort_keys=True))
    return 0 if receipt["overall"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
