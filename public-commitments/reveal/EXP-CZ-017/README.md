# EXP-CZ-017 reveal (sealed set 3)

Status: NOT YET REVEALED. EXP-CZ-017 is reported; the reveal follows owner approval. This page lists exactly what will be added here. After the reveal, sealed set 3 is retired and never used for a sealed claim again.

## Files to be added

| File | What it is |
|---|---|
| sealed-s3-scored.jsonl | The 2,393 scored tasks of sealed set 3 with their reference answers |
| sealed_salt.hex | The 32-byte secret that generated sealed set 3, as 64 hex characters |
| manifest.json | The full frozen design |
| manifest_salt.hex | The 32-byte secret behind the per-field commitment, as 64 hex characters |
| manifest_reveal.json | Every field with its field salt and leaf, for checking one field at a time |
| freeze.jsonl | The one-event freeze ledger |

Nothing else is added: no weights, adapters or model files.

The salt generated 2,400 tasks. Seven of them repeat a prompt from a public file, an earlier sealed set, or set 3 itself by chance, so they were excluded before any run. The committed and revealed file is the 2,393 scored tasks.

## Verify in one command

From the public-commitments folder: `python3 verify_reveal.py reveal/EXP-CZ-017`

It needs only Python 3. It checks, against values published before the reveal (../../EXP-CZ-017.md): the sealed task file hash, the sealed salt commitment, the manifest salt commitment, the manifest file hash, the manifest digest (SHA-256 of its canonical JSON), the commitment root rebuilt field by field, and the freeze ledger (every event hash, its root, and the commitments its freeze event records). Each line prints PASS or FAIL.

The OpenTimestamps proof (../../EXP-CZ-017-freeze.txt.ots) shows when the freeze root existed. Check it with the standard OpenTimestamps client (`ots verify`), and read the timing note on the commitment page: the commitment was published after the runs, and the Bitcoin anchor is the only timing evidence.

## Run ledgers

The sealed-run ledgers and result files will be a release asset of this repository, with its SHA-256 listed here at release: the 13 planned runs and the 9 exploratory runs of the untrained founders. Each ledger is hash-chained, and its last hash is the ledger root listed in RESULTS.md. Each result file carries the sealed task file hash it ran against.

## What the reveal does not let you do

Regenerating the tasks from the salt needs the task generator, which is not published.

## Release asset

`EXP-CZ-017-sealed-run-ledgers.tar.gz`, SHA-256 `ba6930c6be4b6f36c423756153b82b30fee87ee1169e966a3a2c157104540642`: result JSON and ledger JSONL for all 22 sealed set 3 runs, plus a SHA256SUMS file.
