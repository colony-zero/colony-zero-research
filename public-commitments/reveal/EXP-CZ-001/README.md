# EXP-CZ-001 reveal

Revealed 2026-10-25, after the sealed run. This sealed set is now retired: it will never be used for a sealed claim again.

| File | What it is |
|---|---|
| sealed1200.jsonl | The 1,200 sealed tasks with their reference answers |
| sealed_salt.hex | The 32-byte secret that generated them, as hex |
| manifest.json | The full frozen design |
| manifest_salt.hex | The 32-byte secret behind the per-field commitment, as hex |
| manifest_reveal.json | Every field with its field salt and leaf, for checking one field at a time |

## Verify in one command

From the public-commitments folder: `python3 verify_reveal.py reveal/EXP-CZ-001`

It needs only Python 3 and checks five things against values published before the run: the sealed task file hash, the sealed salt commitment, the manifest salt commitment, the manifest digest (SHA-256 of its canonical JSON) and the commitment root. Each line prints PASS or FAIL. The OpenTimestamps proof for the freeze record (../../EXP-CZ-001-freeze.txt.ots) shows when those values existed; check it with the standard OpenTimestamps client (`ots verify`).

## Run ledgers

Release assets of this repository, tag exp-cz-001-reveal:

| Asset | SHA-256 |
|---|---|
| EXP-CZ-001-sealed-run-ledgers.tar.gz (8 sealed runs with their result files) | 985b61f4730f4117b436a6c28c636c9fcb62a59a143a54604e4a48f98e044575 |
| EXP-CZ-001-dev-ledgers.tar.gz (Phase 0, Phase 1, Phase 1 v2) | 1e576745dc65ff1a4d3ad4641e55900a736720e3464fc6b814f3f690eeacbad6 |

Each ledger is hash-chained: every event records the hash of the one before it, and the last hash is the ledger root listed in RESULTS.md and RESULTS_SO_FAR.md. Each result file also carries the sealed task file hash it ran against.

## What the reveal does not let you do

Regenerating the tasks from the salt needs the task generator, which is not published. The task file hash, the salt commitment and the ledger roots are checkable now. Before the reveal, our own check regenerated the 1,200 tasks from the salt with the frozen generator and matched the committed file hash byte for byte.
