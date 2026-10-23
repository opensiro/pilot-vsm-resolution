# Proof of Concept — VSM-RES-001 / P0

**Independent OpenSiro exploratory study.** This is a research PoC, not a Resolution endorsement or a claim about AI alignment.

## Problem and motivation

[Resolution's October 2026 Hironaka report](https://resolution.org/post/formalizing-resolution-of-singularities) describes a large-scale Lean autoformalization based on a high-level plan and atomic research tasks, followed by a substantial human-guided refactoring stage. Its authors explicitly left open how much additional agent scaffolding would have helped. Their public [Lean repository at `044d89c`](https://github.com/resolutionorg/hironaka/tree/044d89c9455859446fc5e986667319f910e15f4b) includes a pinned Lean 4.35.0 toolchain, challenge statements and comparator/axiom checks.

**Hypothesis:** a VSM-informed control plane may help coordinate bounded research work, keep verification and policy boundaries explicit, and make failures observable. **Alternative explanation:** a small task list and deterministic Lean CI would work equally well without VSM.

P0 asks only whether an implementable workflow is plausible. It cannot estimate an incremental VSM effect.

## Realized design

- [T01](../tasks/T01-proof-construction.md): construct generic Lean list operations and mathematical properties under `Pilot/Core.lean`.
- [T02](../tasks/T02-defect-detection.md): introduce a false equality in a separate fixture to measure actual error detection.
- [T03](../tasks/T03-independent-check.md): run the proof build and the negative challenge through a separate Lean process, preserving exit codes, logs and timing with `scripts/run_pilot.py` and optional GitHub Actions artifact retention.
- [Protocol](../PROTOCOL.md) and [manifest](../experiments/P0-001/manifest.json): stable hypotheses, task order, constraints, model request and metric rules.

These are implemented repository components; **successful execution must be established by actual receipts**. A GitHub workflow's existence is not a verified result.

## VSM roles and autonomy

The detailed local [function → right → owner → mechanism](../PROTOCOL.md#vsm-operational-mapping) table references [VSM Profile 0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/527fe01ccf1ee22e54bd9525285a89a93179c1e7/PROFILE.md). In P0, S1/S2/S3 decisions are coordinated by the operator, S5 rights remain with the human owner, and S4 recommendations are advisory. Lean is a mechanical verifier, **not** evidence by itself of independently autonomous S3*. A separate reviewer with source isolation and authority to reject would be required for that stronger claim.

## Evidence and outcomes

Consult [P0 feasibility report](../reports/P0_FEASIBILITY.md) and any timestamped receipt under `experiments/P0-001/runs/`. Distinguish source committed, local script tests, Lean verification, and CI run completion. The pilot is not complete merely because these links exist.

Compatible categories with Resolution's published process are task count, token input/output, cost, human interventions, wall time and verification. Current per-model tokens and inference dollars are unavailable unless separately attested; they are never estimated from prose length.

## Limits and next experiment

The examples do not exercise Mathlib, algebraic geometry, long-context research, inter-branch conflicts or real Resolution tools. A successful unit proof does not establish a productive research platform or a VSM effect. The current session cannot independently verify its own judgment; neither can a scripted checker infer organizational autonomy from filenames.

P1, if justified, should select a small pinned public Mathlib/Hironaka-adjacent task set, run conventional orchestration and VSM orchestration at equal Sol/tool budgets, predefine acceptance checks and intervention accounting, and blind an independent reviewer to conditions. Include a no-S3* or no-S4 ablation if feasible. Preserve failed tasks and costs.

## Discussion summary

OpenSiro is exploring whether a VSM-inspired control layer is technically useful for formalized research workflows of the sort publicly described by Resolution. This pilot checks only a small Lean proof/defect/review cycle and records function ownership and evidence gaps. We would be interested in discussing which real coordination failures deserve controlled testing; no integration or endorsement is implied.
