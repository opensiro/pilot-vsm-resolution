# OpenSiro Research Automation — VSM-RES-001

**Making AI-assisted research understandable and governable by humans.**

This is an **independent OpenSiro feasibility study** exploring whether an existing Viable System Model (VSM) organizational standard can help people understand, coordinate, review, and constrain AI-assisted research workflows. Its primary motivation is **human legibility as a foundation for AI safety**, alongside easier contributor onboarding and cross-project collaboration. Faster agents are not an assumed benefit.

**Relationship to Resolution:** the study is informed by [Resolution's public research on AI-assisted Lean formalization](https://resolution.org/post/formalizing-resolution-of-singularities), but **Resolution has not participated in, approved, or adopted this project**. A possible joint pilot is a [proposal for discussion](docs/RESOLUTION_COLLABORATION_PROPOSAL.md), not an existing collaboration.

## What is here — and what is not

| Workstream | Public evidence | Status and limits |
| --- | --- | --- |
| **Lean feasibility (P0)** | [Protocol](PROTOCOL.md), [Python runner](scripts/run_pilot.py), [small Lean proofs](Pilot/Core.lean), [results](reports/P0_FEASIBILITY.md) | **Executed; `ITERATE`.** Checks basic proof construction, deliberate error detection, and preservation of machine evidence. This is a small infrastructure test, **not** advanced mathematical research. |
| **Second-host replication (P0.1)** | [Replication results](experiments/P0-002/RESULTS.md) | **Executed; `ITERATE`.** Repeats the bounded Lean experiment on another machine; not a comparative evaluation of VSM. |
| **Separate research harness case study** | [Public, redacted account](docs/RESEARCH_AUTOMATION_CASE_STUDY.md) | **Completed exploratory exercise, not externally reproducible.** Three small maintenance trials are summarized; underlying private code, prompts and raw traces are not public. These are not the Lean P0 results. |
| **Research Control Plane** | [Function-first design](docs/RESEARCH_CONTROL_PLANE_DESIGN.md) | **Design proposal.** Describes roles, evidence, decisions and feedback without treating a diagram as proof of autonomous VSM functions. |
| **Technical P0.2 control-closure runner** | [Issue #5](https://github.com/opensiro/pilot-vsm-resolution/issues/5), [open PR #6](https://github.com/opensiro/pilot-vsm-resolution/pull/6) | **Incomplete.** Proposed code and Python tests are not a completed live Lean run or a demonstrated S3 decision-and-return loop. |
| **Possible external collaboration** | [Collaboration proposal](docs/RESOLUTION_COLLABORATION_PROPOSAL.md) | **Not started.** Pilot choice, evaluation and access would need to be agreed with the participating organization. |

There is **no public evidence here** of a large autonomous multi-agent research system, a reproduction of Resolution's Hironaka result, a causal benefit from VSM, or a security-certified runtime.

## The research question

As research workflows involve more AI actors, a human reviewer should still be able to answer:

- **Purpose and boundaries:** what is the system trying to do, and where does its authority stop?
- **Responsibility:** who performs work, who makes consequential decisions, and who enforces them?
- **Evidence:** which protocol, attempt, tool output and review support a conclusion?
- **Intervention:** how can a person stop, redirect or correct the system, and what happens afterward?
- **Collaboration:** can another contributor understand and continue the work without relying on undocumented knowledge from its designer?

OpenSiro uses VSM as a **shared organizational description** for those questions. It distinguishes operational work (S1), coordination of disturbances between operational units (S2), current-system control (S3), future-oriented adaptation (S4), and identity/ultimate policy (S5). These are **functions and decision rights, not a requirement to deploy five agents or services**. An actual function needs observed behavior and evidence; a name or configuration is not sufficient.

### Three objectives

1. **AI safety through human legibility and governability.** Make authority, permissions, trust boundaries, escalation and return from intervention inspectable so that safety mechanisms can be specified, implemented and tested. This is an *enabling condition*, not proof that the AI model itself is interpretable or safe.
2. **Standardization and onboarding.** Give people and AI contributors a consistent vocabulary for task ownership, handoffs, evidence and operating boundaries across projects. The [standard already exists](https://github.com/opensiro/vsm-harness-profile); this repository does not introduce a competing standard.
3. **Controlled change and evaluation.** Make it practical to describe system modifications and compare A/B-like variants with fixed inputs, reproducible checks, recorded failures and appropriately limited conclusions. Performance improvements remain an empirical question.

VSM does not have to replace a self-organizing **swarm**. A swarm may be useful for execution; the question is whether a human can reconstruct its decision structure and enforce meaningful boundaries. Neither swarms nor VSM are inherently safe or unsafe based on topology alone.

## Two possible pilot entry points

These are **options for joint selection and assessment**, not experiments already performed with Resolution.

| Entry point | Small exercise | How usefulness would be assessed |
| --- | --- | --- |
| **People-first: collaboration and onboarding** | Two or more contributors use existing OpenSiro conventions on a real bounded task; a new participant follows the entry points and a handoff. | **Qualitative feedback from participants:** what became clearer, what was confusing, what added overhead, and whether they would keep the conventions. Avoid artificial numerical productivity scores for subjective usability. |
| **System-first: controlled research changes** | Compare a baseline and a clearly specified modification of a small research/Lean workflow under comparable conditions. Optionally formalize one narrow governance invariant in Lean or test denied actions in a sandbox. | Inspect reproducibility, authority and evidence trails, failed/blocked paths, and whether the chosen invariant relates to real runtime behavior. Quantitative comparisons are appropriate only where the design supports them. |

Other possible follow-ups include human–AI handoffs, explicit tool-permission boundaries, or mapping a multi-agent trace to decisions that a reviewer can actually reconstruct. See the [full proposal and pilot options](docs/RESOLUTION_COLLABORATION_PROPOSAL.md).

The intended decision is **“Is this useful enough to investigate further?”**, not **“Has VSM been proven superior?”**. A negative result is valid. A collaborating organization would select the workflow, reviewers, admissible evidence and whether to proceed.

## Reproduce the public Lean P0

Requirements: **Python 3.10+** and Lean/Lake matching [`lean-toolchain`](lean-toolchain). **Mathlib is not required.** Run from the repository root:

```sh
python3 -m unittest discover -s scripts -p 'test_*.py' -v
python3 scripts/run_pilot.py --output experiments/local-run
```

The runner builds small valid Lean proofs, expects a deliberately invalid theorem to fail with the relevant diagnostic, and preserves command outputs, exit status, timing and source hashes. It also invokes a supplementary `lake env leanchecker Pilot` check. Use a **new output directory for each run**: existing evidence is not overwritten. Successful source inspection alone does not count as Lean proof verification.

- See [P0-001 primary results](experiments/P0-001/RESULTS.md), [P0-002 second-host results](experiments/P0-002/RESULTS.md), and [the Proof of Concept write-up](docs/PROOF_OF_CONCEPT.md).
- See [GitHub Actions](https://github.com/opensiro/pilot-vsm-resolution/actions) for current CI status; historical failed or infrastructure-blocked runs remain part of the record.
- **P0.2 is separate:** neither these commands nor passing Python unit tests close [its open acceptance criteria](https://github.com/opensiro/pilot-vsm-resolution/issues/5).

## Safety, attribution and evidence boundaries

- **Organizational legibility is not runtime enforcement.** A VSM model alone does not enforce sandbox isolation, access control or safe tool execution.
- **Integrity is not authorization.** SHA-256 evidence binding can help detect changed artifacts, but an `owner` string or hash does not authenticate the decision-maker or authorize a decision. Those controls require a separate threat model and implementation.
- **Abstract Lean invariants are not deployment guarantees.** A checked theorem only establishes the stated property under its model and assumptions; runtime correspondence must be tested separately.
- **Function and autonomy claims require witnesses.** S1–S5 labels, sequential tasks and static approval gates do not establish exercised coordination, control or adaptation. No autonomy grade is automatically awarded. S3* is outside the current P0.2 scope.
- **Evidence is kept distinct from conclusions.** Preserve negative results, unknown costs, human interventions and alternative explanations. P0/P0.1 remain `ITERATE`; no matched VSM-versus-baseline result has been produced.
- **Public repository, limited disclosure.** The [redacted case study](docs/RESEARCH_AUTOMATION_CASE_STUDY.md) is publicly readable. Its underlying private harness source, prompts, configuration and raw machine traces have **not** been published and require separate owner-approved disclosure review.

## Where to read next

| If you want to… | Read |
| --- | --- |
| Understand the external research idea | [Collaboration proposal](docs/RESOLUTION_COLLABORATION_PROPOSAL.md) |
| Inspect the executed public feasibility work | [P0 protocol](PROTOCOL.md) → [results](reports/P0_FEASIBILITY.md) → [replication](experiments/P0-002/RESULTS.md) |
| Understand the proposed decision/control architecture | [Research Control Plane design](docs/RESEARCH_CONTROL_PLANE_DESIGN.md) |
| Read about the separate private exploratory exercise | [Redacted case study](docs/RESEARCH_AUTOMATION_CASE_STUDY.md) |
| Track unfinished implementation work | [P0.2 issue #5](https://github.com/opensiro/pilot-vsm-resolution/issues/5) and [PR #6](https://github.com/opensiro/pilot-vsm-resolution/pull/6) |

### Existing OpenSiro references

- [OpenSiro](https://opensiro.com) — project overview.
- [VSM Harness Profile v0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/527fe01ccf1ee22e54bd9525285a89a93179c1e7/PROFILE.md) — normative organizational definitions and decision-right semantics.
- [VSM Harness Skills](https://github.com/opensiro/vsm-harness-skills) — evidence-based assessment methodology.
- [VSM Harness Index](https://github.com/opensiro/vsm-harness-index) — public assessment corpus, not validation of this pilot.
- [VSM OSS Organization](https://github.com/opensiro/vsm-oss-organization) — existing applied coordination, contributor onboarding and governance reference.
- [OpenSiro Upstream](https://github.com/opensiro/upstream) — another operational example of bounded contributor workflows.

All results and proposed next steps belong to **OpenSiro's independent research** unless a collaboration is explicitly agreed and documented.
