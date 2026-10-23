# P0-001 results — chronological index

Protocol: [P0-v0.1](../../PROTOCOL.md). All receipts below are separate, immutable snapshots. `P0-A01` is an explicit post-run supplementary checker, not a primary acceptance change.

| Run | Evidence | Outcome |
| --- | --- | --- |
| Initial local, no Lean | [receipt](runs/2026-10-23-local-no-lean/receipt.json) | BLOCKED — no Lean/Lake executable |
| First true Lean verification | [receipt](runs/2026-10-23-local-lean435-001/receipt.json) | T01 PASS, T02 PASS, before P0-A01 |
| Supplementary checker, warm build | [receipt](runs/2026-10-23-local-lean435-a01/receipt.json) | Primary PASS; checker PASS |
| Source-digested warm build | [receipt](runs/2026-10-23-local-lean435-final/receipt.json) | Primary PASS; checker PASS; SHA-256 added |
| **Clean build after `lake clean`** | [receipt](runs/2026-10-23-clean-lean435/receipt.json) | **T01 PASS, T02 PASS, P0-A01 checker PASS** |

The clean-run receipt is the main result. Its `positive.stdout.log`, `negative.stdout.log`, and `checker.stdout.log` (including empty successful checker output) and respective stderr logs are preserved in the same directory. Lean 4.35.0 Git revision: `eb6cafb7290e8bd5f2937522d8d804f58f02bafc`.

**Environment:** Linux x86-64; Python 3.12.3; official Lean 4.35.0 archive installed temporarily, no Mathlib. The host Git check-out was not a Git repository, so no local Git SHA could be attested; the receipt contains SHA-256 of each relevant code/config file. Source is published through OpenSiro GitHub PR #2; compare those hashes before replication.

**Unmeasured:** generation model runtime ID, input/output tokens, inference cost, full agent wall time and comparable human intervention count. Do not estimate them from subprocess duration.

**CI exception:** [GitHub Actions run 39993639899](https://github.com/opensiro/pilot-vsm-resolution/actions/runs/39993639899) was marked failed. The connector reported an empty step list, no retained artifact and `BlobNotFound` for log retrieval; root cause remains undetermined. It was **not** counted as Lean validation. Local Lean execution provides the positive evidence instead.

Read [feasibility assessment](../../reports/P0_FEASIBILITY.md) for the `ITERATE` recommendation and [P0-A01 amendment](AMENDMENT-A01.md) for protocol provenance.
