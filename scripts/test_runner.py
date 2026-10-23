import tempfile
from pathlib import Path
import unittest
from unittest import mock

from run_pilot import classify_negative, classify_positive, forbid_holes, run_command


class RunPilotTests(unittest.TestCase):
    def test_hole_guard_detects_admit(self):
        with tempfile.TemporaryDirectory() as folder:
            sample = Path(folder) / "test.lean"
            sample.write_text("theorem falseClaim : True := by admit\n")
            with mock.patch("run_pilot.ROOT", Path(folder)):
                self.assertEqual(forbid_holes([sample]), ["test.lean"])

    def test_subprocess_missing_command(self):
        result = run_command(["no-such-lean-pilot-executable-1234"], 1)
        self.assertIsNone(result["exit_code"])

    def test_existing_sources_have_no_holes(self):
        self.assertEqual(forbid_holes(), [])

    def test_verification_states_distinguish_blocked_and_failure(self):
        missing = {"exit_code": None, "timed_out": False, "stdout": "", "stderr": "missing"}
        rejected = {"exit_code": 1, "timed_out": False, "stdout": "", "stderr": "fixtures/InvalidProof.lean:7:2: error: Tactic `rfl` failed"}
        import_error = {"exit_code": 1, "timed_out": False, "stdout": "", "stderr": "error: unknown module 'Pilot.Core'"}
        accepted = {"exit_code": 0, "timed_out": False, "stdout": "", "stderr": ""}
        self.assertEqual(classify_positive(missing, []), "BLOCKED_EXECUTION")
        self.assertEqual(classify_positive(rejected, []), "FAIL_PROOF")
        self.assertEqual(classify_positive(accepted, ["Pilot/Core.lean"]), "FAIL_SOURCE_GUARD")
        self.assertEqual(classify_negative(missing), "BLOCKED_EXECUTION")
        self.assertEqual(classify_negative(accepted), "FAIL_NOT_REJECTED")
        self.assertEqual(classify_negative(rejected), "PASS")
        self.assertEqual(classify_negative(import_error), "FAIL_UNEXPECTED_DIAGNOSTIC")


if __name__ == "__main__":
    unittest.main()
