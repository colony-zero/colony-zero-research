# EXP-CZ-002 commitments

Status: REPORTED. The scored sealed set and the verification material are in [reveal/EXP-CZ-002/](reveal/EXP-CZ-002/). The release contains no task content outside the scored set and no candidate set. Its result JSONs and ledgers contain task-level execution evidence, including task identifiers, answers, and verdict status. This Markdown page publishes no outcome values from those records.

## Commitment chain

| Record | Purpose | Bitcoin anchor |
|---|---|---|
| PREGEN | Frozen kit and pre-generation identity | block 974697 |
| PRERUN | Frozen scored-set and run identity | blocks 974714 and 974715 |
| POSTRUN | Scoring input inventory | blocks 974919 through 974921 |
| BEACON | Digest-only scoring-release receipt | No OpenTimestamps proof or Bitcoin block was published |
| AMEND-A1 | Text-ledger identity acceptance | blocks 974909 and 974912 |
| AMEND-A2 | Amended checkout authentication | block 974935 |
| AMEND-A3 | Historical beacon receipt handling | blocks 974953 and 974956 |
| AMEND-A4 | Scorer-output staging | blocks 974970 and 974974 |
| AMEND-A5 | Scorer acceptance-rule replacement | block 975002 |
| AMEND-A6 | Authenticated scorer source-hash check | block 975020 |

The source records and, where published, their OpenTimestamps proofs are in [commitments/EXP-CZ-002/](../commitments/EXP-CZ-002/). A1 through A6 are disclosed in [the results](../experiments/EXP-CZ-002/RESULTS.md) and [operations record](../experiments/EXP-CZ-002/OPERATIONS.md). No score existed before these amendments. The scoring math, thresholds, task bytes, and ledger bytes were not changed by the amendments.

Run `python3 public-commitments/verify_reveal.py public-commitments/reveal/EXP-CZ-002 exp-cz-002-reveal.tar.gz` from the repository root after downloading the release asset. The verifier checks the fixed local scored-set file, salt format and commitment, the PREGEN and PRERUN records, the hardcoded hashes of PREGEN, PRERUN, POSTRUN, BEACON, and AMEND-A1 through AMEND-A6, the POSTRUN digest list against all 44 released result and ledger files, the 46-file release manifest, and the scorer-envelope bindings to PRERUN, POSTRUN, BEACON, A5, and A6.

This check does not deterministically regenerate the scored set because the generator and preparation implementation are not published here. The prior consumed domains remain sealed, so it also cannot replay the final overlap audit against those domains. The private staging procedure verifies those bindings before it copies the public-safe reveal material.
