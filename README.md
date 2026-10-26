# OpenSiro × Resolution — VSM-RES-001

**P0: exploratory feasibility pilot — completed with `ITERATE` recommendation (2026-10-23).** This is an independent OpenSiro study, not a Resolution collaboration, integration, or comparison of system performance.

Question: can a bounded VSM-governed research workflow produce independently checkable Lean artifacts, react to a detected error, and retain sufficient evidence for a later controlled experiment?

## Run the pilot

Requires Python 3.10+ and Lean/Lake matching [`lean-toolchain`](lean-toolchain). No Mathlib download is required.

```sh
python3 -m unittest discover -s scripts -p 'test_*.py' -v
python3 scripts/run_pilot.py --output experiments/local-run
```

The second command builds the valid Lean library **and** verifies that an intentionally invalid theorem fails Lean elaboration. A post-run supplementary checker also runs `lake env leanchecker Pilot`. It returns nonzero if the primary positive or negative test behaves unexpectedly. Never treat a static/source-only check as Lean verification.

CI runs the same commands with `leanprover/lean-action@v1`; run artifacts are retained by GitHub Actions. See [P0-001 manifest](experiments/P0-001/manifest.json) for the experimental boundary. The presence of CI configuration is not itself evidence of a successful CI run.

## Navigation

- [P0 protocol](PROTOCOL.md) — registered scope, observables, and decision rules.
- [Pilot tasks](tasks/) — [T01](tasks/T01-proof-construction.md) proof construction, [T02](tasks/T02-defect-detection.md) negative test, [T03](tasks/T03-independent-check.md) verifier boundary.
- [Proof of Concept](docs/PROOF_OF_CONCEPT.md) — implementation, actual evidence, gaps, external summary.
- [Feasibility assessment](reports/P0_FEASIBILITY.md) — observed outcomes and GO/ITERATE/NO-GO decision.
- [Executed results](experiments/P0-001/RESULTS.md) — clean Lean receipt, diagnostics, limitations and source hashes.
- [Research record](experiments/P0-001/) — protocol-specific manifest and archived receipts.
- [P0.1 dev-alpha replication](experiments/P0-002/RESULTS.md) — cross-host Lean results and reproducible runbook; decision remains `ITERATE`.
- [Minimal Research Control Plane — proposed design](docs/RESEARCH_CONTROL_PLANE_DESIGN.md) — three user-facing stages, strict S1–S5 decision-right witnesses, and a bounded next iteration; **not executed yet**.
- [Research Automation — redacted case study](docs/RESEARCH_AUTOMATION_CASE_STUDY.md) — owner-review draft summarizing a **separate private exploratory research-harness exercise**; no private implementation or raw evidence is disclosed, no new VSM-RES-001 live run is claimed, and external sharing requires owner disclosure review ([case-study issue #7](https://github.com/opensiro/pilot-vsm-resolution/issues/7)).

## Normative and reference sources

- [OpenSiro VSM Profile v0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/527fe01ccf1ee22e54bd9525285a89a93179c1e7/PROFILE.md) is the normative source for S1–S5, ownership and autonomy. This pilot does not redefine it.
- [OpenSiro VSM Skills](https://github.com/opensiro/vsm-harness-skills/tree/5d36fd2e40e4e8a1711b1f315f7a60a9a78a2a25) owns assessment methodology, which is distinct from this exploratory operational mapping.
- [Resolution's research post](https://resolution.org/post/formalizing-resolution-of-singularities) and [public Hironaka source snapshot](https://github.com/resolutionorg/hironaka/tree/044d89c9455859446fc5e986667319f910e15f4b) are context, **not** a performance baseline. The P0 deliberately uses much smaller independent examples, with Lean 4.35.0 to align the compiler family.

No claims about alignment, comparative efficiency, or adoption by Resolution follow from this pilot.
