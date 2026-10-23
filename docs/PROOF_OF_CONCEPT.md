# Proof of Concept — VSM-RES-001 / P0

**Independent OpenSiro exploratory study; P0 executed 2026-10-23, recommendation `ITERATE`.** This is a research PoC, not a Resolution endorsement or a claim about AI alignment.

## Problem and motivation

[Resolution's October 2026 Hironaka report](https://resolution.org/post/formalizing-resolution-of-singularities) describes a large-scale Lean autoformalization based on a high-level plan and atomic research tasks, followed by a substantial human-guided refactoring stage. Its authors explicitly left open how much additional agent scaffolding would have helped. Their public [Lean repository at `044d89c`](https://github.com/resolutionorg/hironaka/tree/044d89c9455859446fc5e986667319f910e15f4b) includes a pinned Lean 4.35.0 toolchain, challenge statements and comparator/axiom checks.

**Hypothesis:** a VSM-informed control plane may help coordinate bounded research work, keep verification and policy boundaries explicit, and make failures observable. **Alternative explanation:** a small task list and deterministic Lean CI would work equally well without VSM.

P0 asks only whether an implementable workflow is plausible. It cannot estimate an incremental VSM effect.

## Realized design

- [T01](../tasks/T01-proof-construction.md): construct generic Lean list operations and mathematical properties under `Pilot/Core.lean`.
- [T02](../tasks/T02-defect-detection.md): introduce a false equality in a separate fixture to measure actual error detection.
- [T03](../tasks/T03-independent-check.md): after the Lean proof build and negative challenge, separately run `leanchecker Pilot`, preserving each exit code, log and timing with `scripts/run_pilot.py` and optional GitHub Actions artifact retention.
- [Protocol](../PROTOCOL.md) and [manifest](../experiments/P0-001/manifest.json): stable hypotheses, task order, constraints, model request and metric rules.

These are implemented repository components. Actual Lean proof checking is confirmed by the [clean-run machine receipt](../experiments/P0-001/runs/2026-10-23-clean-lean435/receipt.json) and the [P0 results index](../experiments/P0-001/RESULTS.md). A GitHub workflow's existence is not a verified CI result.

## GPT-6 Sol / ChatGPT Browser execution boundary

The planned coordinating environment was **GPT-6 Sol in ChatGPT Browser**, using one bounded operator session for task selection, proof edits and response to errors. In this execution, the available ChatGPT-connected workspace and GitHub connector handled code and provenance while a separately installed local Lean binary performed checks; a private-repository browser view was not authenticated. The generation model's exact runtime identity was not exposed or attested, so `GPT-6 Sol` remains a *requested* model, not a measured condition. No independent GPT-6 Sol API run, token invoice or persistent autonomous Browser orchestration took place.

Browser sessions have manual continuity, tool authorization and context boundaries. A repeatable API-scale experiment would require pinned model identifiers, explicit prompt transcripts, session-isolation rules, fixed token/retry budgets and machine-observed interventions. Those are **P1 prerequisites**, not outcomes of this pilot.

## VSM roles and autonomy

The detailed local [function → right → owner → mechanism](../PROTOCOL.md#vsm-operational-mapping) table references [VSM Profile 0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/527fe01ccf1ee22e54bd9525285a89a93179c1e7/PROFILE.md). In P0, S1/S2/S3 decisions are coordinated by the operator, S5 rights remain with the human owner, and S4 recommendations are advisory. Lean is a mechanical verifier, **not** evidence by itself of independently autonomous S3*. A separate reviewer with source isolation and authority to reject would be required for that stronger claim.

## Evidence and outcomes

**Observed:** after `lake clean`, `lake build Pilot` passed (0.848 s), the deliberately wrong theorem was rejected with a Lean diagnostic (0.277 s), and supplemental `lake env leanchecker Pilot` passed (0.755 s), all using Lean 4.35.0. Python unit tests passed 4/4. Times cover the individual subprocesses only, not agent reasoning or full workflow duration. See [raw JSON and logs](../experiments/P0-001/runs/2026-10-23-clean-lean435/receipt.json) and [interpretation](../reports/P0_FEASIBILITY.md).

**Observed limitations:** the initial local executor lacked Lean/Lake; a GitHub Actions job failed without accessible steps/logs/artifacts ([CI run 39993639899](https://github.com/opensiro/pilot-vsm-resolution/actions/runs/39993639899)). Local verification recovered through an official toolchain installation. The local workspace was not a Git checkout (`git_sha: null`); the receipt preserves SHA-256 hashes of all check-relevant source files. The exact model runtime, tokens and model cost were not attested. The supplementary leanchecker was added after the first successful run under [amendment P0-A01](../experiments/P0-001/AMENDMENT-A01.md), not retroactively made part of primary acceptance.

Compatible categories with Resolution's published process are task count, token input/output, cost, human interventions, wall time and verification. Current per-model tokens and inference dollars are unavailable unless separately attested; they are never estimated from prose length.

## Limits and next experiment

The examples do not exercise Mathlib, algebraic geometry, long-context research, inter-branch conflicts or real Resolution tools. A successful unit proof does not establish a productive research platform or a VSM effect. The current session cannot independently verify its own judgment; neither can a scripted checker infer organizational autonomy from filenames.

**Decision: ITERATE.** The bounded proof/defect cycle is technically viable, but the current evidence does not demonstrate the incremental value or autonomy of VSM functions, notably independent S3*, or reliable CI portability.

P1, after these gaps are addressed, should select a small pinned public Mathlib/Hironaka-adjacent task set, run conventional orchestration and VSM orchestration at equal Sol/tool budgets, predefine acceptance checks and intervention accounting, and blind an independent reviewer to conditions. Include a no-S3* or no-S4 ablation if feasible. Preserve failed tasks and costs.

## Discussion summary

OpenSiro is exploring whether a VSM-inspired control layer is technically useful for formalized research workflows of the sort publicly described by Resolution. This pilot checks only a small Lean proof/defect/review cycle and records function ownership and evidence gaps. We would be interested in discussing which real coordination failures deserve controlled testing; no integration or endorsement is implied.
