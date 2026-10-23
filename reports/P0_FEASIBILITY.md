# P0 feasibility assessment — VSM-RES-001

**2026-10-23 — EXECUTED, decision: `ITERATE`.** This is a bounded technical result, not comparative VSM effectiveness.

## Observation and receipts

| Test / measurement | Direct evidence | Status |
| --- | --- | --- |
| Python runner tests | `python3 -m unittest discover -s scripts -p 'test_*.py' -v` | 4/4 PASS |
| T01 — generic Lean proof module | [Clean receipt](../experiments/P0-001/runs/2026-10-23-clean-lean435/receipt.json), `lake build Pilot` exit `0` | **PASS**, 0.848 s |
| T02 — false theorem negative control | Same receipt, `lake env lean fixtures/InvalidProof.lean` exit `1` with expected `rfl` failure | **PASS**, 0.277 s |
| Supplementary checker P0-A01 | Same receipt, `lake env leanchecker Pilot` exit `0` | **PASS**, 0.755 s |
| Initial local environment | [Immutable blocked receipt](../experiments/P0-001/runs/2026-10-23-local-no-lean/receipt.json) | BLOCKED, Lean/Lake missing |
| GitHub Actions job | [Run 39993639899](https://github.com/opensiro/pilot-vsm-resolution/actions/runs/39993639899) | FAILURE; job steps empty and logs returned `BlobNotFound`; root cause **unknown** |
| Exact GPT-6 Sol runtime, tokens and cost | No provider attestation or billing receipt | **Unavailable**; not imputed |
| Total agent execution time / interventions | Only command durations available; no full session accounting | **Unavailable** |

Raw output and individual checks: [P0-001 result index](../experiments/P0-001/RESULTS.md). The clean build was run after `lake clean`. Earlier successful warm runs are preserved separately; the post-run checker did not change the preregistered T01/T02 end points. The local check-out had no Git metadata, so the machine receipt's `git_sha` is `null`; source SHA-256 digests are recorded.

## VSM mapping: actual rights, not labels

| Function | Actual observation | Autonomy / gap |
| --- | --- | --- |
| S1 | ChatGPT-led proposal of Lean definitions/proofs; Lean compiled and checked results | Task execution evidenced, exact Sol runtime ID not attested |
| S2 | Ordered T01→T02→T03 and preserved related receipts | Operator coordination exercised; no independent S2 runtime |
| S3 | Bounded protocol and failure classification; local fallback chosen after CI trouble | Operator-mediated execution control; decision ownership not proven autonomous |
| S3* | Lean and `leanchecker` verified formal artifacts in separate processes | **Independent agent audit not demonstrated**; deterministic verification only |
| S4 | Environment failure prompted adaptation; added outcome classification and extra checker | Observed adaptation by coordinating assistant, not measured as self-maintaining S4 loop |
| S5 | Owner-defined boundaries prevented external contributions and superiority claims | Human policy authority retained; no delegated S5 autonomy |

Function names follow [Profile v0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/527fe01ccf1ee22e54bd9525285a89a93179c1e7/PROFILE.md). This table is a local case analysis, **not** a published general autonomy grade. A separate compiler process is not an independent organizational auditor.

## Interpretation and decision

**OBSERVATION:** a small formalized workflow can be coordinated with an explicit scope, fail-closed verification, error detection and source-linked receipts. Technical feasibility for these limited tasks is supported.

**ALTERNATIVE EXPLANATION:** ordinary task sequencing plus Lean checks could fully explain every positive result. No experiment isolated any causal contribution of VSM structure, and the tasks are much smaller than Resolution's Hironaka effort.

**LIMITATION:** no Mathlib/hard research task, no parallel conflicting workers, no blinded S3*, no model API usage metrics, no controlled non-VSM baseline, and an unresolved GitHub Actions job failure. Therefore `GO` for a comparative experiment is not justified yet.

**DECISION: ITERATE.** Continue because the fundamental proof/verification path works, but close reproducibility and independence gaps first. No evidence supports a broad `NO-GO` either.

## Next bounded experiment

**P0.1 — portability and reviewer boundary:** rerun the exact clean task suite on a pinned external runner with an inspectable CI trace; add a source-isolated reviewer that can reject a semantically flawed or unsupported claim; record its decision and owner separately from Lean. Then design **P1** with 6–10 pinned Mathlib/Hironaka-adjacent tasks, matched conventional-vs-VSM conditions and separately tracked reviewer cost. Do not reuse Resolution's 286M-output-token campaign as a causal baseline.
