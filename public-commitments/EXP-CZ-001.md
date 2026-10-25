# EXP-CZ-001 commitments

Status: REVEALED 2026-10-25; every value below verifies (reveal/EXP-CZ-001/README.md). Frozen 2026-10-24T23:45:20Z. The freeze record is EXP-CZ-001-freeze.txt in this folder, and EXP-CZ-001-freeze.txt.ots is its OpenTimestamps proof.

| Commitment | What it covers | Value |
|---|---|---|
| Salt commitment | The secret salt that generates the sealed tasks | 944c6a61135558626cf27bc7897b3ced84bd8f71920bf8304dfbfd10587ebe4b |
| Sealed task file | SHA-256 of the sealed task file: task suite 0.0.2, 1,200 tasks, 300 per family | 0a60bd438ddabbea9e2cc92d640b6b0437ffac7f7db8bddf34881003d0cd8388 |
| Freeze commitment root | Per-field salted commitment to the full design (12 fields) | c95f852c4967ede66f40f29bdfff8d3666127c940efef2fbe858e3b222d52ef9 |
| Manifest digest | SHA-256 of the canonical JSON design | 58e9b7bd900eb86d80c5e520caff28c69a3c7e5ab9db02bd6c065ef02e976fe5 |
| Manifest salt commitment | SHA-256 of ASCII `cz-manifest-salt-commit-v1\|` plus the 32 raw manifest-salt bytes | e95cdac1cc593d6c98df55e7d39bbbe00c92d003cc7f28b5f97c483be929eb51 |
| Freeze ledger root | Root of the one-event hash-chained freeze ledger | c59b3e3ca3468feb0097fde5117642d796a735cae37149502b50a4f886afacdf |

The committed design binds, by SHA-256, the run and analysis binaries, the run driver, the full specification and the Laya predictions. After the run, the manifest and selected field salts are revealed so each field can be checked against the root.

How to verify: see README.md in this folder. When the sealed run is done, we reveal the task file and the salt. The task file must hash to the sealed task file value above. The salt commitment is SHA-256 of the ASCII bytes `cz-salt-commit-v1|` followed by the 32 raw salt bytes, so the revealed salt must reproduce the value above.
