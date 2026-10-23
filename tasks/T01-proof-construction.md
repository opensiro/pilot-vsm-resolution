# T01 — Construct and formalize a small proof

**Input:** `Pilot/Core.lean` (generic list append/reverse) and the [registered protocol](../PROTOCOL.md).

**Task:** implement custom append/reverse, prove append-neutrality and associativity, prove reverse-append and reverse-involution by induction; add a downstream use site in `Pilot/Verification.lean`.

**Acceptance:** `lake build Pilot` returns 0 under `leanprover/lean4:v4.35.0`; source checks forbid `sorry` / `admit` in the positive files. Built-in Lean tactics may assist, but only the kernel-checked artifact counts.

**Purpose:** test a tiny proof-construction/refactoring workflow, not the novelty or mathematical difficulty of the lemmas. A successful construction could occur with ordinary software-engineering structure.
