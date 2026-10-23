# T03 — Separate verifier process and audit trail

**Input:** T01 and T02 source, committed configuration, run scripts.

**Task:** from a clean check-out execute Python unit tests and `python3 scripts/run_pilot.py --output <unique-directory>`. After a successful Lean build, the runner additionally calls `lake env leanchecker Pilot` to check the compiled proof artifacts. Archive JSON, stdout/stderr and exact Git SHA/CI URL when available.

**Primary acceptance:** positive build and deliberate rejection have recorded exit codes and a unique receipt. The pipeline fails closed on a missing Lean environment. An additional `leanchecker` run is **post-run supplementary evidence** under [P0-A01](../experiments/P0-001/AMENDMENT-A01.md), not a retroactive change to primary acceptance. Human review assesses what the checks do *not* prove.

**Independence caveat:** external Lean invocation isolates checking from proof generation, but ordinary verifier separation alone is not proof of S3* agent autonomy or source-blind audit. That gap must be explicit in the final decision.
