# Public commitments

A commitment is a published fingerprint of something we keep secret for now. It lets us fix a design or a test set before a run and prove later that we did not change it.

The fingerprint is a SHA-256 hash. Anyone can hash the same bytes and compare. If even one bit differs, the hash differs, so a match shows the revealed bytes are exactly the committed bytes.

## Verify a commitment

1. Get the revealed bytes. This is a file or a string that we publish after the run.
2. Compute its SHA-256 hash. For a file on a Unix shell: `sha256sum <file>`.
3. Compare the result with the value in the commitment page. They must match exactly, in all 64 hexadecimal characters.
4. If they differ, the commitment is broken. Treat the experiment as invalid.

## Order of events

1. Before a run: we publish the commitments.
2. During the run: nothing is revealed.
3. After the run: we reveal the bytes. You verify them as above.

A commitment published after the run it covers is worth nothing. Commit dates alone are not timing evidence, because whoever makes a commit can set its date. So before any sealed run, each commitment is pushed to this public repository and its hash is timestamped with OpenTimestamps, which anchors the hash in the Bitcoin blockchain. The proof file is published beside the commitment, and anyone can check it with the standard OpenTimestamps tools.

One exception so far. The commitments for EXP-CZ-010, EXP-CZ-011 and EXP-CZ-017 were timestamped but not pushed here before their sealed runs, and the first runs began before the timestamp request. Their only timing evidence is the Bitcoin anchor, block 973187 (2026-10-26T04:42:29Z). Every trained model's run started after that block. Each of those pages says which runs started before it.

## Verify a reveal in one command

`python3 verify_reveal.py reveal/<folder>` checks a reveal against the values published here. It needs only Python 3. `python3 verify_reveal.py --self-test` builds fake reveals from random salts and checks that they pass and that tampering fails.

## Pages

- EXP-CZ-001.md (revealed: reveal/EXP-CZ-001/)
- EXP-CZ-009.md (second casting; reveal with EXP-CZ-010 and EXP-CZ-011 in reveal/EXP-CZ-009-011/)
- EXP-CZ-010.md (self-taught adapters)
- EXP-CZ-011.md (teacher-taught adapters)
- EXP-CZ-017.md (first children; reveal in reveal/EXP-CZ-017/)
