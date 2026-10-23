import tempfile
from pathlib import Path
import unittest
from unittest import mock

from run_pilot import forbid_holes, run_command


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


if __name__ == "__main__":
    unittest.main()
