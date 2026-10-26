# VSM-RES-001 — Minimal Research Control Plane (design proposal)

**Status:** PROPOSED, 2026-10-26. **Scope:** the next bounded iteration after P0/P0.1; no new execution or VSM capability result is claimed here.

The [completed P0](https://github.com/opensiro/pilot-vsm-resolution/blob/main/reports/P0_FEASIBILITY.md) and [cross-host P0.1](https://github.com/opensiro/pilot-vsm-resolution/blob/main/experiments/P0-002/RESULTS.md) established a small reproducible Lean proof/error-checking workflow. Both retained `ITERATE`. This document is a prospective design clarification, **not** a retrospective amendment to P0 protocols, receipts, or conclusions.

## Purpose and system boundary

Demonstrate the *organizational methodology* of VSM in a minimal scientific agent harness: a research question can be executed, technically checked, governed under current resource constraints, and linked to an inspectable decision and a possible next experiment.

- **System-in-focus:** an OpenSiro-controlled research harness operating on a small, pinned Lean task suite, its agent actor(s), protocol, deterministic runner, evidence store, and legitimate human owner. Declare any external runner or parent decision path separately in each run.
- **Environment:** public research literature, available Lean/toolchain versions and task requirements, computation and human review limits; no private Resolution systems, code, or prompts.
- **Non-goals:** reproducing Resolution's Hironaka effort; a large agent swarm; a claim of improved theorem success, scientific quality, or cost; causal A/B conclusions in this feasibility iteration.
- **Explicit exclusion:** S3* is not in the current design's completion gates. Routine Lean checks are not silently reclassified as S3*.

Normative semantics: [VSM Harness Profile v0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md). Evidence and autonomy publication: [assess-vsm-harness Methodology v0.3.8](https://github.com/opensiro/vsm-harness-skills/blob/main/skills/assess-vsm-harness/SKILL.md) and its [autonomy states](https://github.com/opensiro/vsm-harness-skills/blob/main/skills/assess-vsm-harness/references/autonomy-states.md). Pin exact revisions before a formal assessment; this design is not one.

## Three user-facing stages are not three VSM functions

| Simple interface | User sees | Organizational function(s) that may participate |
| --- | --- | --- |
| **Research Governance** | research aim, policy boundaries, proposed options, current budget/commitments | S5 owns identity/ultimate policy; S4 develops external/future adaptation options; S3 allocates current resources and commitments |
| **Research Operations** | task execution, interactions and exceptions | S1 does research work and ordinary verification; S2 addresses a *specific* inter-S1 disturbance **only if** at least two distinct operational units exist; S3 regulates the whole current operation |
| **Evidence & Feedback** | traceable results, faults, decision and next proposal | S1 supplies primary artifacts/checks; S3 closes current-control interventions; S4 closes prospective environment-driven adaptations into current capability; S5 intervenes only for identity/ultimate-policy matters |

The UI may consist of one short protocol and one result page. It does **not** require five agents or five code services. The decisive owner may be an agent, human, or other actor; deterministic enforcement must be recorded separately.

## Function-first design and witness requirements

| Function | Relevant disturbance and decisive right | Minimal prospective witness | Do not count as evidence |
| --- | --- | --- | --- |
| **S1 — operations** | local difficulty in completing a bounded research task; agent chooses a candidate and responds to tool feedback | agent action → Lean result → local repair or documented failure, with commands and artifact hashes | tool invocation or a static task label alone |
| **S2 — coordination** | specific collision/oscillation among at least two distinct S1 units; response changes their later behavior | two operational units, a concrete shared-resource/file/lemma conflict, coordinated response and observable return | task ordering, delegation, shared queue or a single research worker |
| **S3 — current control** | a whole-system commitment/resource exception; owner decides how to revise priorities, budgets or work admission | current-work summary → discretionary decision with identified owner → enforced change → observed subsequent operation | configured cap, kill switch, runner scheduling, or a component named manager |
| **S4 — adaptation** | a prospective external change/opportunity (e.g., relevant new method or tool capability); owner develops an option to adapt | identifiable external signal → future-oriented option → S3 dialogue/decision → actual change in present research capability | ordinary results analysis, internal retries, backlog grooming or failure recovery alone |
| **S5 — identity/policy** | disagreement or change to the mission, permissible claims or ultimate risk policy; legitimate human owner decides | policy-level issue → owner decision → updated governing rule → subsequent run visibly subject to that rule | approval of an ordinary experiment, choice of a tactic, static prompt or policy text alone |

For each claimed function retain: **system boundary, disturbance, decisive right, owner, support/enforcement, return/closure, primary evidence, and gaps**. First establish the function and only then classify ownership as `A`, `C`, `P`, etc.; these are not a maturity scale. No positive state is awarded by this proposal.

### Correction to interpretation of the historical P0

This prospective semantic review preserves the P0 result but **does not treat** its ordered T01→T02→T03 sequence as sufficient S2 evidence: distinct S1 units and inter-S1 interference were not shown. Likewise, recovering from unavailable Lean/CI execution and adding a checker is internal troubleshooting, not by itself an externally oriented S4 adaptation loop. P0's bounded protocol and hard checks also do not, by themselves, establish agent-owned S3. The human-defined scope is a policy boundary, but S5 `P` publication additionally needs an identity/policy issue, legitimate decision and returned effect on subsequent operation.

These statements are not a new canonical Index assessment or an edit to frozen P0 observations. They prevent future diagrams from overstating capability.

## Minimal implementation contract for the next iteration

Borrow general practices from OpenSiro's existing research harnesses (registered protocol, source/version pinning, machine-readable receipts, negative cases, and report derived from evidence), without copying private research data or whole project stacks.

**Required small artifacts:**

1. A short versioned protocol: research question, hypotheses, fixed task set, toolchain/model provenance, metrics, budget and stop rules, owner-held policy constraints.
2. One reproducible runner: executes bounded Lean tasks, preserves successful/failed commands and source hashes, and does not treat source-only inspection as compiler verification.
3. One evidence bundle per run: stdout/stderr, return codes, timings, interventions, unavailable measurements as `null` with reasons, and explicit owner/action/closure event records.
4. One concise outcome page: what happened, what failed, what VSM rights were *actually exercised*, alternative non-VSM explanations, and owner-level `GO / ITERATE / NO-GO` recommendation.

Optional experiment variant definitions may express paired A/B runs (for example, direct proof vs lemma-first proof). In this next iteration, they demonstrate **experiment governance and observability**, not a statistical or causal superiority claim. A later controlled study must preregister matched tasks, toolchain, model, budgets, run order, intervention accounting and analysis.

## Bounded demonstrations and acceptance

| Demonstration | Acceptance evidence | Failure/limit |
| --- | --- | --- |
| **D1 — experiment governance** | registered protocol → actual run → verifiable result → report; clean rerun possible | no run, missing artifact, invented cost/metrics or unverifiable result |
| **D2 — S3 exception closure** | injected or natural whole-system resource/commitment exception; owner explicitly decides; runner applies; next operation changes | a static threshold fires but no discretionary current-control owner/return is shown |
| **D3 — traceability and policy** | hypothesis-to-artifact link; a genuine high-level policy decision, if raised, returns into the next run | generic approval is presented as S5, or a paper/report substitutes for primary evidence |
| **Optional S4 probe** | external/future-relevant signal and proposed option demonstrably return via S3 into capability | internal retrospective analysis is mislabeled S4 |
| **Optional S2 probe** | two S1 units, specific conflict, attenuation and observable return | mere task sequence or routing |

The iteration may honestly report **S2 or S4 not exercised**. It need not manufacture extra agents or external events just to fill the VSM diagram. The user-facing UI should remain understandable in minutes; any paper draft is an optional *derived consumer* of verified results rather than the primary proof of functionality.

**Decision:** `GO` only for demonstrated, reproducible function-specific closure at the claimed boundary with explicit limitations; `ITERATE` for a technically working but organizationally incomplete harness; `NO-GO` if fundamental bounded research execution or evidence integrity repeatedly fails. None implies superiority over a conventional harness. Keep all old receipts unchanged, and open a separately preregistered controlled comparison only after feasibility closes.
