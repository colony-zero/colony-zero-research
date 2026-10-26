# EXP-CZ-009 commitments (second casting)

Status: FROZEN 2026-10-25T03:32:59Z, before any member saw sealed set 2. Sealed run 2026-10-25T03:37:41Z to 04:17:33Z, after the freeze. Reported and REVEALED 2026-10-26, with EXP-CZ-010 and EXP-CZ-011 (reveal/EXP-CZ-009-011/); sealed set 2 is retired. The freeze record is EXP-CZ-009-freeze.txt in this folder, and EXP-CZ-009-freeze.txt.ots is its OpenTimestamps proof.

Bitcoin anchor: block 973012, 2026-10-25T03:58:36Z, about 21 minutes after the sealed run started (03:37:41Z). The commitment was pushed here at 03:37:28Z by GitHub's server log; see README.md, Timing evidence.

| Commitment | What it covers | Value |
|---|---|---|
| Sealed set 2 | SHA-256 of the task file: 1,200 tasks, 300 per family, no task shared with sealed set 1 | 578bc7a8e63dd1602a88318bed24ba24ffd9281a06c311a58130e1e1911a4297 |
| Sealed set 2 salt | SHA-256 of ASCII `cz-salt-commit-v1\|` plus the 32 raw salt bytes | e9dd57a6be3b5dd871476b54441710d5614007d0dd3f1b01a207ef449b3ce4b4 |
| Freeze commitment root | Per-field salted commitment to the full design | 1d3dc84533898b3375b5f936508ca3f774f596d0dbf47bbb7ced667a9fa1327c |
| Manifest digest | SHA-256 of the canonical JSON design | 1d8b7861b34343caa3c761e3147e468b881255b6a3b205cef9d1cc0290830651 |
| Manifest salt | SHA-256 of ASCII `cz-manifest-salt-commit-v1\|` plus the 32 raw manifest-salt bytes | 35c6b2c33583e4e4b7864add1b0ef5897edf0ad431856463c48c4aa301104356 |
| Freeze ledger root | Root of the one-event hash-chained freeze ledger | aade5eba2744874c63df6f2a56ec2987039aa4c6436f52f8dff2525609ec852c |

Sealed set 2 is shared with the targeted fine-tuning experiment (EXP-CZ-010) as a paired comparison, so it was revealed only after that experiment and EXP-CZ-011 had run on it. verify_reveal.py checks it (reveal/EXP-CZ-009-011/README.md); the EXP-CZ-009 manifest is revealed in full. It also checks the manifest file hash, 79aadf666e33049ab3581c21c4baf9b861e2b473928a366dd1a6feb45d873cf1, which is recorded in the freeze ledger and therefore covered by the freeze ledger root above.
