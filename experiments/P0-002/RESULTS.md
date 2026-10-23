# P0.1 — dev-alpha portability result (P0-002)

**2026-10-23. Execution: PASS for unchanged P0 Lean micro-suite; study decision: ITERATE.** One non-comparative cross-host replication. The host-specific manifest was written after execution; underlying T01/T02 checks were fixed under [P0-v0.1](../../PROTOCOL.md). No efficacy result was newly preregistered.

## Direct observations

| Check | Machine observation |
| --- | --- |
| Source | [Exact commit](https://github.com/opensiro/pilot-vsm-resolution/commit/1f232ebfc915bb7a45db20ac12381cc2099f7136), recorded in receipt |
| Python runner tests | 4/4 PASS, Python 3.12.3 |
| T01 `lake build Pilot` after `lake clean` | PASS, exit 0, 1.775 s |
| T02 planted-invalid Lean theorem | PASS (expected rejection), exit 1, 0.506 s; expected Lean `rfl` failure diagnostic |
| Supplemental `lake env leanchecker Pilot` | PASS, exit 0, 1.815 s; not an independent agent auditor |
| Exact model runtime, tokens, monetary cost | Not measured / not attested |

The [raw machine receipt](runs/2026-10-23-dev-alpha-lean435/receipt.json) includes commands, exit codes, source SHA-256, diagnostics and per-command timing. Matching stdout/stderr logs are beside it. Lean 4.35.0 release archive SHA-256: `7289597a44543246c9227b8cae501767e095ce17f6d448b95fc4a8dc97268f6d`.

## Environment and deviations

- Runner: registered dev-alpha SSH device; separate Linux x86_64 VM, kernel 6.8.0-138, Lean 4.35.0 commit `eb6cafb7290e8bd5f2937522d8d804f58f02bafc`, Python 3.12.3. GitHub Actions were not changed.
- VM root filesystem had ~481 MB free. Lean archive, extraction and temporary checkout used `/dev/shm` (~18 GB free before run). This is an ephemeral VM run, not a permanent toolchain installation.
- The initial connector command specified `cwd` but ran from home and failed at Python test discovery, before executing the pilot suite. The explicit `cd` retry was the sole complete recorded suite. This tool invocation error is disclosed, not silently excluded.
- Unit-test pass is in dev-alpha monitoring session `4283cee3-a911-4673-96a4-309ba839abd0`; the machine receipt captures Lean. End-to-end elapsed time and human intervention counts are unavailable.

## Interpretation, status and next step

The unchanged Lean suite passes on a second host under the exact pinned commit. This addresses one portability gap, but ordinary scripts plus Lean can fully explain success; no causal VSM effect is shown. Independent source-isolated S3* review, a successful inspectable CI trace, and model-level cost accounting remain absent. This VM run neither repairs nor explains the prior GitHub Actions failure.

**Decision: ITERATE (unchanged).** Next: source-isolated reviewer with power to reject unsupported claims, then matched conventional-vs-VSM research tasks. See [runbook](REPRODUCE.md).
