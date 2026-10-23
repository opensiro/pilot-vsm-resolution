# T03 — Separate verifier process and audit trail

**Input:** T01 and T02 source, committed configuration, run scripts.

**Task:** from a clean check-out execute Python unit tests and `python3 scripts/run_pilot.py --output <unique-directory>`, archive JSON, stdout/stderr and exact Git SHA/CI URL.

**Acceptance:** both test outcomes appear individually and exit codes are recorded. The pipeline fails closed on a missing Lean environment. Human review assesses what the checks do *not* prove.

**Independence caveat:** external Lean invocation isolates checking from proof generation, but ordinary verifier separation alone is not proof of S3* agent autonomy or source-blind audit. That gap must be explicit in the final decision.
