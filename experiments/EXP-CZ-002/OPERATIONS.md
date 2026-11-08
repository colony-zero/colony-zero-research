# EXP-CZ-002 Operations and Deviations

This file records operational facts that are not fully covered by amendments A1 through A6 in `REPORT.md`. It does not reveal a salt value, a salt or sealed-file location, task content, or a per-task outcome.

## 1. Transport, checkout, and Git ownership adaptations

- Plan: The original command blocks assumed direct host-to-host Git and timestamp traffic, host-side tests, normal repository ownership, and a healthy recurring service.
- Done: Transfers were relayed through the code-server checkout and checked by SHA-256 at both ends. Git used `safe.directory` entries for both host checkouts. Timestamp checks ran from code-server or through a local-hop SSH shim. Tests ran from code-server when the generation host lacked pytest. Failed recurring-service state was reset before checkout changes. A stale public scaffold was replaced with the real public checkout. The timestamp image was used on the scoring host because it was not present on the generation host. Commit identity was supplied with `git -c` where repository configuration was unsuitable. One root-owned private directory and later Git indexes were returned to the normal checkout owner after failed or host-side Git operations.
- When: 2026-11-02 through 2026-11-07 UTC.
- Why: The live hosts did not match the transport, tool, ownership, and service assumptions in the first plan blocks.
- Decision: Claude+Codex consensus approved the adapted transport. The log does not identify a separate decision maker for each ownership repair.
- Effect on results: None. These changes moved and authenticated bytes. They did not change tasks, ledgers, scoring, thresholds, or outcomes.
- Evidence: private commits `2344cde`, `0508c24`, `6a4af6e`, and `9df0c46`; public commits `3b1f2ea`, `202e0d0`, and `d4a893c`; digest-map SHA-256 prefix `0b86a5d6`; canonical kit SHA-256 prefix `c4b63622`.

## 2. Fixed-path timestamp supersession

- Plan: Stamp the fixed commitment proof path.
- Done: Existing proof bytes were archived byte for byte. The old proof file was removed immediately before `ots stamp` because the timestamp tool creates the proof exclusively and will not overwrite it. The fixed public path was then repopulated with the new proof.
- When: 2026-11-03 UTC.
- Why: The plan reused a fixed path, but the timestamp command refuses an existing proof file.
- Decision: Claude+Codex consensus.
- Effect on results: None. This occurred before the applicable sealed generation and preserved the superseded evidence.
- Evidence: superseded public commit `db58673`; old proof SHA-256 prefix `40fca08e`; replacement commitment SHA-256 prefix `f772f310`; replacement proof SHA-256 prefix `c3201a87`; Bitcoin block `974395`; public commit `202e0d0`.

## 3. Revision 002 PREGEN index check

- Plan: `verify-private-index --phase PREGEN` had to pass before the PREGEN commit.
- Done: The check exited 2 because `KIT_MANIFEST.json` was byte-identical to the prior revision and therefore was not staged. An inline shell failure did not stop the commit. Independent checks then proved that the committed change set was an allowed subset, the record and manifest bytes matched the worktree, the manifest was canonical, the record validated, and the parent was correct. The commit was kept without amendment. The allowlist logic was repaired before the next PREGEN revision.
- When: 2026-11-03 UTC.
- Why: The verifier required exact staged-path equality when a byte-identical file did not need staging.
- Decision: Claude+Codex consensus, verdict A.
- Effect on results: None. No sealed score existed. The committed tree passed the equivalent binding checks before generation continued.
- Evidence: private commit `0508c24521a68ac595e20c7b60c867d62d4a848d`; parent `c72c148`; record SHA-256 prefix `9f9cfeb7`; canonical manifest SHA-256 prefix `c4b63622`.

## 4. Attempt 001 recovery rule and pre-generation rule change

- Plan: Any interrupted generation was to be voided, and the original interpretation expected zero preparation exclusions from 2,400 candidates.
- Done: Consensus required authentication of any existing canonical summary, preparation record, overlap audit, inventory, output bytes, and the mode of the salt file after an interruption. Valid canonical output could be kept. Missing, noncanonical, changed, or integrity-failed output had to be voided. Before attempt 001 created any salt or output, rehearsal showed that zero exclusions was infeasible. Consensus approved deterministic candidate headroom and first-survivor selection while preserving the final 2,400-task balance and all endpoints.
- When: 2026-11-03 UTC.
- Why: The original recovery rule could discard authenticated output, and the zero-exclusion interpretation failed rehearsal before generation.
- Decision: Claude+Codex consensus.
- Effect on results: None at the time of the decision. No score existed. The final domain size, balance, endpoints, and thresholds were unchanged.
- Evidence: generation-gate receipt SHA-256 prefix `d2e2a7e9`; attempt 001 summary SHA-256 prefix `5f71501a`; scored-file SHA-256 prefix `fe4855c9`; audit receipt SHA-256 prefix `c531ee57`; PRERUN private commit `8f31c99`; Bitcoin block `974412`.

## 5. Exact-match local-hop SSH shim

- Plan: Timestamp verification on the scoring host was to hop through the generation host using normal SSH.
- Done: An exact-match local-hop shim was installed for the seven approved timestamp-check command strings. Near variants failed closed. Other destinations passed through to the system SSH client. The same shim pattern was recreated only in host blocks that needed it.
- When: 2026-11-03 UTC, with later reuse through 2026-11-07 UTC.
- Why: The available key was restricted to a forced command and could not perform the planned hop. A service drop-in was rejected because the sealed service required no drop-ins.
- Decision: Claude+Codex consensus.
- Effect on results: None. The shim only transported timestamp verification commands. Explorer connection flakes failed closed and passed on retry.
- Evidence: shim SHA-256 `30be694fac3a7607f0e69cdded6d64840ef3aa8a2e67348a96678bbec30d4e81`; verified PREGEN blocks `974395` and `974412`.

## 6. Revision 002 label failure and revision 003 recovery

- Plan: Start the sealed queue with generated labels containing the word `sealed`.
- Done: The frozen probes rejected those labels before task access or model execution. All pending jobs were cancelled. Consensus required a full new freeze cycle, one centralized safe label format, generation-time validation, rehearsal of all command identities, revision-qualified queue IDs, stronger receipt binding, authenticated prior-attempt inventory, repaired index checks, and preserved evidence.
- When: 2026-11-03 UTC.
- Why: The generator and frozen parser enforced incompatible label rules.
- Decision: Claude+Codex consensus, verdict A.
- Effect on results: None. No task was accessed, no model ran, and no score existed. Attempt 001 remained preserved as consumed generation evidence.
- Evidence: r002 PRERUN private commit `8f31c99`; public commit `1883033`; Bitcoin block `974412`; revision 003 candidate commits `0beebdf` and `1658e77`.

## 7. Attempts 002 and 003, then revision 004

- Plan: Attempt 002 would use the same final-domain rule, and attempt 003 could proceed under the same provenance implementation if needed.
- Done: Attempt 002 was voided because one cell had fewer than 120 survivors. Consensus opened attempt 003 with unchanged parameters. Attempt 003 then stopped before inventory, salt creation, or output because provenance was hard-coded to attempt 002. Consensus opened revision 004, generalized the provenance rule, increased candidate headroom to 150 per cell, created a new PREGEN commitment, and kept the final 120 per cell unchanged.
- When: 2026-11-03 UTC.
- Why: The first recovery followed the frozen shortfall rule. The second fixed an attempt-number restriction and used rehearsal-backed headroom.
- Decision: Claude+Codex consensus.
- Effect on results: None. Attempt 002 was void and absent. Attempt 003 had created no inventory, salt, or output at the point of the provenance failure. No score existed.
- Evidence: superseded PREGEN private commit `6a4af6e`; superseded commitment SHA-256 prefix `35c33ad6`; Bitcoin block `974431`; revision 004 candidate `e0569612`; revision 004 PREGEN `82060d3`; Bitcoin block `974448`; successful attempt 003 summary SHA-256 prefix `fa5002d1`.

## 8. Revision 004 infrastructure stop and fresh revision 005

- Plan: A valid completed team result had to be accepted by the driver and POSTRUN validator, and the 60,000,000-token and 45-hour caps covered the sealed run.
- Done: The driver rejected a valid one-sample team result because the optional `samples` field was absent. Evidence was preserved and the run was classified as infrastructure, not a scientific result. Consensus required a tested fix, a full dress rehearsal, a fresh sealed attempt, new commitments, and a rerun of every tuple. The owner approved revision 005 with fresh 60,000,000-token and 45-hour caps and required cumulative resource disclosure.
- When: 2026-11-04 UTC.
- Why: The frozen driver and POSTRUN validator disagreed with the frozen team result format.
- Decision: Claude+Codex consensus chose the recovery. The owner approved revision 005 and fresh caps.
- Effect on results: Revision 004 was never scored and is excluded from analysis. Its exact token use was 19,018,136. Revision 005 started from a fresh attempt.
- Evidence: revision 004 private PRERUN commit `1df185b`; public commit `1be55f6`; Bitcoin block `974459`; revision 005 candidate `e2e1613`; revision 005 PREGEN `b49b3ed`.

## 9. Revision 005 manifest removal and gate-request source

- Plan: Step 2 said `SEALED_MANIFEST.json` and `SEALED_JOB_MANIFEST.json` would remain absent. The generation-gate transfer block expected the request under the gate output directory.
- Done: Both manifests were tracked in the revision 005 base, so they were removed with `git rm` before the PREGEN index check. They remained preserved in the earlier private commit and the prior-attempt bundle. The request was copied from the queue job directory, where the gate writer actually placed it. Its exact SHA-256 remained bound by the gate receipt.
- When: 2026-11-04 UTC.
- Why: The plan prose was stale about the inherited PRERUN files and wrong about the gate writer's output directory.
- Decision: Claude+Codex consensus.
- Effect on results: None. The files were regenerated at PRERUN. The request bytes were unchanged and receipt-bound.
- Evidence: revision 005 PREGEN private commit `b49b3ed`; record SHA-256 prefix `60afd2f0`; prior private commit `1df185b`; commitment SHA-256 prefix `6ae90592`; Bitcoin block `974558`; public commit `d71dfcd`.

## 10. Revision 005 cap stop and revision 006 fresh cap

- Plan: Revision 005 had a 60,000,000-token cap. A budget stop was terminal and could not be raised in place.
- Done: Revision 005 stopped under `STOP_TOKEN_CAP` at 60,000,767 recorded prompt-plus-generated tokens and was never scored. The owner chose revision 006 with a fresh attempt, a measured 100,000,000-token cap, and the same 45-hour cap. Revision 006 completed at 76,299,045 tokens.
- When: 2026-11-05 through 2026-11-08 UTC.
- Why: The preregistration estimate understated repeated prompt tokens. This was a budget-estimate failure, not a code failure.
- Decision: Owner.
- Effect on results: Revision 005 outcomes were excluded and never scored. Revision 006 supplied the only scored result. Exact cumulative use across revisions 004, 005, and 006 was 155,317,948 tokens.
- Evidence: revision 005 start `2026-11-04T20:01:21Z`; revision 005 totals 46,217,149 prompt and 13,783,618 generated; revision 006 first task `2026-11-05T22:31:22Z`; revision 006 total 76,299,045; final report and runbook agree on cumulative 155,317,948.

## 11. Temporary gate-reviewer substitution

- Plan: Gates used Claude+Codex consensus.
- Done: When the Codex quota was unavailable, the owner authorized a fresh isolated Claude reviewer and the label `consensus:claude+claude-fresh`. The reviewer path was tested before use. When Codex returned, the gate reviewer and consensus label were restored before attempt 005.
- When: 2026-11-05 UTC.
- Why: The planned reviewer was temporarily unavailable.
- Decision: Owner.
- Effect on results: None. The temporary reviewer covered candidate review only. Attempt 005 returned to Claude+Codex review before generation.
- Evidence: revision 006 candidate commit `ce1b423`; the runbook records a fresh-review approval and a later `CODEX-OK` check. No receipt digest for the temporary liveness check is stated in the log.

## 12. Attempt 005 prose erratum and added path preflight

- Plan: Two `FREEZE_PLAN.md` references named attempt `004`, and the host block did not explicitly prove that the attempt 005 inventory, salt-file role, and output roles were absent before generation.
- Done: The executed block treated the attempt number as `005` and added the stricter absence preflight. The frozen PREGEN-to-PRERUN change boundary was not widened. The main plan still needs the prose erratum and preflight carried back after the run.
- When: 2026-11-05 UTC.
- Why: The scheduled reviewer found stale attempt prose and missing absence evidence.
- Decision: Claude+Codex consensus.
- Effect on results: None. The correction happened before salt creation and generation. It reduced the chance of reusing an attempt path.
- Evidence: `FREEZE_PLAN.md` lines identified in the runbook as 1599 and 1657; attempt 005 summary SHA-256 prefix `c4cb8ab9`; PRERUN private commit `9df0c46`; scored-file SHA-256 prefix `adbaf3a1`; Bitcoin blocks `974714` and `974715`.

## 13. Salt-file paths in gate packets

- Plan: Gate packets were not to contain a salt path, salt value, task content, or sealed path.
- Done: Gate packets for attempts 001 through 005 carried the path to the salt file. They did not carry a salt value or task content. No location is repeated in this disclosure. The owner ruled that a path alone was not a leak and approved attempt 005. The packet builder still needs a post-run fix that strips host, salt, sealed, and task paths and tests that rule.
- When: Discovered and ruled on 2026-11-05 UTC.
- Why: The packet builder copied plan context that contained the path.
- Decision: Owner ruling, followed by Claude+Codex agreement.
- Effect on results: None. The packets exposed no salt value and changed no task, ledger, score, or threshold.
- Evidence: attempt 005 audit-gate escalation and owner ruling in the runbook; attempt 005 summary SHA-256 prefix `c4cb8ab9`; PRERUN private commit `9df0c46`. The log gives no separate packet SHA-256 for all five attempts.

## 14. Funding file held aside through the sealed publication chain

- Plan: The public checkout had to stay clean and at the receipt-bound head through generation, POSTRUN, BEACON, and amendment publications.
- Done: An unrelated `funding.json` was moved aside after it caused the first attempt 005 host block to fail the clean-check guard. A staged inventory from that failed block was quarantined. The same attempt number was rerun because no salt or output had been created. The funding file remained aside through every EXP-CZ-002 publication receipt. It was restored and published alone only after the report completed and after the last experiment receipt.
- When: 2026-11-05 through 2026-11-08 UTC.
- Why: The untracked file made the public checkout dirty and could have invalidated head-bound receipts if published mid-run.
- Decision: Claude+Codex consensus chose the recovery. The owner separately approved publishing the funding file after the experiment receipts.
- Effect on results: None. The first block failed before salt or output creation. The later standalone funding commit did not enter any experiment receipt or score.
- Evidence: initial aside SHA-256 prefix `1cec35da`; final file SHA-256 prefix `61a1915e`; final standalone public commit `e722608`; remote match recorded in the runbook.

## 15. Bare checkout switch left the service on revision 005

- Plan: Stop the sealed service and timer, switch the checkout, then restart them so the daemon loads revision 006.
- Done: A bare `git switch` changed the worktree while the daemon retained revision 005 code. The daemon rejected revision 006 job IDs. With no sealed job running, the planned stop, switch, reset-failed, and restart sequence was then executed.
- When: 2026-11-05 UTC.
- Why: The preparation chain omitted the service-control part of the plan's checkout block.
- Decision: The recovery was performed immediately. A separate decision identity is unclear in the log.
- Effect on results: None. The old daemon rejected the new IDs before an accepted revision 006 run began.
- Evidence: revision 006 candidate `ce1b423`; PRERUN private commit `9df0c46`; public PRERUN anchor commit `d4a893c`; Bitcoin blocks `974714` and `974715`.

## 16. Quarantine inside the scanned runs root

- Plan: Preserve revision 004 and 005 evidence under `superseded/` and let POSTRUN scan the sealed runs root. The report would later authenticate the preserved run states.
- Done: The preserved `superseded/` tree was under the directory scanned by POSTRUN. POSTRUN failed twice on that unexpected inventory. Consensus cancelled the report, moved the entire preserved tree temporarily outside the scanned root, saved and checked its tree hash, retried POSTRUN and scoring, then restored it after scoring so the report could authenticate the earlier run states.
- When: 2026-11-06 through 2026-11-08 UTC.
- Why: The quarantine layout and POSTRUN's recursive inventory rule were incompatible. The rehearsal used a separate layout and did not expose the conflict.
- Decision: Claude+Codex consensus.
- Effect on results: None. No score existed at the two POSTRUN failures. The evidence bytes were hash-checked before and after the temporary move. Restoring them enabled the resource disclosures in the private report.
- Evidence: revision 006 completed with 76,299,045 tokens before the failure; POSTRUN later published at public commit `fbc240b`; anchored POSTRUN public commit `f5e2443`; Bitcoin blocks `974919` through `974921`; final score completed under amendment commit `ac2e01b`.

## 17. POSTRUN proof precheck after the poller upgraded the proof

- Plan: The POSTRUN upgrade block first compared the local proof to the original pending proof before upgrading it.
- Done: The background poller had already upgraded the scoring-host copy. The stale equality precheck was dropped, and the upgraded proof was verified and published.
- When: 2026-11-07 UTC.
- Why: The precheck assumed the poller had not yet changed the proof.
- Decision: Unclear in the log.
- Effect on results: None. The proof was already upgraded, and the normal timestamp verification and remote-head checks still passed before scoring release.
- Evidence: POSTRUN SHA-256 prefix `ffe20dc0`; pending proof SHA-256 prefix `e2d13fa1`; anchored public commit `f5e2443`; Bitcoin blocks `974919` through `974921`.

## 18. BEACON local-hop shim

- Plan: The BEACON host block called the timestamp checker without recreating the local-hop shim.
- Done: The first BEACON block failed on the unavailable SSH hop. The same exact-match shim used by the proven POSTRUN block was added, and the block was rerun successfully.
- When: 2026-11-07 UTC.
- Why: The BEACON block omitted the required transport adaptation.
- Decision: Unclear in the log. The shim itself had prior Claude+Codex approval.
- Effect on results: None. The first block failed before the release receipt and before scoring. The successful rerun created the beacon and released scoring.
- Evidence: public BEACON commit `e70efc2`; POSTRUN anchor commit `f5e2443`; shim SHA-256 `30be694fac3a7607f0e69cdded6d64840ef3aa8a2e67348a96678bbec30d4e81`.

## 19. Amendment publication transport

- Plan: The A2 host block used `git push origin main` from the host public checkout.
- Done: The host push was replaced by the existing publication tool from code-server, followed by an independent remote-head match check. The same publication pattern was carried into later amendment blocks.
- When: 2026-11-07 UTC.
- Why: The public checkout publication path was already defined around the publication tool and remote verification. Direct host Git publication did not match the live credential and transport boundary.
- Decision: The runbook records this as an operational deviation. A separate consensus result is not stated for the A2 substitution.
- Effect on results: None. The published bytes were unchanged, and the remote match was checked before the receipt and scoring retry.
- Evidence: A2 public commit `8c02e90`; A2 anchor commit `d49ef28`; A2 commitment SHA-256 prefix `2af4a2f0`; Bitcoin block `974935`.

## 20. Amendments A2 through A6 after the public beacon

- Plan: The release verifier originally required the BEACON receipt's public head to remain the current public head, which implied no later public commits before scoring.
- Done: A2 through A6 were committed and published after public BEACON commit `e70efc2`. Each was a hash-only authenticated amendment and was Bitcoin-anchored before the successful score. Claude+Codex consensus ruled that the beacon fixed the release time, that the scorer did not consume the beacon, and that authenticated later amendments did not invalidate the result. A3 changed the release verifier to authenticate this chain.
- When: 2026-11-07 UTC.
- Why: Pre-score authentication and scorer defects were found only after the beacon release. No score existed at any of those failures.
- Decision: Claude+Codex consensus for the post-beacon chain. The owner separately approved the A5 scorer replacement.
- Effect on results: No score existed before A6. A2, A3, A4, and A6 changed authentication or output staging. A5 changed one scorer acceptance rule but not scoring math, thresholds, task bytes, or ledger bytes. The successful score was attempt 7.
- Evidence: BEACON public commit `e70efc2`; A2 commitment prefix `2af4a2f0`, block `974935`; A3 prefix `a4c64f2e`, blocks `974953` and `974956`; A4 prefix `990513c0`, blocks `974970` and `974974`; A5 prefix `a85f534d`, block `975002`; A6 prefix `675c00a3`, block `975020`; final amendment commit `ac2e01b`.

## 21. A5 anchor wait without a local Bitcoin node

- Plan: The A5 anchor wait used `ots verify` on the scoring host.
- Done: The wait used the upgraded proof plus `ots info` to detect a `BitcoinBlockHeaderAttestation`. The normal two-explorer `ots_check` remained unchanged and was required before the receipt and cutover.
- When: 2026-11-07 UTC.
- Why: `ots verify` always returned failure on that host because it had no Bitcoin node.
- Decision: Claude+Codex consensus. The A6 anchor wait used the same condition.
- Effect on results: None. The replacement changed only the wait condition. Independent explorer verification still passed before scoring.
- Evidence: A5 commitment SHA-256 `a85f534de2763a2bbe3a61a90cfb80adc78ebbefef12d8ac811c13e175df4e70`; anchor public commit `12d6299`; Bitcoin block `975002`; replacement scorer SHA-256 prefix `623cda67`.

## 22. Reading notes for the report

These are not deviations. They explain figures in `REPORT.md` that are easy to misread. The frozen report and scorer output are unchanged.

- The prose prints the H2.1 exact McNemar p-value as `0.000000`. That is rounding. The scorer value is 1.86e-14 (375 tasks solved only by T3, 193 only by U_tool at 4x).
- U(B) and U_tool(B) are non-realizable references (DRAFT_SPEC.md, arm table). Their `realizable_accuracy` values in the JSON block are not meaningful and should not be cited. For these two arms the frozen scorer computes coverage with the union budget rule over all tasks, but computes `realizable_accuracy` with the per-candidate rule and divides by the tasks reached within the cut. This is why U 1x and 2x and U_tool 1x and 2x show accuracy above coverage.
- For every arm, `realizable_accuracy` is divided by the tasks that have at least one candidate within the cut, not always by all 2,400 tasks. At the 1x and 2x cuts it can therefore use a smaller denominator than coverage.
- None of this touches a confirmatory endpoint. H2.1 compares T3 and U_tool coverage at 4x on all 2,400 tasks. Every reported status agrees with its p-value and Holm threshold.
