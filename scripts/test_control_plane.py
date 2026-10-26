import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import control_plane


def result(argv, exit_code, seconds=0.2, stderr=""):
    return {"argv": argv, "exit_code": exit_code, "elapsed_seconds": seconds,
            "stdout": "", "stderr": stderr, "timed_out": False}


class ControlPlaneTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.protocol = self.base / "protocol.json"
        self.protocol.write_text(json.dumps({"id": "VSM-RES-001/P0.2-v0.1",
                                             "max_primary_plus_optional_seconds": 0.5,
                                             "optional_estimate_seconds": 0.4}))
        self.run_dir = self.base / "run"

    def prepare(self, positive=0):
        calls = [result(["lean", "--version"], 0, 0.1),
                 result(["lake", "build", "Pilot"], positive, 0.3),
                 result(["lake", "env", "lean", "fixtures/InvalidProof.lean"], 1, 0.3,
                        "fixtures/InvalidProof.lean: error: Tactic `rfl` failed")]
        with mock.patch.object(control_plane.run_pilot, "SOURCE_PATHS", ()), \
             mock.patch.object(control_plane.run_pilot, "forbid_holes", return_value=[]), \
             mock.patch.object(control_plane.run_pilot, "run_command", side_effect=calls):
            return control_plane.prepare_run(self.run_dir, self.protocol)

    def decision_file(self, request, action):
        path = self.base / "external-decision.json"
        path.write_text(json.dumps({"request_sha256": control_plane.digest((self.run_dir / "decision_request.json").read_bytes()),
                                    "action": action, "owner": "research-agent-session",
                                    "owner_kind": "agent", "rationale": "bounded current-work budget exception"}))
        return path

    def test_budget_exception_and_skip_closure(self):
        request = self.prepare()
        self.assertEqual(request["exception"], "BUDGET_PRESSURE")
        self.assertEqual(request["current_work"], {"T01": "PASS", "T02": "PASS"})
        closed = control_plane.resume_run(self.run_dir, self.decision_file(request, "skip_optional_checker"))
        self.assertEqual(closed["observable_effect"], {"optional_checker_executed": False,
                                                        "status": "SKIPPED_BY_DECISION"})
        self.assertEqual(closed["s3_autonomy_claim"], "UNASSESSED")
        with self.assertRaises(FileExistsError):
            control_plane.resume_run(self.run_dir, self.base / "external-decision.json")

    def test_optional_checker_is_real_subprocess_action(self):
        request = self.prepare()
        with mock.patch.object(control_plane.run_pilot, "run_command",
                               return_value=result(["lake", "env", "leanchecker", "Pilot"], 0)) as called:
            closed = control_plane.resume_run(self.run_dir, self.decision_file(request, "run_optional_checker"))
        called.assert_called_once_with(["lake", "env", "leanchecker", "Pilot"])
        self.assertEqual(closed["observable_effect"]["status"], "PASS")

    def test_stale_decision_rejected_without_writing(self):
        request = self.prepare()
        path = self.decision_file(request, "skip_optional_checker")
        data = json.loads(path.read_text())
        data["request_sha256"] = "bad"
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, "not bound"):
            control_plane.resume_run(self.run_dir, path)
        self.assertFalse((self.run_dir / "closure.json").exists())

    def test_no_checker_after_failed_positive(self):
        request = self.prepare(positive=1)
        self.assertEqual(request["allowed_actions"], ["skip_optional_checker"])
        path = self.decision_file(request, "run_optional_checker")
        with self.assertRaisesRegex(ValueError, "not allowed"):
            control_plane.resume_run(self.run_dir, path)


if __name__ == "__main__":
    unittest.main()
