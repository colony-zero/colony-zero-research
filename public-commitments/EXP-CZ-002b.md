# EXP-CZ-002b commitments

Status: REPORTED and REVEALED 2026-11-11. Results: [../experiments/EXP-CZ-002b/RESULTS.md](../experiments/EXP-CZ-002b/RESULTS.md). Preregistration: [../experiments/EXP-CZ-002b/PREREGISTRATION.md](../experiments/EXP-CZ-002b/PREREGISTRATION.md).

## Commitment chain

| Record | Purpose | Bitcoin anchor |
|---|---|---|
| COMMIT-COUNCIL | Council ballots, template, packet and pool, before any leave-one-out score | block 975331 |
| COMMIT-PREGEN | Freeze record, kit manifest, binaries, scorer, selection and R-draw code, salt commitments | block 975331 |
| COMMIT-PRERUN-S | Selection set S and its overlap summary, before any S task was read | block 975342 |
| SELECT | S ledger roots of the five configurations, contribution table, e | block 975368 |
| R draw | r drawn from the hash of block H_SELECT + 6, read from two explorers | block 975374 (the beacon block) |
| COMMIT-PRERUN-V | Evaluation set V, its overlap summary, SELECT and the R draw, before any V task was read | block 975377 |
| POSTRUN | Hash of the private record of every evaluation file and ledger root, before scoring | block 975487 |
| BEACON | Digest-only beacon receipt at H_POSTRUN + 6 | no proof of its own; binds the anchored POSTRUN |

The source records and their OpenTimestamps proofs are in [../commitments/EXP-CZ-002b/](../commitments/EXP-CZ-002b/).

## Reveal

[reveal/EXP-CZ-002b/](reveal/EXP-CZ-002b/) holds the four freeze-record versions, the SELECT and R-draw records, the POSTRUN and BEACON records, score.json, both sealed task sets with generation summaries and sealed manifests, the Council ballots and both salt files. SHA256SUMS lists every file and the release asset. The release `exp-cz-002b-reveal` carries `exp-cz-002b-ledgers.tar.gz`: 63 result, ledger and timing files plus the per-arm outcome files.

To check by hand: FREEZE_RECORD-PREGEN.json and FREEZE_RECORD-PRERUN-S.json hash to `private_freeze_record_sha256` in COMMIT-PREGEN and COMMIT-PRERUN-S; the PRERUN-V and POSTRUN versions differ from PRERUN-S only by the phase and the hashes that COMMIT-PRERUN-V publishes. Each salt file hashes to its commitment in COMMIT-PREGEN. S-tasks.jsonl and V-tasks.jsonl hash to the task-file values in COMMIT-PRERUN-S and COMMIT-PRERUN-V, and the generation summaries to the overlap-summary values there. SELECT_RECORD.json hashes to `private_select_record_sha256` in SELECT, RDRAW_RECORD.json to `rdraw_record_sha256` in COMMIT-PRERUN-V, and POSTRUN_RECORD.txt and BEACON_RECORD.txt to POSTRUN and BEACON. POSTRUN_RECORD.txt lists the hash of every released ledger.

Withheld, with reasons, as listed in the results page: the kit manifest and the Council summary (hash-bound, and they name run-host paths or the host), two timing sidecars, server logs and host sidecars. There is no automated verifier for this experiment yet, and the generator is not published, so the sets cannot be regenerated from the salts here.
