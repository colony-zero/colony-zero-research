# EXP-CZ-017 commitments (first children: Theo and Hazel)

Status: FROZEN 2026-10-26T04:30:59Z, before any child saw sealed set 3. Published here after the sealed runs; see "Timing" below. The freeze record is EXP-CZ-017-freeze.txt in this folder, and EXP-CZ-017-freeze.txt.ots is its OpenTimestamps proof.

| Commitment | What it covers | Value |
|---|---|---|
| Sealed set 3, scored file | SHA-256 of the 2,393 scored tasks (2,400 generated; 7 that repeat a public or earlier prompt by chance were excluded before any run) | 7531dc118f7991dbaaf7720c4a512923b0fc072ec2f146e1ee932dee78873136 |
| Sealed set 3 salt | SHA-256 of ASCII `cz-salt-commit-v1\|` plus the 32 raw salt bytes | 4ed91e22a8e6b450cf04d4d76af727766dab0429249be008dfe67dd531e67dfe |
| Freeze commitment root | Per-field salted commitment to the full design (12 fields) | 55a51dd37ca213dbc6ee99f51ca59b5baca1f747919a1ce567d06c9b7dd9500a |
| Manifest digest | SHA-256 of the canonical JSON design | 4c2b76347d85c79e643858b905b69ea4d6e43d214e4713dca1a48b5422466d05 |
| Manifest file | SHA-256 of the manifest file as written | 2c5ab6893fddd502a8bbbdb0d067f04ea7c6b06e1d3991443df7cded83f29aa1 |
| Manifest salt | SHA-256 of ASCII `cz-manifest-salt-commit-v1\|` plus the 32 raw manifest-salt bytes | 18bbfdc47bc251e5fbc1b4580a57a278aa0f64d28e2e71876cf198cc3f35b3fb |
| Freeze ledger root | Root of the one-event hash-chained freeze ledger | 35c648e696ae3b8c601fce5fb4930927c8179db5488f6b9155e8f851ebaf57b8 |

The freeze record lists the commitment root and the freeze ledger root. The freeze ledger's one event records every other value in this table, so the timestamp on its root dates all of them.

## Timing

EXP-CZ-010, EXP-CZ-011 and EXP-CZ-017 were frozen together at 04:30:59Z. Their freeze record was submitted to OpenTimestamps at about 04:33Z, and the proof is anchored in Bitcoin block 973187, mined at 2026-10-26T04:42:29Z. Our own rule says each commitment is pushed to this repository and timestamped before its sealed run. These were not pushed before the runs. So the only timing evidence is the Bitcoin anchor. Every EXP-CZ-017 run started after it (the first at 06:46:24Z). Details: ../experiments/EXP-CZ-017/RESULTS.md.

Sealed set 3, its salt, the manifest and its salt will be revealed after owner approval (reveal/EXP-CZ-017/README.md). verify_reveal.py already holds the values above.
