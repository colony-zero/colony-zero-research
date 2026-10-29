# EXP-CZ-003a commitments (who does what: routing across the colony)

Status: RUN 2026-10-28, not yet scored. This page and its freeze record were pushed here before any sealed run. Sealed set 4 and its salt stay secret until the report. The freeze record is EXP-CZ-003a-freeze.txt in this folder, and EXP-CZ-003a-freeze.txt.ots is its OpenTimestamps proof. That proof was submitted between the freeze at 2026-10-28T02:50:41Z and the push that carried it at 02:54:10Z (GitHub server time), and is anchored in Bitcoin block 973489, mined at 2026-10-28T03:10:30Z. The first sealed run started at 2026-10-28T04:20:02Z, after the anchor verified.

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

## Post-run record

The sealed runs finished at 2026-10-28T13:48:39Z and the route records at about 2026-10-29T02:05Z. Before any scoring, EXP-CZ-003a-postrun.txt in this folder lists the SHA-256 of all 97 files the scorer will read: each run's result, ledger and command file, and every route record. Its own SHA-256 is 554e6ca09728109043036981222fafbd7cee8677364dd48a38fccdaf6d5a8bad. EXP-CZ-003a-postrun.txt.ots is its OpenTimestamps proof, submitted at about 2026-10-29T02:11Z and anchored in Bitcoin block 973627, mined at 2026-10-29T02:18:57Z. The verification beacon is block 973633. The scorer refuses to run unless every file still matches this record.

## Deviations recorded before scoring

Three post-run scripts that were frozen with the design had bugs that stopped them before they did any work. We did not edit them, because each is bound by hash to the freeze. Instead, each ran unchanged with a small wrapper that fixes one call. All three are written up in full in the report.

1. Route records and scoring called the integrity check without the experiment folder it needs, so it refused. The wrapper supplies the folder. The check itself runs in full.
2. Route records stopped at the first record, because deleting a file that did not exist yet counted as a failure. The wrapper makes that one delete succeed when there is nothing to delete.
3. The post-run hash command was garbled in transit (shell quoting) and was longer than the Windows command-line limit. The wrapper sends the same SHA-256 hashing command intact and shorter.

None of the three changes a hypothesis, margin, test, task or route program. Each was found and fixed before the step it affects produced any output.

## What comes next

Once the post-run record's proof is anchored in a Bitcoin block, the block six above it picks which route records are re-verified, so nobody could choose them in advance. Then the scorer runs and the report follows.
