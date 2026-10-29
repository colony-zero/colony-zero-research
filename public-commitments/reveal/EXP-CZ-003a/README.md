# EXP-CZ-003a reveal (sealed set 4)

Status: REVEALED 2026-10-29, after the experiment was run and reported. Sealed set 4 is retired and will not be used for another sealed claim.

## Files

| File | What it is |
|---|---|
| sealed-s4-scored.jsonl | The 3,581 scored tasks of sealed set 4 with their reference answers |
| sealed_salt.hex | The 32-byte secret that generated sealed set 4, as 64 hex characters |
| manifest.json | The frozen experiment design |
| manifest_salt.hex | The 32-byte secret behind the per-field commitment, as 64 hex characters |
| manifest_reveal.json | The design fields and their field salts used to rebuild the commitment root |
| freeze.jsonl | The one-event freeze ledger |

The salt generated 3,600 tasks. Nineteen prompts repeated a public or earlier prompt and were excluded before any run. The revealed scored file contains the remaining 3,581 tasks.

## Verify in one command

From the `public-commitments` folder:

`python3 verify_reveal.py reveal/EXP-CZ-003a`

It needs only Python 3. It checks the sealed task file hash, sealed-salt commitment, manifest-salt commitment, manifest file hash, canonical manifest digest, commitment root rebuilt field by field, and the freeze ledger. Each line prints PASS, FAIL, or SKIP. Values are checked against the commitment page at ../../EXP-CZ-003a.md.

The OpenTimestamps proof at ../../EXP-CZ-003a-freeze.txt.ots shows when the freeze root existed. Verify it with the standard OpenTimestamps client: `ots verify ../../EXP-CZ-003a-freeze.txt.ots`.

## Run ledgers and route records

Release asset of this repository, tag exp-cz-003a-reveal:

| Asset | SHA-256 |
|---|---|
| EXP-CZ-003a-sealed-run-ledgers.tar.gz (result JSON and ledger JSONL for all 30 sealed set 4 runs, the 7 route records, and a SHA256SUMS file) | 229406f4e0d80957f1ac9035876b1c8ab2d6993337abee899111c3d9aef654a0 |

The 30 runs are the 27 greedy member runs and the 3 self-consistency runs. The route records are the base-Laya embedding record, the Laya zero-shot record and the five Laya fine-tuned records. Every one of these 67 files matches its SHA-256 in the post-run record (../../EXP-CZ-003a-postrun.txt), which was timestamped in Bitcoin before scoring. Each ledger records a verdict for every task, so the solve counts in experiments/EXP-CZ-003a/RESULTS.md can be recomputed from the ledgers.

## What the reveal does not let you do

- Regenerate the tasks from the salt, because the task generator is not published.
- Recompute verdicts from model answers, because the runner and checker source are not public.
- Reproduce the sealed member runs or the learned-route records yourself: that needs the members' weights and the route program, which are not published. The release lets you check the recorded runs and route records against the post-run record.
