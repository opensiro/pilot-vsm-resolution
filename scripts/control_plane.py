#!/usr/bin/env python3
"""P0.2 two-phase research run: observe, decide, apply, record closure.

The program enforces an external decision. It does not own S3 discretion and
does not automatically classify any VSM autonomy state.
"""

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import sys

import run_pilot


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROTOCOL = ROOT / "experiments/P0-003/protocol.json"


def utc_now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def canonical_bytes(data):
    return (json.dumps(data, sort_keys=True, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def create_json(path, data):
    with path.open("xb") as output:
        output.write(canonical_bytes(data))


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_protocol(path):
    protocol = read_json(path)
    if protocol.get("id") != "VSM-RES-001/P0.2-v0.1":
        raise ValueError("unexpected protocol id")
    for key in ("max_primary_plus_optional_seconds", "optional_estimate_seconds"):
        value = protocol.get(key)
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{key} must be a positive number")
    return protocol


def classify(primary):
    positive = run_pilot.classify_positive(primary["positive"], primary["hole_guard"]["flagged_paths"])
    negative = run_pilot.classify_negative(primary["negative"])
    overall = ("PASS" if (positive, negative) == ("PASS", "PASS")
               else "BLOCKED" if any(x.startswith("BLOCKED") for x in (positive, negative))
               else "FAIL")
    return {"positive": positive, "negative": negative, "overall": overall}


def prepare_run(output_dir, protocol_path=DEFAULT_PROTOCOL):
    protocol = load_protocol(protocol_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=False)
    protocol_bytes = Path(protocol_path).read_bytes()

    holes = run_pilot.forbid_holes()
    version = run_pilot.run_command(["lean", "--version"], 30)
    positive = run_pilot.run_command(["lake", "build", "Pilot"])
    negative = run_pilot.run_command(["lake", "env", "lean", "fixtures/InvalidProof.lean"])
    primary = {
        "protocol_id": protocol["id"],
        "protocol_sha256": digest(protocol_bytes),
        "utc_prepared": utc_now(),
        "lean_version": version,
        "positive": positive,
        "negative": negative,
        "hole_guard": {"flagged_paths": holes, "passed": not holes},
        "source_sha256": {path: digest((ROOT / path).read_bytes()) for path in run_pilot.SOURCE_PATHS},
        "control_plane_sha256": digest(Path(__file__).read_bytes()),
        "model_runtime_attested": None,
        "input_tokens": None,
        "output_tokens": None,
        "model_cost_usd": None,
    }
    primary["outcome"] = classify(primary)
    elapsed = positive["elapsed_seconds"] + negative["elapsed_seconds"]
    pressure = elapsed + protocol["optional_estimate_seconds"] > protocol["max_primary_plus_optional_seconds"]
    request = {
        "protocol_id": protocol["id"],
        "primary_receipt_sha256": digest(canonical_bytes(primary)),
        "utc_requested": utc_now(),
        "current_work": {"T01": primary["outcome"]["positive"], "T02": primary["outcome"]["negative"]},
        "whole_run_elapsed_seconds": round(elapsed, 3),
        "resource_envelope_seconds": protocol["max_primary_plus_optional_seconds"],
        "optional_estimate_seconds": protocol["optional_estimate_seconds"],
        "exception": "BUDGET_PRESSURE" if pressure else "NONE",
        "allowed_actions": ["run_optional_checker", "skip_optional_checker"]
                           if primary["outcome"]["positive"] == "PASS" else ["skip_optional_checker"],
        "decision_owner": None,
        "autonomy_state": "UNASSESSED",
    }
    for name, result in (("positive", positive), ("negative", negative), ("lean_version", version)):
        (output_dir / f"{name}.stdout.log").write_text(result["stdout"], encoding="utf-8")
        (output_dir / f"{name}.stderr.log").write_text(result["stderr"], encoding="utf-8")
    create_json(output_dir / "primary_receipt.json", primary)
    create_json(output_dir / "decision_request.json", request)
    return request


def resume_run(run_dir, decision_path):
    run_dir = Path(run_dir)
    request_path = run_dir / "decision_request.json"
    request = read_json(request_path)
    receipt_path = run_dir / "primary_receipt.json"
    primary = read_json(receipt_path)
    if request["primary_receipt_sha256"] != digest(canonical_bytes(primary)):
        raise ValueError("primary receipt does not match decision request")
    if request["protocol_id"] != primary["protocol_id"]:
        raise ValueError("protocol mismatch")
    if (run_dir / "closure.json").exists() or (run_dir / "decision.json").exists():
        raise FileExistsError("run has already received a decision; immutable closure")

    decision = read_json(decision_path)
    if decision.get("request_sha256") != digest(request_path.read_bytes()):
        raise ValueError("decision is not bound to the exact request")
    if decision.get("action") not in request["allowed_actions"]:
        raise ValueError("decision action is not allowed by primary checks")
    for field in ("owner", "owner_kind", "rationale"):
        if not isinstance(decision.get(field), str) or not decision[field].strip():
            raise ValueError(f"decision requires {field}")
    if decision["owner_kind"] not in ("human", "agent", "parent"):
        raise ValueError("owner_kind must be human, agent, or parent")

    optional = None
    if decision["action"] == "run_optional_checker":
        optional = run_pilot.run_command(["lake", "env", "leanchecker", "Pilot"])
        (run_dir / "optional.stdout.log").write_text(optional["stdout"], encoding="utf-8")
        (run_dir / "optional.stderr.log").write_text(optional["stderr"], encoding="utf-8")
    action_status = ("SKIPPED_BY_DECISION" if optional is None
                     else "PASS" if optional["exit_code"] == 0 and not optional["timed_out"]
                     else "BLOCKED" if optional["exit_code"] is None or optional["timed_out"]
                     else "FAIL")
    closure = {
        "protocol_id": request["protocol_id"],
        "utc_closed": utc_now(),
        "request_sha256": digest(request_path.read_bytes()),
        "decision_sha256": digest(canonical_bytes(decision)),
        "decisive_owner": {"name": decision["owner"], "kind": decision["owner_kind"]},
        "decision_action": decision["action"],
        "decision_rationale": decision["rationale"],
        "supporting_enforcer": "scripts/control_plane.py",
        "observable_effect": {"optional_checker_executed": optional is not None, "status": action_status},
        "optional_result": optional,
        "overall": primary["outcome"]["overall"],
        "s3_autonomy_claim": "UNASSESSED",
        "notes": "A logged decision and enforcement do not alone prove S3 organizational autonomy.",
    }
    create_json(run_dir / "decision.json", decision)
    create_json(run_dir / "closure.json", closure)
    return closure


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    a = sub.add_parser("prepare")
    a.add_argument("--output", required=True)
    a.add_argument("--protocol", default=str(DEFAULT_PROTOCOL))
    b = sub.add_parser("resume")
    b.add_argument("--run", required=True)
    b.add_argument("--decision", required=True)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            result = prepare_run(args.output, Path(args.protocol))
            print(json.dumps({"request": str(Path(args.output) / "decision_request.json"),
                              "exception": result["exception"], "work": result["current_work"]}))
            return 0 if all(v == "PASS" for v in result["current_work"].values()) else 2
        result = resume_run(args.run, args.decision)
        print(json.dumps({"closure": str(Path(args.run) / "closure.json"),
                          "effect": result["observable_effect"]}))
        return 0 if result["overall"] == "PASS" and result["observable_effect"]["status"] not in ("FAIL", "BLOCKED") else 2
    except (ValueError, FileExistsError, FileNotFoundError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    sys.exit(main())
