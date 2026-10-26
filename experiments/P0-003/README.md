# P0.2 — bounded control-closure runbook

**Prospective protocol, not yet an executed Lean result.** This work supplements, but does not rewrite, completed P0/P0.1.

## Two-phase operation

1. Execute `python3 scripts/control_plane.py prepare --output experiments/local-p02-unique`. This runs actual Lean T01/T02 checks and writes a primary receipt plus `decision_request.json` containing current work, elapsed time, budget pressure and allowed actions. A missing Lean executable yields blocked evidence rather than a success claim. For a deliberately injected exception, add `--protocol experiments/P0-003/protocol-budget-pressure.json` and disclose that fixture in the run report.
2. A legitimate decision owner reads the exact request and creates a **separate** JSON file with `request_sha256` (SHA-256 of the request file's raw bytes), `owner`, `owner_kind` (`human`, `agent`, or `parent`), `action` (`run_optional_checker` or `skip_optional_checker`) and nonempty `rationale`.
3. Execute `python3 scripts/control_plane.py resume --run experiments/local-p02-unique --decision /path/to/decision.json`. The runner validates the binding, records the decision, executes or skips the optional Lean checker, and writes immutable `closure.json`. It refuses a second decision for the same run.

The runner **enforces** a decision; it does not make the resource judgment on behalf of S3. An agent-owned organizational loop, if claimed, needs separate behavioral evidence. A static budget threshold alone is not S3; no A/C/P state is conferred by these scripts. The output's `UNASSESSED` is intentional.

## Evidence, boundaries and next work

- Preserve raw stdout/stderr, exit status, timings, source hashes, decisions and closure; do not overwrite previous runs.
- The configured budget threshold may produce no exception for a fast run. If a test deliberately lowers it, record that as **injected**, never as a naturally observed failure.
- Ordinary Lean proof checks are part of S1 operation; S3* remains outside P0.2 gates. No S2 is credited without two distinct S1 units and a concrete interference path; no S4 without external/prospective adaptation into current capability.
- The primary toolchain is the existing P0 Lean setup. Model identity, inference tokens and dollars remain unmeasured unless independently attested.
- A separate result report must be written after a real run. Do not count unit-test mocks as an executed scientific experiment.

See [design](../../docs/RESEARCH_CONTROL_PLANE_DESIGN.md) and [implementation issue #5](https://github.com/opensiro/pilot-vsm-resolution/issues/5).
