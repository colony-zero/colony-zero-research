# EXP-CZ-011 results: outside teacher

Status: REPORTED 2026-10-26. Frozen 2026-10-26T04:30:59Z together with EXP-CZ-010 (root 5a7eed65..., ../../public-commitments/EXP-CZ-011.md). Sealed run of the teacher-taught adapters 2026-10-26T06:10:23Z to 06:46:01Z on one 16 GB consumer GPU, with EXP-CZ-010's frozen runner binary (4e9d101a...), in the same driver run as EXP-CZ-010 and after its control and self-taught arm. Analysis by the frozen paired-analysis program (955bb78a...) with the frozen analysis plan. Sealed set 2: 1,200 tasks, SHA-256 578bc7a8.... Read the commitment-timing incident below before relying on the timestamps.

## Outcome

Training each member on checked answers from an outside teacher (DeepSeek V4.1 Flash 1017, FP8, thinking off) raised its sealed solve count for all 8 members tested, so H11.1 is SUPPORTED (8 of 8 against a bar of 5; Holm over 9 with Graham at p = 1).

H11.3 is SUPPORTED: no member's format validity fell; every member has fewer malformed answers than untrained.

H11.2 predicted no direction. The teacher-taught adapter beats the self-taught adapter from EXP-CZ-010 for 7 of 8 members after Holm, and the self-taught adapter beats the teacher-taught one for none. For Quentin no Holm-significant difference was detected (765 against 771 solved, 279 against 285 discordant tasks, p = 0.83). So the preregistered count is 7 teacher-significant, 0 self-significant, 1 inconclusive. Seven of the 8 teacher-taught members pass R1, against four self-taught.

One caution governs the H11.2 reading. The teacher arm also trained on 1.4 to 4.1 times as many examples per member, so this experiment cannot separate "a better teacher" from "more checked examples".

## Hypotheses

| Hypothesis | Verdict | Evidence |
|---|---|---|
| H11.1 for at least five of the nine members, the outside-taught member solves more sealed tasks than the untrained member (exact McNemar, Holm over nine, alpha 0.05) | SUPPORTED | 8 of 8 tested members gain, every Holm p below 1e-29. Graham not tested (parity gate), counted at p = 1. |
| H11.2 outside-taught versus self-taught, per member, two-sided, no direction predicted | Teacher significantly better for 7, self for 0, inconclusive for 1 (Quentin) | Holm over nine with Graham at p = 1. Largest teacher margins: Mina +28.7 points, Bastien +23.1, Sam +15.6. Smallest significant: Rowan +4.7 (Holm p = 0.017), Quinn +5.4 (Holm p = 6.3e-4). |
| H11.3 E2 of the outside-taught member does not fall more than 2 points below the untrained member for any member | SUPPORTED | No member has more malformed answers than untrained; the changes range from 3 to 925 fewer. |

## Standings (greedy, 1,200 sealed tasks of set 2, 95% Wilson intervals)

| Rank | Member | Untrained | Self-taught (EXP-CZ-010) | Teacher-taught | Teacher-taught solve rate | Format valid | Solves per million tokens | R1 | Against untrained: only teacher / only untrained, Holm p | Against self-taught: only teacher / only self, Holm p |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Quinn | 512 | 994 | 1,059 | 0.883 [0.863, 0.900] | 1.000 | 3,230 | pass | 563 / 16, 5.2e-143 | 177 / 112, 6.3e-4 |
| 2 | Quentin | 354 | 771 | 765 | 0.638 [0.610, 0.664] | 1.000 | 6,699 | pass | 422 / 11, 1.0e-108 | 279 / 285, 1.00 (raw 0.83) |
| 3 | Mina | 218 | 369 | 713 | 0.594 [0.566, 0.622] | 1.000 | 5,861 | pass | 497 / 2, 1.4e-144 | 352 / 8, 5.1e-92 |
| 4 | Grace | 281 | 587 | 702 | 0.585 [0.557, 0.613] | 1.000 | 5,389 | pass | 431 / 10, 1.5e-112 | 133 / 18, 5.1e-22 |
| 5 | Rowan | 154 | 565 | 621 | 0.518 [0.489, 0.546] | 1.000 | 5,821 | pass | 467 / 0, 3.7e-140 | 225 / 169, 0.017 |
| 6 | Erin | 237 | 375 | 518 | 0.432 [0.404, 0.460] | 0.738 | 730 | fail: format | 338 / 57, 3.2e-49 | 347 / 204, 5.9e-9 |
| 7 | Sam | 189 | 243 | 430 | 0.358 [0.332, 0.386] | 1.000 | 3,035 | pass | 353 / 112, 8.2e-30 | 305 / 118, 2.2e-19 |
| 8 | Bastien | 78 | 147 | 424 | 0.353 [0.327, 0.381] | 0.901 | 4,054 | pass | 404 / 58, 2.8e-64 | 365 / 88, 3.1e-40 |
| - | Graham | not run | not run | not run | - | - | - | - | 1 (untested) | 1 (untested) |

Guessing baseline: 0.125, upper Wilson bound 0.1449. "Untrained" is the same-binary rerun shared with EXP-CZ-010, which reproduces EXP-CZ-009 exactly for all 8 members. The secondary comparison against EXP-CZ-009's ledgers gives identical counts and p values.

R1 under the teacher arm: Bastien, Grace, Mina, Quentin, Quinn, Rowan and Sam pass; all seven failed it untrained. Erin fails on format (0.738), although her format still improves on her untrained run (0.687).

## Exploratory: where the two adapters differ

Not preregistered. Solved of 300 per family, self-taught / teacher-taught.

| Member | Arithmetic | Graph reachability | JSON extraction | List transforms |
|---|---|---|---|---|
| Quinn | 287 / 191 | 270 / 300 | 262 / 285 | 175 / 283 |
| Quentin | 293 / 74 | 150 / 300 | 230 / 213 | 98 / 178 |
| Mina | 0 / 59 | 150 / 300 | 173 / 203 | 46 / 151 |
| Grace | 9 / 53 | 291 / 300 | 184 / 178 | 103 / 171 |
| Rowan | 178 / 26 | 298 / 300 | 77 / 130 | 12 / 165 |
| Erin | 221 / 38 | 152 / 276 | 0 / 82 | 2 / 122 |
| Sam | 4 / 8 | 163 / 191 | 64 / 116 | 12 / 115 |
| Bastien | 92 / 11 | 55 / 272 | 0 / 74 | 0 / 67 |

1. The teacher arm wins graph reachability and list transforms for every member. Five teacher-taught members solve all 300 graph tasks.
2. The self-taught arm wins arithmetic clearly for Quentin (293 against 74), Quinn, Rowan, Erin and Bastien. Quentin's overall tie hides this: with the teacher he gains on graph and lists and loses about as much on arithmetic.
3. The teacher arm cures two problems the self-taught arm kept. Bastien's output drops from 570,241 tokens (self-taught) to 15,264, and his format validity rises to 0.901. Erin's JSON comes back (0 self-taught, 82 teacher-taught), but her answers still run long: 614,096 output tokens, about 512 per task against the 512-token cap.
4. These per-family patterns are descriptive only. Families were not part of any hypothesis and no test was run on them.

## Training and cost (reported, not tested)

| Member | Kept teacher examples | Kept self examples (EXP-CZ-010) | Ratio | Chosen epoch (dev 0 to 399, epoch 1 / epoch 2) | Serving | Parity, max top-10 difference |
|---|---|---|---|---|---|---|
| Quinn (few-shot template) | 3,083 | 2,128 | 1.4 | 2 (351 / 354) | adapter | 0.0039 |
| Quentin | 2,799 | 1,367 | 2.0 | 2 (243 / 246) | adapter | 0.0003 |
| Mina | 2,799 | 884 | 3.2 | 2 (218 / 228) | adapter | 0.0008 |
| Grace | 2,799 | 1,171 | 2.4 | 2 (221 / 235) | adapter | 0.0019 |
| Rowan | 2,799 | 1,017 | 2.8 | 2 (197 / 197, tie) | merged, Q8_0 | 0.0002 |
| Erin | 2,799 | 1,364 | 2.1 | 2 (124 / 159) | adapter | 0.0027 |
| Sam | 2,799 | 882 | 3.2 | 2 (117 / 125) | adapter | 0.0085 |
| Bastien | 2,799 | 689 | 4.1 | 2 (98 / 144) | adapter | 0.0070 |

The seven members on the format-line template draw their examples from the same teacher run, so they train on the same 2,799 checked answers, each tokenised for its own model. Quinn's come from the teacher run on his few-shot template. Adapter sizes equal the self-taught ones (same shapes; Rowan's merged file is 523,649,152 bytes). Generated tokens in the sealed run: 786,133 against a cap of 4.92 million; wall time 36 minutes.

Teacher requests, tokens and USD spent are endpoints in the preregistration, but the proxy ledger totals are not in the frozen sources, so they are not reported here. The proxy's hard stop was 15 USD. GPU minutes for training are likewise not recorded in the frozen sources.

## Deviations from the preregistration

All of these were decided and recorded before any adapter saw sealed set 2.

1. Teacher endpoint (amendment 1, before any teacher answer existed): the model developer's own endpoint was refused under the account's privacy setting, so the teacher is the same open weights served in FP8 by a provider that does not train on or retain data. Nothing was produced or spent on the first endpoint.
2. Teacher inputs (amendment 2): Quinn's template is few-shot, so the teacher also saw the 80 never-scored template examples (dev 400 to 479) inside his prompts. It never saw dev 0 to 399, test, or any sealed set.
3. Provider terms (amendment 3): a corrected reading of the provider's general competition clause, recorded as the basis for use until written confirmation is obtained.
4. Control: the same-binary untrained rerun is the primary control, as for EXP-CZ-010, with EXP-CZ-009's ledgers as a secondary reference. They agree exactly.
5. Graham is not counted. His teacher adapter, when loaded, produced only repeated "G" characters (0 of 400 on dev, NaN logits), and his parity check fails in both arms. He enters each Holm family of nine at p = 1.
6. Trainer changes during training: the step that turns teacher ledgers into training data skips one chat-settings comparison for remote teacher ledgers (the template must still match; teacher arm only); Quinn trains with smaller micro-batches, memory only, and is counted by owner decision before the freeze; the parity-check fix and its correction. The recipe is unchanged.
7. Rowan's teacher-taught adapter is merged and served as Q8_0, as in EXP-CZ-010.
8. Teacher sampling is not reproducible run to run (provider sampling). The kept answers are whatever the recorded teacher ledgers hold; their SHA-256 values are in the manifest.

## Incident: the commitment was published after the runs

This is a real protocol slip, shared with EXP-CZ-010 and EXP-CZ-017. Our method says each commitment is pushed to the public repository and timestamped before its sealed run. The freeze roots were frozen at 04:30:59Z and submitted to OpenTimestamps at about 04:33Z. They were not pushed to the public repository before the runs, and the sealed set 2 driver started at 04:32:02Z, before the timestamp was submitted.

So the timing evidence is the Bitcoin attestation alone. All three roots (../../public-commitments/EXP-CZ-011-freeze.txt and its .ots proof) are anchored in Bitcoin block 973187, mined at 2026-10-26T04:42:29Z. Every teacher-taught run started after the anchor, the first at 06:10:23Z. The only runs that started before it were five untrained control runs shared with EXP-CZ-010, whose counts equal EXP-CZ-009's sealed results exactly.

Otherwise, all 8 teacher-arm runs ran once, in order, with no void run and no repeat.

## Run ledgers

The untrained control and self-taught ledgers are listed in ../EXP-CZ-010/RESULTS.md. All of them contain sealed set 2, so they are released with the joint reveal (../../public-commitments/reveal/EXP-CZ-009-011/README.md).

| Run | Solved | Malformed | Tokens out | Ledger root | Result file SHA-256 |
|---|---|---|---|---|---|
| Sam teacher-taught | 430 | 0 | 18,122 | 59f2594fd736fa3be58a8f905baa7615e2d02a3416eaef88a5bce35fe363c6cb | fc6f5daf4718579c19792b7620bc6fce0478f1228e417a2578909a8049dbb7ca |
| Grace teacher-taught | 702 | 0 | 14,231 | 387cb83f79be785be9adee2c0a335c7c5a9684c8a6bfd6f5114f6e57abf01dda | bdfc3830a710d2e25b38a869f4098ebc26e336b5d518f40d2e89fac290d8abb8 |
| Quentin teacher-taught | 765 | 0 | 16,535 | 282dc37818e30977b5248bf55d1fecb4ac43e2268cd728e551c5272cbdbb152d | c0437cc4e381c5b537f4430bb9ea43494edafea78043d8ea6056a34e08fb066f |
| Quinn teacher-taught | 1,059 | 0 | 72,961 | db2693a76df8d40264e65c6c9db3512af525a3aa8aeefceb8c8fdeb8eae7da09 | 41c95300df66bfffaba75ee9fa67a65e53c82e3cfc6331a1e6756ca57e9054cf |
| Rowan teacher-taught | 621 | 0 | 16,102 | c0998a2abcf74f0561c7d10f6eb23b8f3f92e9e0857871963ae4debba7431ddd | 6b53ba19da74bdebf71fd66a28d3d2b2840c03a872e147e0cf9fae8903f9ab12 |
| Erin teacher-taught | 518 | 315 | 614,096 | f4e4be42ee81a38bffb0ca70f0c5ce070ca8fb817fd7dbc571583351f0354355 | bca78768343913511c8958a78836a95153cffaaf75bef223a571cff11c8be5a3 |
| Bastien teacher-taught | 424 | 119 | 15,264 | 6cc6f3bf7efaa2e62ab478d89cb28fb4211190a247283dfae5be9701ac5033dd | 89fa4c6c5682e63f2b96019871b9192b9da287e57ac96738a4b5af3116184f63 |
| Mina teacher-taught | 713 | 0 | 18,822 | 1232f877767ad86faddc123d3d98ac1bb4e80c47e3ac462144be12d1c774a3d4 | 1a12fb8c8e23dc3ae4264efb29cb2adc48a576c5de54a5b90b7ff52918197f6e |

## What this does not show

- That the teacher is better than self-training as such. The teacher arm had 1.4 to 4.1 times as many training examples, and its examples cover the tasks the teacher could answer rather than the tasks each member could answer. Teacher quality, data volume and data coverage are confounded here.
- Generalisation. Sealed tasks come from the same generator families and difficulty levels as the training tasks; these are in-distribution gains on four synthetic families.
- Robustness across test sets. One sealed set (set 2), 1,200 tasks.
- Behaviour under other decoding. Greedy, 512-token cap.
- Anything about larger students. All members are small, about 340M to 800M parameters.
- Other teachers, more samples, or the teacher's reasoning traces. One teacher, thinking off, 4 samples per task.
- Other quantisations. Every comparison uses Q8_0 base files (merged Q8_0 for Rowan).
- Training-seed variance (seed 0 only), Graham, or behaviour inside a colony.

## Next

On these task families, checked teacher answers lifted every tested member and left format intact, and seven members now clear R1. The teacher-versus-self difference is real in this design but cannot be credited to the teacher alone, because the teacher arm had more data. EXP-CZ-017 tests the teacher question with equal data, by giving teacher-trained children and a solver-label control exactly the same task ids. A follow-up for the founders would equalise the example count between arms. Open items: teacher spend and GPU-minute accounting, and the joint reveal of sealed set 2.
