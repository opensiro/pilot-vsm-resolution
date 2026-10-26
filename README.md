# OpenSiro Research Automation — VSM-RES-001

**Independent feasibility portfolio and pilot record.** OpenSiro is exploring whether scientific AI workflows can keep research intent, execution, review, and claim admission traceable under explicit organizational decision rights.

**Not a Resolution project or collaboration.** This repository is an independent OpenSiro study motivated in part by Resolution's public work on research automation. It does not establish performance parity, comparative VSM benefit, or adoption by Resolution.

**Prospective use:** make AI-assisted research systems legible to humans—who acts, who decides, which boundaries are enforceable, and how interventions return to operation—as a foundation for investigating AI safety. Standardization, contributor interoperability and onboarding are additional goals; agent throughput improvements are **not assumed**. See the [draft collaboration proposal](docs/RESOLUTION_COLLABORATION_PROPOSAL.md).

## Start here

| Reading path | Document | What it establishes |
| --- | --- | --- |
| **1. Existing work** | [Redacted Research Automation Case Study](docs/RESEARCH_AUTOMATION_CASE_STUDY.md) | A completed **private, exploratory** harness exercise summarized without source disclosure: three bounded trials, ordinary evaluation, complementary review, and explicit limits. External sharing requires **owner disclosure review**. |
| **2. Prospective method** | [Minimal Research Control Plane design](docs/RESEARCH_CONTROL_PLANE_DESIGN.md) | A simple governance → operations → evidence view, separated from formal S1–S5 function/ownership claims. **Design only**, not a new executed experiment. |
| **3. Earlier technical evidence** | [P0 feasibility assessment](reports/P0_FEASIBILITY.md) and [P0.1 replication](experiments/P0-002/RESULTS.md) | Narrow Lean 4 proof and error-checking feasibility, including an external-host replication. Both retain `ITERATE`. |
| **4. Prospective collaboration** | [OpenSiro × Resolution proposal](docs/RESOLUTION_COLLABORATION_PROPOSAL.md) | **Draft only:** human-legible and governable AI research as an AI-safety foundation, qualitative contributor onboarding, and controlled system-modification/Lean pilot options requiring Resolution's joint evaluation. |

### Current status — 2026-10-26

| Track | Status | Evidence boundary |
| --- | --- | --- |
| **Research Automation case study** | **Completed; merged in [PR #8](https://github.com/opensiro/pilot-vsm-resolution/pull/8)** | Retrospective, redacted narrative of a **separate private harness**. It is not a publicly reproducible software demo, a VSM-effect result, or the source of the separate AAMAS 2027 paper's outcomes. |
| **Research Control Plane** | **Proposed** | Function-first design only; no positive S1–S5 ownership/autonomy grades inferred. S3* is excluded from this pilot's current scope. |
| **Lean P0 and P0.1** | **Executed; `ITERATE`** | Limited technical verification and reproducibility, not a matched baseline or evidence of VSM superiority. |
| **Technical P0.2 runner** | **Deferred, incomplete; issue reopened** | [Open issue #5](https://github.com/opensiro/pilot-vsm-resolution/issues/5) / [open PR #6](https://github.com/opensiro/pilot-vsm-resolution/pull/6): Python tests passed, but no live P0.2 Lean run or S3 closure result is claimed. |

## Scope and scientific standards

This repository distinguishes **protocol**, **execution**, **raw evidence**, **review**, **decision**, and **scientific claim**. An organizational component or static policy label does not demonstrate a VSM function. A function requires observed disturbances, actual decision rights, exercised action, and observable return at a declared system boundary.

- **What exists:** a redacted external-facing case study, an exploratory Lean PoC with historical receipts, and a proposed research-control architecture.
- **What remains unverified:** a new non-Lean live demonstration, independently inspectable evidence for the private case study, a real inter-S1 coordination closure, a prospective S4 return, and any causal advantage from VSM over a coherent baseline.
- **Evidence policy:** preserve negative/null outcomes, human interventions, unavailable costs, and failures. Historical results are not rewritten to match new research priorities.
- **Publication boundary:** the case study deliberately omits private harness code, prompts, configuration, raw traces, internal paths, and secrets. Its presence in this **private repository is not authorization to distribute it externally**.

## Historical Lean feasibility pilot (P0 / P0.1)

The original P0 asked whether a small, bounded workflow could produce independently checkable Lean artifacts, detect a deliberate error, and preserve sufficient receipts for a future controlled experiment. It did **not** attempt to replicate Resolution's much larger Hironaka effort.

### Reproduce the original P0 locally

Requires Python 3.10+ and Lean/Lake matching [`lean-toolchain`](lean-toolchain). Mathlib is not required.

```sh
python3 -m unittest discover -s scripts -p 'test_*.py' -v
python3 scripts/run_pilot.py --output experiments/local-run
```

The runner builds the valid Lean library and verifies that an intentionally invalid theorem fails elaboration. The supplementary check runs `lake env leanchecker Pilot`. A source-only check is **not** proof verification. Each invocation needs a fresh output directory; the runner refuses to overwrite evidence. The [CI workflow](.github/workflows/p0-lean.yml) runs the same checks and Python tests; inspect [actual Actions runs](https://github.com/opensiro/pilot-vsm-resolution/actions) before claiming CI passed. Historical unsuccessful CI runs, including the earlier `BlobNotFound` log-retrieval limitation, remain part of the P0 record.

### Historical evidence and implementation

- [Frozen P0 protocol](PROTOCOL.md) and [task descriptions](tasks/) ([T01](tasks/T01-proof-construction.md), [T02](tasks/T02-defect-detection.md), [T03](tasks/T03-independent-check.md)).
- [Proof of Concept report](docs/PROOF_OF_CONCEPT.md), [P0 feasibility and `ITERATE` decision](reports/P0_FEASIBILITY.md).
- [P0-001 primary results](experiments/P0-001/RESULTS.md) and [underlying experiment record](experiments/P0-001/).
- [P0-002 second-host results](experiments/P0-002/RESULTS.md).
- [Scripts and deterministic checks](scripts/).

The historical feasibility report contains preliminary S2/S4 interpretations. **Do not treat sequencing alone as S2, or recovery from an internal infrastructure problem as S4.** The later [function-first design review](docs/RESEARCH_CONTROL_PLANE_DESIGN.md) records the stricter evidence boundaries without changing historical receipts.

## Methodological references

- [OpenSiro VSM Profile v0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/527fe01ccf1ee22e54bd9525285a89a93179c1e7/PROFILE.md) — normative S1–S5 semantics, ownership, autonomy.
- [OpenSiro Assessment Methodology v0.3.8](https://github.com/opensiro/vsm-harness-skills/tree/5d36fd2e40e4e8a1711b1f315f7a60a9a78a2a25/skills/assess-vsm-harness) — distinct from this pilot's exploratory mapping.
- [OpenSiro VSM OSS Organization](https://github.com/opensiro/vsm-oss-organization) — existing applied contributor/onboarding/control reference, not a second normative standard.
- [Resolution's public Hironaka research](https://resolution.org/post/formalizing-resolution-of-singularities) and [source snapshot](https://github.com/resolutionorg/hironaka/tree/044d89c9455859446fc5e986667319f910e15f4b) — motivation and context, **not** the comparison baseline.

No Resolution affiliation, endorsement, adoption, or comparative effectiveness is implied.
