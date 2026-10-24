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

## Pages

- EXP-CZ-001.md
