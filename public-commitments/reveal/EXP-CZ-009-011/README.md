# EXP-CZ-009, EXP-CZ-010 and EXP-CZ-011 reveal (sealed set 2)

Status: REVEALED 2026-10-26, after all three experiments were run and reported. Sealed set 2 is now retired: it will never be used for a sealed claim again.

The reveal is complete for EXP-CZ-009 and partial for EXP-CZ-010 and EXP-CZ-011; see "Partial manifest reveal" below.

## Files

At the top of this folder, shared by the three experiments:

| File | What it is |
|---|---|
| sealed1200-s2.jsonl | The 1,200 tasks of sealed set 2 with their reference answers |
| sealed_salt.hex | The 32-byte secret that generated them, as 64 hex characters |

In EXP-CZ-009/:

| File | What it is |
|---|---|
| manifest.json | The full frozen design |
| manifest_salt.hex | The 32-byte secret behind the per-field commitment, as 64 hex characters |
| manifest_reveal.json | Every field with its field salt and leaf, for checking one field at a time |
| freeze.jsonl | The one-event freeze ledger |

In EXP-CZ-010/ and EXP-CZ-011/:

| File | What it is |
|---|---|
| manifest_salt.hex | The 32-byte secret behind the per-field commitment, as 64 hex characters |
| manifest_reveal.json | Ten of the twelve fields with their field salts, plus the committed leaves of the two withheld fields |
| freeze.jsonl | The one-event freeze ledger |

No weights, adapters or model files are published.

## Partial manifest reveal (EXP-CZ-010 and EXP-CZ-011)

Two manifest fields, `models` and `task_spec`, are withheld and published only as their committed leaves, because they contain local file paths, which our publication policy does not allow. Their manifest.json files are therefore not published. This has consequences:

- The verifier rebuilds the per-field commitment root from the ten revealed fields and the two withheld leaves, so it shows that the revealed fields are the committed ones.
- It cannot check the manifest file hash or the canonical manifest digest, and prints SKIP for them.
- The model file hashes and the artifact bindings inside `task_spec` (runner, analysis program, training data and served adapter hashes) cannot be audited publicly. The served adapter hashes also appear in the revealed `arms` field.

The full manifests may be published later if the owner grants an exception to the policy.

## Verify in one command

From the public-commitments folder: `python3 verify_reveal.py reveal/EXP-CZ-009-011`

It needs only Python 3. For each experiment it checks, against the values on the commitment pages (../../EXP-CZ-009.md, EXP-CZ-010.md, EXP-CZ-011.md): the sealed task file hash, the sealed salt commitment, the manifest salt commitment, the commitment root rebuilt field by field, and the freeze ledger (every event hash, its root, and the commitments its freeze event records). For EXP-CZ-009 it also checks the manifest file hash and the canonical manifest digest. Each line prints PASS, FAIL or SKIP.

The OpenTimestamps proofs (../../EXP-CZ-0xx-freeze.txt.ots) show when the freeze roots existed. Check them with the standard OpenTimestamps client (`ots verify`). EXP-CZ-010 and EXP-CZ-011 were published after the runs; their commitments are externally anchored no later than Bitcoin block 973187 (2026-10-26T04:42:29Z). See their commitment pages.

## Run ledgers

Release asset of this repository, tag exp-cz-009-011-reveal:

| Asset | SHA-256 |
|---|---|
| EXP-CZ-009-011-sealed-run-ledgers.tar.gz (result JSON and ledger JSONL for all 33 sealed set 2 runs, plus a SHA256SUMS file) | 9a83349e666f62b7d7b66031126da2b86a027ce327edd44cc82ed13ae0d150c5 |

The 33 runs are the 9 EXP-CZ-009 runs, the 8 untrained control reruns, the 8 self-taught runs and the 8 teacher-taught runs. Each ledger is hash-chained, and its last hash is the ledger root listed in the experiment's RESULTS.md. Each ledger records a verdict for every task, so the solve counts in the RESULTS pages can be recomputed from the ledgers. Each result file carries the sealed task file hash it ran against.

## What the reveal does not let you do

- Regenerate the tasks from the salt: that needs the task generator, which is not published.
- Recompute the verdicts from the answers: the runner and checker source is not public, so recomputation relies on the per-task verdicts recorded in the ledgers.
- Audit the withheld `models` and `task_spec` fields of EXP-CZ-010 and EXP-CZ-011 (see above).
