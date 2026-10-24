# EXP-CZ-001 commitments

Status: the freeze commitment root is not yet published. Values below are the two commitments made so far.

| Commitment | What it covers | Value |
|---|---|---|
| Salt commitment | The secret salt that generates the sealed tasks | 944c6a61135558626cf27bc7897b3ced84bd8f71920bf8304dfbfd10587ebe4b |
| Sealed task file | SHA-256 of the sealed task file: 1,200 tasks, 300 per family | 0a60bd438ddabbea9e2cc92d640b6b0437ffac7f7db8bddf34881003d0cd8388 |

freeze commitment root: PENDING

How to verify: see README.md in this folder. When the sealed run is done, we reveal the task file and the salt. The task file must hash to the sealed task file value above. The salt must hash to the salt commitment above, using the recipe published with the reveal.
