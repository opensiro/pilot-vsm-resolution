# VSM-RES-001 — P0 protocol v0.1

**Registered for exploratory feasibility, 2026-10-23.** Results belong in `experiments/P0-001/` and `reports/`; changes to this protocol require a new version, not retroactive edits to receipts.

## Question and falsification

Can one ChatGPT-directed research session coordinate a small Lean proof task and defect challenge, submit both to **actual Lean 4.35.0** verification, preserve provenance, and identify which VSM decision rights it really exercises?

- H0 (operational null): the proposed workflow cannot be completed and verified in the available environment within a bounded pilot.
- H1 (feasibility): a working proof artifact and an intentionally bad artifact are distinguished by Lean, with machine-readable results and an honest VSM ownership record.
- H1 is **not** evidence of VSM superiority. Even success could be fully explained by ordinary planning plus CI.

## System-in-focus

Boundary: this OpenSiro repository, the present ChatGPT research session, checked-in Lean source, Python runner, and a separate Lean/GitHub Actions execution process. Public `resolutionorg/hironaka` serves only as a reference. Private Resolution prompts, models, infrastructure, logs, and data are unavailable and out of scope.

## Fixed tasks and ordering

1. T01: implement and prove a generic reverse/append round-trip property in a minimal Lean library.
2. T02: challenge the verifier with a false concrete reverse equality; the Lean compiler must reject it.
3. T03: separately execute positive/negative checks, record actual results and classify any S3*/independence gap. No human or LLM judgment substitutes for compiler exit status.

This is a tiny proof-engineering workflow, **not** a replica of Resolution's mathematics, 12-branch orchestration, or 366 tasks.

## Environment and control

- Requested generation model: **GPT-6 Sol** via ChatGPT Browser. A UI/session label is not a measured API `model_id`; store it as `requested_model` unless an attestation is available.
- Proof tool: `leanprover/lean4:v4.35.0`, as in pinned public Hironaka source. No Mathlib for P0.
- ChatGPT does task selection, candidate construction, and diagnosis; it is not an independent blinded reviewer of its own output.
- A dedicated subprocess/GitHub Actions runner executes verification. CI provides separate execution and deterministic feedback, but not automatically independent semantic S3* autonomy.
- No new external services, upstream PRs, model API charges, or access to Resolution systems.

## VSM operational mapping

Consult the [normative Profile](https://github.com/opensiro/vsm-harness-profile/blob/527fe01ccf1ee22e54bd9525285a89a93179c1e7/PROFILE.md). The mapping below is **pilot-local evidence**, not a scored general assessment.

| Function | Relevant decision/feedback right | Current owner; support | Evidence threshold |
| --- | --- | --- | --- |
| S1 | choose/propose proof implementation | ChatGPT operator; Lean files | committed source + verified build |
| S2 | order and coordinate T01–T03 | ChatGPT operator; task IDs/runner | task trace and ordered invocations |
| S3 | admit work, bound pilot, react to failures | human-authorized ChatGPT operator; protocol/CI | documented stop/repair decisions |
| S3* | independent assurance beyond ordinary S1 verification | **unassigned independent agent**; separate compiler process only supports audit | independent source-isolated reviewer needed for a positive autonomy claim |
| S4 | detect limits and propose P1 adaptations | ChatGPT operator; failure reports | evidence-linked proposed change, not just speculation |
| S5 | policy, scope and GO authority | OpenSiro human owner; this protocol encodes constraints | explicit human policy; P0 recommendation does not transfer S5 authority |

Recorded mechanisms do **not** imply autonomous closure. If a function has not been exercised, write `not exercised`, rather than silently inferring it from its component's name.

## Measurements

- **Successful tasks:** T01 build passes, T02 compiler rejects defect, T03 report and runnable script produced. Report separate outcomes; no aggregate performance claim.
- **Verification:** return codes, error text, Lean toolchain, source revision, CI run URL and test runner outputs.
- **Execution time:** wall seconds from recorded subprocesses, not invented end-to-end agent time.
- **Human interventions:** owner requests after P0 admission counted when observable; do not extrapolate to an API-scale trial.
- **Input/output tokens and monetary cost:** record only if model/runtime exposes exact figures; otherwise `null` and reason `unavailable`.

Any failure, timeout, skipped check, unavailable Lean executable, or missing receipt remains visible. No success from an unrun test; preserve negative results and unexpected failures. Re-running creates a new receipt, not an overwrite of past results.

## Admission and decision criteria

- **GO:** real Lean positive + negative checks pass; artifacts and versions are reproducible; meaningful VSM feedback/decision rights were exercised; P1 can isolate the value of those rights.
- **ITERATE:** technical viability is partial or demonstrated, but key runtime, observability, or independent-audit gaps prevent a defensible P1 design without changes.
- **NO-GO:** essential checks repeatedly fail under a usable Lean environment, or the workflow cannot be adapted to a bounded research process.

The decision is a **recommendation** within the owner's S5 policy. A future P1 must compare with conventional orchestration using identical tasks, toolchain, model, compute budget, verification and interventions, and separate S3*/audit costs.
