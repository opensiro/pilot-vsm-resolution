# OpenSiro × Resolution — Legible and Governable AI Research

**Status:** DRAFT collaboration proposal for external review. **Owner:** OpenSiro. **Date:** 2026-10-26.  
**Relationship:** Independent OpenSiro proposal only. No Resolution collaboration, endorsement, adoption, permission to access internal systems, or joint experiment has been agreed.

## Executive proposition

OpenSiro proposes a small, **jointly selected and evaluated** pilot with Resolution to explore whether a shared Viable System Model (VSM) organizational description can make human–AI research systems easier to **understand, govern, constrain, and safely modify**, while improving collaboration and onboarding.

**The primary motivation is AI safety through human legibility and governability, alongside interoperability, standardization, and onboarding—not an assumption that VSM will make AI agents faster or more capable.**

A useful organizational representation should let an independent human answer:

- What is the system trying to do, and where does its declared boundary lie?
- What work is performed by which operational units, human contributors, or AI actors?
- Who actually owns each consequential decision right, and who merely enforces or records it?
- What is an autonomous actor allowed to do, what is forbidden, and who can change that policy?
- How are conflicting units coordinated, exceptions escalated, and interventions returned to subsequent operation?
- What primary evidence supports those answers, including failed or blocked cases?

This makes **human inspectability and attribution of authority** a prerequisite for designing and evaluating meaningful safety boundaries: permission scopes, sandbox or trust-zone separation, review gates, containment, and accountable overrides.

A self-organizing **swarm** may be appropriate for high-autonomy task execution. However, a workflow whose emergent decision structure cannot be reconstructed is harder to review and assure. This is a **governability trade-off to investigate**, not proof that swarms are inherently unsafe or VSM structures inherently safe. A VSM organizational layer can describe and constrain a swarm without prescribing the implementation's agent topology.

**Safety claim boundary:** VSM provides a candidate organizational specification, not a security mechanism, mathematical proof of safety, or autonomous assurance of policy compliance. Constraints must be enforced in the real runtime and assessed against observed behavior; a legible diagram alone is insufficient.

## The standard already exists

We are **not** proposing another independent normative standard. OpenSiro already maintains a public, implementation-agnostic VSM Profile, assessment methodology, and an applied multi-repository organization. The pilot would test how useful these existing materials are for an external research context, with any prospective adaptations recorded explicitly.

| Existing OpenSiro surface | Role for this proposal |
| --- | --- |
| [OpenSiro ecosystem](https://opensiro.com) | Public overview of the broader project. |
| [VSM Harness Profile v0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/527fe01ccf1ee22e54bd9525285a89a93179c1e7/PROFILE.md) | Normative organizational vocabulary: S1–S5, system boundary, functions, decisive rights, ownership, enforcement and closure. |
| [VSM Harness Skills](https://github.com/opensiro/vsm-harness-skills) | Reusable methodology and evidence-based assessment procedures; distinguishes interpretation from proven capabilities. |
| [VSM Harness Index](https://github.com/opensiro/vsm-harness-index) | Evidence-backed public corpus of assessments; not evidence that this proposed pilot works. |
| [VSM OSS Organization](https://github.com/opensiro/vsm-oss-organization) | Working reference for contributor entry points, cross-repository organization, control boundaries and explicit admission of operational domains. |
| [OpenSiro Upstream](https://github.com/opensiro/upstream) | Additional operational example involving third-party contributor workflows, constraints and maintenance. |

The Profile owns semantics; other repositories apply them within their own authority boundaries. This proposal is **not** permission to change those contracts or claim new S1–S5 autonomy states.

## Possible joint pilot tracks

The following are options for **Resolution to select, reshape, reject, or combine** after a short asynchronous review. There is no requirement to deploy a broad control plane.

| Track | Candidate activity | What Resolution would evaluate |
| --- | --- | --- |
| **H1 — Human collaboration / onboarding** | Apply the existing VSM-oriented collaboration conventions to one small project with multiple human contributors; introduce a newcomer and follow a real task handoff. | **Qualitative participant judgment**, not numerical productivity metrics: clarity of roles, ease of joining, understandability of decisions, discoverability of evidence, perceived overhead, and whether the workflow is still understandable without its designer. |
| **H2 — Human–AI handoff** | Describe a bounded workflow where a human delegates to an AI actor, receives evidence, and makes or reviews consequential decisions. | Whether a participant can explain the AI's scope, decision owner, stopping conditions, escalation route and return path. Record confusing or misleading descriptions openly. |
| **T1 — A/B-like system-modification experiments** | Select one small research or automation system and two clearly defined modifications (A/B), keeping task inputs, tools, budgets and execution conditions as comparable as practical. Use explicit protocols and machine-checkable receipts. | **The ease and trustworthiness of conducting and interpreting a comparison**: identifiable modifications, preserved provenance, comparable outputs, reproducible checks, visible failures, and controlled admission of conclusions. Outcome or throughput effects are secondary and must not be asserted without an adequate design. |
| **T2 — Lean-governed workflow / formal invariants** | On a deliberately small Lean-based research task, formalize a narrow invariant about authorization, artifact promotion, review, or state transitions; relate it to an executable workflow. | Whether the property is precise, provable and connected to observable runtime behavior. A Lean theorem about an abstract policy does **not** prove that deployed agents follow it. |
| **S1 — Safety boundaries and containment** | Trace an agent task across tool permission scopes, isolated environments, review gates and blocked actions; attempt selected negative cases within an approved sandbox. | Whether forbidden cross-boundary actions are actually rejected and can be understood from evidence; whether the authority owner and exception path are unambiguous. |
| **S2 — Multi-agent / swarm legibility** | Map a bounded multi-agent trace into organizational functions, exercised decisions and cross-unit interactions, without forcing one agent per VSM function. | Whether VSM reveals otherwise hidden owners, unowned decisions, uncontrolled interference or unclear trust boundaries—and whether it adds unnecessary bureaucracy. |

### How to evaluate the human-facing tracks

For H1/H2, **do not turn subjective usability into artificial numeric KPIs**. Prefer a short walkthrough, participant accounts, and a structured discussion:

1. What became easier to understand or hand off?
2. What remained ambiguous?
3. Did the standard help a new contributor act without repeated explanations?
4. What documentation or governance felt excessive?
5. Would participants voluntarily retain or adapt the approach?

Keep differing opinions and counterexamples rather than collapsing them into a score.

### How to evaluate controlled modifications

For T1/T2, explicit A/B-like comparison is useful when variants can be genuinely controlled:

- Pin the system, test inputs, toolchain, configuration, and evidence requirements.
- State what changes between A and B and what must remain fixed.
- Save primary results, failures, human interventions and reasons for any missing measurements.
- Evaluate not only task outcome but also whether decisions, policy boundaries and evidence remain reconstructible.
- Call an experiment **exploratory** unless the comparison actually supports a causal claim.

These technical experiments can use quantitative measurements where meaningful; that is a different evaluation question from people's subjective experience of collaboration.

## Recommended minimal starting point

**Offer a choice of two low-commitment entry points:**

- **People-first:** H1, optionally with H2. One real handoff/onboarding exercise, followed by brief qualitative feedback from the participants.
- **System-first:** T1 on a small, reproducible research workflow; add T2 only if the selected safety or governance invariant benefits from Lean.

Whichever entry point Resolution prefers, OpenSiro supplies the existing public methodology and a scoped draft protocol. **Resolution chooses the relevant workflow, reviewers, admissible data, and whether the evaluation is worth continuing.** An asynchronous proposal review should precede any meeting, access grant or substantive implementation.

The joint pilot's decision question is **"Is this approach useful and worth investigating here?"** not **"Has VSM been proven superior?"**

## Relation to previous independent work

[OpenSiro's independent feasibility repository](https://github.com/opensiro/pilot-vsm-resolution) contains small historical Lean P0/P0.1 exercises and a proposed control-plane design. Those results are exploratory (`ITERATE`) and do not establish VSM advantage, safety assurance or Resolution adoption. The more recent technical P0.2 work remains incomplete. Existing private research materials must undergo a separate owner-approved disclosure review before any external sharing.

This potential institutional pilot is **distinct from the founder's individual Research Engineer application**. Either discussion can proceed—or stop—independently.

## Exit criteria

A modest pilot succeeds as a *feasibility assessment* if Resolution can give a grounded answer about:

- where the proposed VSM representation improves human comprehension and contributor interaction;
- where it obscures reality, adds friction, or lacks enforceable boundaries;
- whether controlled system modifications or Lean-based invariants are more inspectable under the approach;
- whether a second, more rigorous jointly designed experiment would be worthwhile.

A negative or inconclusive answer is a valid result. No hiring decision, organizational commitment, safety certification, autonomy grade, or performance improvement is implied by running the pilot.

## Context

Resolution's public account of the [Hironaka formalization](https://resolution.org/post/formalizing-resolution-of-singularities) motivates this research question: large-scale AI-assisted mathematics requires not just checked proofs but also maintainable structures that humans can inspect and direct. The proposed pilot concerns **research workflow legibility and control**, not a claim to replicate the Hironaka result, compute budget, agent capability or proof quality.
