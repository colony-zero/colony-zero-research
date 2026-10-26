# EXP-CZ-017 reveal (sealed set 3)

Status: REVEALED 2026-10-26, after the experiment was run and reported. Sealed set 3 is now retired: it will never be used for a sealed claim again.

The manifest reveal is partial; see "Partial manifest reveal" below.

## Files

| File | What it is |
|---|---|
| sealed-s3-scored.jsonl | The 2,393 scored tasks of sealed set 3 with their reference answers |
| sealed_salt.hex | The 32-byte secret that generated sealed set 3, as 64 hex characters |
| manifest_salt.hex | The 32-byte secret behind the per-field commitment, as 64 hex characters |
| manifest_reveal.json | Ten of the twelve fields with their field salts, plus the committed leaves of the two withheld fields |
| freeze.jsonl | The one-event freeze ledger |

No weights, adapters or model files are published.

The salt generated 2,400 tasks. Seven of them repeat a prompt from a public file, an earlier sealed set, or set 3 itself by chance, so they were excluded before any run. The committed and revealed file is the 2,393 scored tasks.

## Partial manifest reveal

Two manifest fields, `models` and `task_spec`, are withheld and published only as their committed leaves, because they contain local file paths, which our publication policy does not allow. The manifest.json file is therefore not published. This has consequences:

- The verifier rebuilds the per-field commitment root from the ten revealed fields and the two withheld leaves, so it shows that the revealed fields are the committed ones.
- It cannot check the manifest file hash or the canonical manifest digest, and prints SKIP for them.
- The model file hashes and the artifact bindings inside `task_spec` (runner, analysis program, training data and the full generated set) cannot be audited publicly. The child file hashes also appear in the revealed `arms` field.

The full manifest may be published later if the owner grants an exception to the policy.

## Verify in one command

From the public-commitments folder: `python3 verify_reveal.py reveal/EXP-CZ-017`

It needs only Python 3. It checks, against the values on the commitment page (../../EXP-CZ-017.md): the sealed task file hash, the sealed salt commitment, the manifest salt commitment, the commitment root rebuilt field by field, and the freeze ledger (every event hash, its root, and the commitments its freeze event records). Each line prints PASS, FAIL or SKIP.

The OpenTimestamps proof (../../EXP-CZ-017-freeze.txt.ots) shows when the freeze root existed. Check it with the standard OpenTimestamps client (`ots verify`). EXP-CZ-017 was published after the runs; its commitment is externally anchored no later than Bitcoin block 973187 (2026-10-26T04:42:29Z). See the commitment page.

## Run ledgers

Release asset of this repository, tag exp-cz-017-reveal:

| Asset | SHA-256 |
|---|---|
| EXP-CZ-017-sealed-run-ledgers.tar.gz (result JSON and ledger JSONL for all 22 sealed set 3 runs, plus a SHA256SUMS file) | ba6930c6be4b6f36c423756153b82b30fee87ee1169e966a3a2c157104540642 |

The 22 runs are the 13 planned runs and the 9 exploratory runs of the untrained founders. Each ledger is hash-chained, and its last hash is the ledger root listed in RESULTS.md. Each ledger records a verdict for every task, so the solve counts in RESULTS.md can be recomputed from the ledgers. Each result file carries the sealed task file hash it ran against.

## What the reveal does not let you do

- Regenerate the tasks from the salt: that needs the task generator, which is not published.
- Recompute the verdicts from the answers: the runner and checker source is not public, so recomputation relies on the per-task verdicts recorded in the ledgers.
- Audit the withheld `models` and `task_spec` fields (see above).
