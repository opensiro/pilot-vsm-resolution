# P0-A01 — supplemental checker (post-run amendment)

**2026-10-23; after first successful local T01/T02 receipt.** Original registered protocol: [`PROTOCOL.md`](../../PROTOCOL.md), version P0-v0.1. This amendment is explicitly **post hoc** and is not a primary end-point change.

Additional observation: run `lake env leanchecker Pilot` on built Lean `.olean` proof artifacts, record exit code and separate logs. A successful exit is evidence of an additional machine check; it does not supply blinded human/agent S3* judgment, demonstrate VSM superiority, or change T01/T02 pass/fail criteria.

Older receipt `runs/2026-10-23-local-lean435-001` remains valid without this new field. The next run includes `supplemental_P0_A01` and is reported separately. Do not reinterpret older records as including this check.
