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

One exception so far. EXP-CZ-010, EXP-CZ-011 and EXP-CZ-017 were published after the runs; externally anchored no later than Bitcoin block 973187 (2026-10-26T04:42:29Z). They were not pushed here before their sealed runs, and the first control runs began before the timestamp request. Their freeze time, 04:30:59Z, is our own record and is not independently established. Every adapter and child run began after the anchor; five untrained control runs began before it. Each of those pages gives the details.

## Timing evidence, as it stands

A Bitcoin anchor proves a hash existed no later than the time of its block. It does not prove when the hash was submitted, and anchors usually land minutes to hours after submission. For EXP-CZ-001 and EXP-CZ-009 the anchors landed after the sealed runs began. So the evidence that each commitment came before its run is GitHub's own server-side push time. That record is held by one company, so it is weaker than a Bitcoin anchor. GitHub keeps these events for about 90 days, so a copy is saved in github-push-events-2026-10-26.json.

| Experiment | Public push (GitHub server time) | First sealed run started | Bitcoin anchor |
|---|---|---|---|
| EXP-CZ-001 | 2026-10-24T23:47:08Z (commit aa65ad0) | 2026-10-24T23:47:24Z | block 972993, 2026-10-24T23:56:01Z |
| EXP-CZ-009 | 2026-10-25T03:37:28Z (push of 3b40fa1, which contains the freeze commit 1021c5d) | 2026-10-25T03:37:41Z | block 973012, 2026-10-25T03:58:36Z |
| EXP-CZ-010, 011, 017 | 2026-10-26, after the runs | 2026-10-26T04:32:02Z (first adapter run 05:08:02Z) | block 973187, 2026-10-26T04:42:29Z |
| EXP-CZ-003a | 2026-10-28T02:54:10Z (push of a6ea353) | 2026-10-28T04:20:02Z | block 973489, 2026-10-28T03:10:30Z |

From now on a sealed run starts only after its commitment is pushed here and its Bitcoin anchor is confirmed.

## Verify a reveal in one command

`python3 verify_reveal.py reveal/<folder>` checks a reveal against the values published here. It needs only Python 3. `python3 verify_reveal.py --self-test` builds fake reveals from random salts and checks that they pass and that tampering fails.

## Pages

- EXP-CZ-001.md (revealed: reveal/EXP-CZ-001/)
- EXP-CZ-009.md (second casting; revealed with EXP-CZ-010 and EXP-CZ-011: reveal/EXP-CZ-009-011/)
- EXP-CZ-010.md (self-taught adapters; partial manifest reveal)
- EXP-CZ-011.md (teacher-taught adapters; partial manifest reveal)
- EXP-CZ-017.md (first children; revealed, partial manifest reveal: reveal/EXP-CZ-017/)
- EXP-CZ-003a.md (routing across the colony; reported and revealed: [reveal/EXP-CZ-003a/](reveal/EXP-CZ-003a/))
