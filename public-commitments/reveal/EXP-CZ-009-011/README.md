# EXP-CZ-009, EXP-CZ-010 and EXP-CZ-011 reveal (sealed set 2)

Status: NOT YET REVEALED. All three experiments are reported; the reveal follows owner approval. This page lists exactly what will be added here. After the reveal, sealed set 2 is retired and never used for a sealed claim again.

## Files to be added

At the top of this folder, shared by the three experiments:

| File | What it is |
|---|---|
| sealed1200-s2.jsonl | The 1,200 tasks of sealed set 2 with their reference answers |
| sealed_salt.hex | The 32-byte secret that generated them, as 64 hex characters |

In each of EXP-CZ-009/, EXP-CZ-010/ and EXP-CZ-011/:

| File | What it is |
|---|---|
| manifest.json | The full frozen design |
| manifest_salt.hex | The 32-byte secret behind the per-field commitment, as 64 hex characters |
| manifest_reveal.json | Every field with its field salt and leaf, for checking one field at a time |
| freeze.jsonl | The one-event freeze ledger |

Nothing else is added: no weights, adapters or model files.

## Verify in one command

From the public-commitments folder: `python3 verify_reveal.py reveal/EXP-CZ-009-011`

It needs only Python 3. For each experiment it checks, against values published before the reveal (../../EXP-CZ-009.md, EXP-CZ-010.md, EXP-CZ-011.md): the sealed task file hash, the sealed salt commitment, the manifest salt commitment, the manifest file hash, the manifest digest (SHA-256 of its canonical JSON), the commitment root rebuilt field by field, and the freeze ledger (every event hash, its root, and the commitments its freeze event records). Each line prints PASS or FAIL.

The OpenTimestamps proofs (../../EXP-CZ-0xx-freeze.txt.ots) show when the freeze roots existed. Check them with the standard OpenTimestamps client (`ots verify`). For EXP-CZ-010 and EXP-CZ-011, read the timing note on their commitment pages: their commitments were published after the runs, and the Bitcoin anchor is the only timing evidence.

## Run ledgers

The sealed-run ledgers and result files will be release assets of this repository, one archive for the three experiments, with its SHA-256 listed here at release: the 9 EXP-CZ-009 runs, the 8 untrained control reruns, the 8 self-taught runs and the 8 teacher-taught runs. Each ledger is hash-chained, and its last hash is the ledger root listed in the experiment's RESULTS.md. Each result file carries the sealed task file hash it ran against.

## What the reveal does not let you do

Regenerating the tasks from the salt needs the task generator, which is not published. The task file hash, the salt commitment and the ledger roots are checkable.
