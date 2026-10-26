# OpenSiro Research Automation — Redacted Case Study

**VSM-RES-001 · Case-study track · 2026-10-26**  
**Status:** retrospective, bounded, non-confirmatory report.  
**Disclosure:** review before sharing externally; no private harness source, prompts, configuration, raw traces, or internal evidence paths are included.

## Executive summary

OpenSiro is developing research infrastructure that keeps a scientific claim downstream of a predeclared protocol, an identifiable execution, retained evidence, and a separately inspectable review. This case study summarizes a **completed exploratory exercise of a privately maintained research harness** without disclosing its implementation.

The exercise demonstrates a narrow, reconstructable research-operations workflow. It does **not** demonstrate that VSM increases research quality, reduces cost, outperforms ordinary orchestration, or reproduces any work by Resolution. It is an independent OpenSiro study and not a Resolution collaboration.

The surrounding OpenSiro research program includes a separate AAMAS 2027 submission on organizational properties of agent harnesses. **Results from that paper are not attributed to the private harness exercise described here.**

## Research problem and approach

**Problem.** Multi-step AI-assisted research can lose the distinction between a proposed hypothesis, executable protocol, produced artifact, review result, and admissible scientific claim. A positive-looking final answer alone is not sufficient evidence of a correct research process.

**Approach.** Use a minimal, traceable sequence:

1. Specify a bounded research question, acceptance criteria, evidence-use class, and protocol before execution.
2. Execute admitted work and preserve distinct attempts, evaluations, interventions, and terminal dispositions.
3. Inspect the underlying evidence through a complementary review path, without silently modifying the ordinary result.
4. Record what was exercised, what was merely configured, and what remains unresolved.
5. Decide whether evidence warrants a further pilot, a changed future protocol, or a scientific claim.

The private implementation uses an internal evidence and control substrate. This report intentionally omits component names, source layout, commands, prompts, and machine identifiers. The conceptual workflow above is a **description**, not a reproducible public software release.

## Completed exploratory exercise

An internally preregistered, bounded Pilot 0 exercised three repository-maintenance microtasks. The source research record was reviewed for this summary; its raw artifacts remain private and are **not independently inspectable by an external reader of this report**.

| Recorded observation | Result | Interpretation |
| --- | --- | --- |
| Predeclared trials with terminal disposition | **3/3** | Bounded workflow completed in this pilot. |
| Ordinary task evaluations | **3/3 pass** | Task-specific declared checks passed. |
| Complementary evidence reviews | **3/3 pass**, no material findings | Review path was invoked; its consequential corrective-return branch was **not** exercised. |
| Trial closures | **3/3 `no_material_finding`** | No review-triggered correction was justified or manufactured. |
| S1 functional witness | **Supported at the declared Pilot 0 boundary** | Narrow evidence for an operational actor; not a general autonomy/performance claim. |
| Confirmatory causal experiment | **Not performed** | No VSM-benefit inference is supported. |

One procedural continuation following an unavailable verification subcommand was disclosed in the internal record. No task-specific implementation content was reported as supplied by a human in the frozen S1 witness. A natural failed implementation case did not occur, leaving a broader engineering milestone open.

These are **source-reported, internally recorded results**. The summary does not make private evidence publicly verifiable, and readers should not treat the absence of disclosed raw traces as external attestation.

## Function-first VSM interpretation

The labels below use the semantics of [OpenSiro VSM Profile v0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/527fe01ccf1ee22e54bd9525285a89a93179c1e7/PROFILE.md) and distinguish a retrospective mapping from a formal assessment under [Assessment Methodology v0.3.8](https://github.com/opensiro/vsm-harness-skills/tree/5d36fd2e40e4e8a1711b1f315f7a60a9a78a2a25/skills/assess-vsm-harness). A declared architectural responsibility does not establish a function, its decision owner, or an autonomy state. **S3\*** is outside this case-study track's assessment scope.

| Function | What this case study can say | What it cannot say |
| --- | --- | --- |
| **S1 — Operations** | A bounded operational-ownership witness was supported in three predeclared trials at the original, narrow recursion boundary. | That every research task, model, or environment has autonomous S1 ownership. |
| **S2 — Coordination** | Multi-unit coordination is a research-design concern. | A qualifying disturbance between two distinct S1 units and its closed resolution were demonstrated here. |
| **S3 — Current control** | The private harness has a declared path for current-study constraints and decision records. | A real, discretionary whole-system decision and returned operational consequence were established by these three clean tasks. |
| **S4 — Adaptation** | Future protocol changes are designed to remain separate from frozen historical evidence. | A real external/future signal drove an observed adaptation of current research capability in this exercise. |
| **S5 — Policy/identity** | Ultimate research-policy authority remains with the legitimate human parent. | A policy document or ordinary experiment approval demonstrates an autonomous S5 function. |

No `A`, `C`, or `P` autonomy classifications are awarded by this retrospective summary. Formal grading would require an explicit system boundary, evidence access, actual decision rights and return/closure witnesses under the current assessment methodology.

## Why this is relevant to Research Automation

The transferable design question is whether an AI research organization can keep **research intent, execution, validation, and claim admission** distinguishable even as work is automated. The case gives a concrete, small-scale example of:

- protocol-first execution and preserved negative/null paths;
- traceability from an attempted task to ordinary evaluation, separate review, and terminal decision;
- explicit disclosure of human interventions and unexercised controls;
- a clean separation between implementation tests, exploratory functional evidence, and future confirmatory comparisons.

For a prospective Resolution discussion, these are candidates for evaluating research-process infrastructure, **not** claims about Resolution's systems or a proposed replacement for Lean. A future collaboration would require its own agreed scope, task set, access controls, and matched-opportunity baseline.

## Limitations and recommended next step

1. **External reproducibility:** raw artifacts and private implementation are intentionally withheld; only an owner-reviewed, redacted summary is available for external inspection.
2. **Limited coverage:** three small maintenance tasks do not measure end-to-end scientific discovery, paper quality, large-scale coordination, or general reliability.
3. **No corrective event:** the reviews passed; a material independent finding and its consequential correction were not observed.
4. **No causal comparison:** no matched baseline, tokens/cost comparison, or effect size is claimed.
5. **Paper boundary:** the AAMAS research program and this private harness pilot are related in motivation but are **not represented as one causal evidence chain**.

**Recommendation: `ITERATE`.** Use this case study as a concise portfolio/feasibility artifact for a Research Automation conversation. If a practical comparison becomes valuable, prospectively register a small non-Lean research task with a coherent ordinary-workflow baseline, an equal-opportunity VSM condition, and explicit decision/evidence checkpoints. Do not retroactively convert the exploratory private Pilot 0 into a confirmatory result.

## Provenance and publication boundary

- This is a **redacted derivative narrative** of internal research, not the internal protocol, source code, or machine evidence itself.
- Summary observations were checked against the private harness's completed exploratory Pilot 0 result and research boundary documentation as available on 2026-10-26. Internal file paths, revisions, run IDs, and data are deliberately omitted.
- The separate VSM-RES-001 Lean P0/P0.1 outcomes remain recorded in this repository and retain `ITERATE`. This case-study track does not overwrite or reclassify them.
- The proposed [Research Control Plane design](RESEARCH_CONTROL_PLANE_DESIGN.md) and the open implementation [PR #6](https://github.com/opensiro/pilot-vsm-resolution/pull/6) are distinct, unfinished work; no live new run is claimed here.
- Any external sharing of this report should follow a separate disclosure review by the owner. The report does not grant access to the private harness.
