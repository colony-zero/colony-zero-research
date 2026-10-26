# EXP-CZ-010 commitments (self-taught adapters)

Status: REVEALED 2026-10-26; the manifest reveal is partial (see below). Published after the runs; externally anchored no later than Bitcoin block 973187 (2026-10-26T04:42:29Z). Our own freeze record gives 2026-10-26T04:30:59Z, before any adapter saw sealed set 2; that time is not independently established. The freeze record is EXP-CZ-010-freeze.txt in this folder, and EXP-CZ-010-freeze.txt.ots is its OpenTimestamps proof.

| Commitment | What it covers | Value |
|---|---|---|
| Sealed set 2 | SHA-256 of the task file, shared with EXP-CZ-009 and EXP-CZ-011 | 578bc7a8e63dd1602a88318bed24ba24ffd9281a06c311a58130e1e1911a4297 |
| Sealed set 2 salt | SHA-256 of ASCII `cz-salt-commit-v1\|` plus the 32 raw salt bytes | e9dd57a6be3b5dd871476b54441710d5614007d0dd3f1b01a207ef449b3ce4b4 |
| Freeze commitment root | Per-field salted commitment to the full design (12 fields) | 1468e1c64dbae2ac9b6cf2e482db2bf46a6cee122c6a4f1160ff2c85b9a70237 |
| Manifest digest | SHA-256 of the canonical JSON design | 0aa38df1b86d030daba8f21512b9c0802cce48bc676d142d47ab5beae1e24d98 |
| Manifest file | SHA-256 of the manifest file as written | 0cb7e715fa333564b44b1c6050e926f6d8c14a99d0b9be31db68f97cda4d8965 |
| Manifest salt | SHA-256 of ASCII `cz-manifest-salt-commit-v1\|` plus the 32 raw manifest-salt bytes | 1e23a0f06cdd7c1469f0fbc973d05b67de14916292aae53d72855ec3372bff15 |
| Freeze ledger root | Root of the one-event hash-chained freeze ledger | 7f0b925d9e5fd4d7b55f32637e2943def7a10300e45d87a50c190b428e6cefdf |

The freeze record lists the commitment root and the freeze ledger root. The freeze ledger's one event records every other value in this table, so the timestamp on its root dates all of them.

## Timing

By our own record, EXP-CZ-010, EXP-CZ-011 and EXP-CZ-017 were frozen together at 04:30:59Z; that time is not independently established. Their freeze record was submitted to OpenTimestamps at about 04:33Z, and the proof is anchored in Bitcoin block 973187, mined at 2026-10-26T04:42:29Z. Our own rule says each commitment is pushed to this repository and timestamped before its sealed run. These were not pushed before the runs, and the sealed set 2 driver started at 04:32:02Z, before the timestamp was even submitted. So the only external timing evidence is the Bitcoin anchor: the commitments existed no later than block 973187. Every adapter run started after it (the first at 05:08:02Z). The runs that started before it were five untrained control runs (04:32:02Z to 04:42:28Z), whose results equal EXP-CZ-009's sealed results exactly. Details: ../experiments/EXP-CZ-010/RESULTS.md.

Confirmatory status: Every adapter run began after the anchor; five untrained control runs began before it.

## Reveal

Sealed set 2 and its salt were revealed on 2026-10-26 (reveal/EXP-CZ-009-011/README.md), and the set is retired. The manifest reveal is partial: the fields `models` and `task_spec` are withheld and published only as their committed leaves, because they contain local file paths, which our publication policy does not allow. verify_reveal.py checks the per-field commitment root, but it cannot check the manifest file hash or the canonical digest in the table above, and the model file hashes and artifact bindings inside `task_spec` cannot be audited publicly. The full manifest may be published later if the owner grants an exception to the policy.
