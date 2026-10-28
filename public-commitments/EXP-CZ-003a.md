# EXP-CZ-003a commitments (who does what: routing across the colony)

Status: COMMITTED 2026-10-28, not yet run. This page and its freeze record are pushed here before any sealed run. Sealed set 4 and its salt stay secret until the report. The freeze record is EXP-CZ-003a-freeze.txt in this folder, and EXP-CZ-003a-freeze.txt.ots is its OpenTimestamps proof. That proof was submitted at about 2026-10-28T03:00Z and is anchored in Bitcoin block 973489, mined at 2026-10-28T03:10:30Z. No sealed run started before the anchor verified.

| Commitment | What it covers | Value |
|---|---|---|
| Sealed set 4, scored file | SHA-256 of the 3,581 scored tasks (3,600 generated; 19 that repeat a public or earlier prompt were excluded before any run) | 525da50809ff284fe5e4ee458320e5a01152717e8c7ca089b72317435914a530 |
| Sealed set 4 salt | SHA-256 of ASCII `cz-salt-commit-v1\|` plus the 32 raw salt bytes | 0d3724b9d80714aa27a0284d6fc525e150a0c055176f0a7aa7e15d2312a2d617 |
| Freeze commitment root | Per-field salted commitment to the full design | a8f0663504e03c7c2ce455aff69203351ca3432842b958b39d52b802d18c2c6e |
| Manifest digest | SHA-256 of the canonical JSON design | e455e58c029263e0c3e50d948083578ebe8cf560a7fedf7cf693563fa7ba7574 |
| Manifest file | SHA-256 of the manifest file as written | 5a114f2bc73696ea5a3a2e8bf87dda6fc4db4c4ab41b35bead47a7b6dbbe1227 |
| Manifest salt | SHA-256 of ASCII `cz-manifest-salt-commit-v1\|` plus the 32 raw manifest-salt bytes | 63eb8c0e1be202d8bc1cfe493126cc46508f61c7056093c82113ade9356ad804 |
| Freeze ledger root | Root of the one-event hash-chained freeze ledger | 5123db066ad93aef1bf0c5aba30453cc8619b3362443b53ec076ca8fa0f2d988 |
| Freeze ledger file | SHA-256 of the freeze ledger file | d6b3522c3775d89ddeace891bdb54f1870afa14954c3933f21562d3e66e18f73 |

The freeze record lists the commitment root, the freeze ledger root, the manifest file hash and the freeze ledger file hash. The freeze ledger's one event records every other value in this table, so the timestamp on the record dates all of them.

## What comes next

After the sealed runs, a post-run record of result hashes is pushed and timestamped here before any scoring. A Bitcoin block mined after that record then picks which route records are re-verified, so nobody could choose them in advance.
