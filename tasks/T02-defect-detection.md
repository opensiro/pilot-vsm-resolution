# T02 — Deliberately invalid theorem

**Input:** `fixtures/InvalidProof.lean`, which incorrectly asserts that reversing `[1,2]` gives `[1,2]`.

**Task:** invoke `lake env lean fixtures/InvalidProof.lean` independently of the positive build.

**Acceptance:** compiler **must fail**, with a Lean error diagnostic. A timeout, missing executable, Python-only scan, or silent skipping is not a successful negative test. The fixture is intentionally excluded from the `Pilot` library build.

**Purpose:** test if the real verification path catches a concrete false claim. It does **not** establish broad vulnerability detection or independent AI review.
