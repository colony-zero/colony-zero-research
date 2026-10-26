# EXP-CZ-017 results: First Birth

Status: REPORTED and REVEALED 2026-10-26. Sealed set 3 and its salt are revealed and the set is retired; the manifest reveal is partial (../../public-commitments/reveal/EXP-CZ-017/README.md). Timing: published after the runs; externally anchored no later than Bitcoin block 973187 (2026-10-26T04:42:29Z); the 04:30:59Z freeze time is our own record. Every EXP-CZ-017 run began after the anchor. Frozen 2026-10-26T04:30:59Z, before any child saw sealed set 3 (root 55a51dd3..., ../../public-commitments/EXP-CZ-017.md). Sealed run on one 16 GB consumer GPU with a frozen runner binary (e058fb4e...): the 13 planned runs 2026-10-26T06:46:24Z to 07:44:36Z, then the nine untrained founders as exploratory comparators, 07:44:39Z to 09:27:49Z. Analysis by the frozen paired-analysis program (955bb78a...) with the frozen analysis plan. Sealed set 3, scored file: 2,393 tasks, SHA-256 7531dc11... (7 chance-collision tasks excluded before any run). See also the commitment-timing incident below.

Read first. Each arm was trained with three seeds, and seed 0 alone decides every hypothesis and admission; seeds 1 and 2 are replications. Our methodology asks for at least five seeds for anything that learns, so this is a departure from that rule: seed variance is only partly known, and the learning results are preliminary on that axis. All results are within four synthetic Forge task families, tested on fresh tasks from the same generators as the training tasks.

The frozen analysis plan (analysis_plan.json) and the analysis output (analysis/results.json) are not published: both contain local file paths in a notes field, which our publication policy does not allow. The tests themselves are standard (exact McNemar, Holm, Wilson intervals) and can be recomputed from the per-task verdicts in the ledgers, but the frozen plan that maps runs to tests cannot be checked from this repository.

## Outcome

Both children beat their parent by a wide margin, so H17.1 and H17.2 are SUPPORTED. Theo (taught by DeepSeek V4.1 Flash 1017) solves 37.0% of sealed set 3 and Hazel (taught by MiMo V2.6 Flash) 37.4%, against 12.6% for the untrained SmolLM2-135M parent: +24.4 and +24.8 points. Seeds 1 and 2 agree in sign with seed 0 for both.

H17.3 is NOT SUPPORTED: no Holm-significant difference between Theo and Hazel was detected (40 against 49 discordant tasks, p = 0.40).

H17.4a and H17.4b are NOT SUPPORTED. Neither child beats the solver-label control, which is the same parent trained on the same task ids with the generator's own correct answers (Theo +0.04 points, Hazel +0.42 points, both far from significant and below the 2-point minimum).

H17.5 fails for both children. The Q4_K_M files lose more than the allowed 2 points against Q8_0 (lower bounds -3.5 points for Hazel, -6.6 for Theo), so both children ship as Q8_0.

All nine trained Q8_0 runs (three seeds each of Theo, Hazel and the solver-label control, which is a control and not a member) pass R1, and the parent does not. Under the membership rule, the seed-0 Theo and Hazel are admitted to the colony.

The main reading: for this parent on these task families, no preregistered teacher advantage over correct solver labels on the same tasks was observed. These were superiority tests, not equivalence tests, so they do not show that teachers and solver labels are equal.

## Hypotheses (seed 0, Q8_0, Holm over the five tests)

| Hypothesis | Verdict | Evidence |
|---|---|---|
| H17.1 Theo solves at least 5 points more than the parent, significant | SUPPORTED | 885 against 301; only Theo 593, only parent 9; +24.4 points; Holm p = 1.7e-161. Robust: seeds 1 and 2 +24.0 and +24.2 points. |
| H17.2 Hazel solves at least 5 points more than the parent, significant | SUPPORTED | 894 against 301; only Hazel 609, only parent 16; +24.8 points; Holm p = 1.3e-156. Robust: seeds 1 and 2 +23.8 and +25.0 points. |
| H17.3 Theo and Hazel differ (two-sided) | NOT SUPPORTED | Only Theo 40, only Hazel 49; -0.4 points; p = 0.40, Holm p = 1. |
| H17.4a Theo solves at least 2 points more than the solver control, significant | NOT SUPPORTED | Only Theo 46, only solver 45; +0.04 points; p = 1, Holm p = 1. |
| H17.4b Hazel solves at least 2 points more than the solver control, significant | NOT SUPPORTED | Only Hazel 51, only solver 41; +0.42 points; p = 0.35, Holm p = 1. |
| H17.5 Q4_K_M loses no more than 2 points against Q8_0 (one-sided 95% Wald lower bound above -0.02) | NOT SUPPORTED for Theo or Hazel | Table below. Both children ship as Q8_0. |

## Standings (greedy, format-line template, 512 tokens, 2,393 sealed tasks of set 3, 95% Wilson intervals)

| Run | Solved | Solve rate | Format valid | Solves per million tokens | R1 |
|---|---|---|---|---|---|
| Hazel seed 0, Q8_0 | 894 | 0.374 [0.354, 0.393] | 1.000 | 3,097 | pass |
| Theo seed 0, Q8_0 | 885 | 0.370 [0.351, 0.389] | 1.000 | 3,124 | pass |
| Solver control seed 0, Q8_0 | 884 | 0.369 [0.350, 0.389] | 1.000 | 3,124 | pass (reported only) |
| Parent, SmolLM2-135M-Instruct, Q8_0 | 301 | 0.126 [0.113, 0.140] | 0.418 | 658 | fail: all three conditions |

All seeds and quantisations (solved of 2,393):

| Arm | Seed 0 Q8_0 | Seed 1 Q8_0 | Seed 2 Q8_0 | Seed 0 Q4_K_M |
|---|---|---|---|---|
| Theo | 885 | 876 | 879 | 749 |
| Hazel | 894 | 871 | 899 | 830 |
| Solver control | 884 | 854 | 864 | 755 |

Guessing baseline: 0.1254, upper Wilson bound 0.1393, read back from the 13 planned ledgers (the exploratory runs cannot move it). Every child run, at every seed and both quantisations, passes R1. The spread between seeds within one arm (up to 30 tasks, 1.3 points, for the solver control; 28 for Hazel) is larger than any difference between arms at seed 0 (at most 10 tasks).

## Replications (seeds 1 and 2, each its own Holm family of five; reported, seed 0 decides)

| Test | Seed 0 difference, Holm p | Seed 1 difference, Holm p | Seed 2 difference, Holm p |
|---|---|---|---|
| H17.1 Theo against parent | +24.4 points, 1.7e-161 | +24.0 points, 5.3e-145 | +24.2 points, 1.2e-158 |
| H17.2 Hazel against parent | +24.8 points, 1.3e-156 | +23.8 points, 9.2e-131 | +25.0 points, 2.0e-164 |
| H17.3 Theo against Hazel | -0.4 points, 1 | +0.2 points, 0.68 | -0.8 points, 0.057 |
| H17.4a Theo against solver | +0.04 points, 1 | +0.9 points, 0.15 | +0.6 points, 0.18 |
| H17.4b Hazel against solver | +0.4 points, 1 | +0.7 points, 0.20 | +1.5 points, 0.0017 |

H17.1 and H17.2 hold in both replications, so they are robust under the preregistered rule. One replication result is nominally significant: Hazel against the solver control at seed 2 (67 against 32 discordant tasks, Holm p = 0.0017). It does not change any verdict. Replications are reported only and seed 0 decides, and the seed-2 difference, 1.5 points, is below the preregistered 2-point minimum, so it would fail H17.4b even as the deciding seed. Read together, the three seeds put Hazel between 0.4 and 1.5 points above the solver control and Theo between 0.04 and 0.9 points above it.

## Quantisation (H17.5)

| Child | Q8_0 solved | Q4_K_M solved | Only Q4 / only Q8 | Difference | One-sided 95% lower bound | Margin | Pass |
|---|---|---|---|---|---|---|---|
| Hazel | 894 | 830 | 34 / 98 | -2.7 points | -3.5 points | -2.0 | no |
| Theo | 885 | 749 | 31 / 167 | -5.7 points | -6.6 points | -2.0 | no |
| Solver control (reported) | 884 | 755 | 45 / 174 | -5.4 points | -6.4 points | -2.0 | no |

Q4_K_M costs these 135M children between 2.7 and 5.7 points and adds some malformed answers (35 for Theo, 1 for Hazel, 41 for the solver control, against at most 1 at Q8_0). File sizes: Q8_0 144,810,912 bytes, Q4_K_M 105,453,984 bytes.

## Membership

Under the frozen rule only the seed-0 Q8_0 runs of Theo and Hazel decide admission. Both pass R1 (Wilson lower bounds 0.351 and 0.354 against 0.25, format 1.000, solve rate above 0.1393). Theo and Hazel therefore join the colony as Q8_0 files (../../COLONY.md). They also beat their parent by a wide margin (H17.1 and H17.2), so the README rule that an offspring enters only if it beats its parent on a sealed test holds here. The EXP-CZ-017 gate itself did not require the parent comparison; future offspring specifications will require both R1 and a preregistered win over the parent. The solver control and seeds 1 and 2 also pass R1, which is reported only; the solver control is a control, not a member. The parent fails all three R1 conditions: its solve rate sits at the guessing baseline, and only 41.8% of its answers are well formed.

## By family and cell

Seed 0, Q8_0, solved per family:

| Run | Arithmetic (599) | Graph reachability (598) | JSON extraction (598) | List transforms (598) |
|---|---|---|---|---|
| Parent | 1 | 300 | 0 | 0 |
| Theo | 8 | 576 | 63 | 238 |
| Hazel | 6 | 575 | 74 | 239 |
| Solver control | 8 | 578 | 65 | 233 |

1. The parent's 300 graph solves are exactly the constant-answer floor on a family whose two answer classes are almost equal in size. Its only other solve is one arithmetic task.
2. All three trained arms learn graph reachability (above 96%) and the easy list cells, and reach about 11% on JSON.
3. None of them learns arithmetic. Arithmetic is 27% of the training set (2,361 of 8,621 examples, including the full 600 shared tasks at difficulty 4 and at difficulty 5), yet every child solves at most 12 of 599 sealed arithmetic tasks. The same holds for list transforms at difficulty 5 (599 training examples, at most 4 of 120 sealed tasks solved). At 135M parameters, checked examples alone did not teach this parent these hard cells.

Per cell, every child, with the two exempt cells marked and each cell's share of the training examples. All three arms train on the same 8,621 task ids, one example per task, so the share is the same for every child. Column key: T Theo, H Hazel, S solver control, digit = seed, Q8_0 unless marked q4.

| Cell | n | Training examples (share of 8,621) | Parent | T0 | T1 | T2 | H0 | H1 | H2 | S0 | S1 | S2 | T0 q4 | H0 q4 | S0 q4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| arith_chain d1 | 119 | 583 (6.8%) | 0 | 2 | 4 | 3 | 3 | 3 | 3 | 4 | 5 | 3 | 5 | 4 | 5 |
| arith_chain d2 | 120 | 400 (4.6%) | 0 | 2 | 1 | 3 | 1 | 1 | 2 | 0 | 1 | 1 | 2 | 1 | 2 |
| arith_chain d3 | 120 | 178 (2.1%) | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 0 | 2 |
| arith_chain d4 | 120 | 600 (7.0%) | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 |
| arith_chain d5 | 120 | 600 (7.0%) | 0 | 2 | 1 | 2 | 0 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |
| graph_reach d1 | 118 | 546 (6.3%) | 60 | 110 | 106 | 114 | 111 | 103 | 116 | 113 | 99 | 102 | 79 | 108 | 96 |
| graph_reach d2 | 120 | 524 (6.1%) | 60 | 116 | 118 | 118 | 117 | 113 | 119 | 117 | 113 | 117 | 84 | 112 | 89 |
| graph_reach d3 | 120 | 491 (5.7%) | 60 | 115 | 116 | 117 | 112 | 110 | 116 | 113 | 111 | 114 | 96 | 109 | 94 |
| graph_reach d4 | 120 | 460 (5.3%) | 60 | 117 | 114 | 119 | 116 | 111 | 118 | 116 | 109 | 111 | 114 | 115 | 113 |
| graph_reach d5 | 120 | 443 (5.1%) | 60 | 118 | 119 | 118 | 119 | 119 | 119 | 119 | 118 | 119 | 108 | 118 | 102 |
| json_extract d1 | 120 | 495 (5.7%) | 0 | 24 | 18 | 19 | 25 | 24 | 21 | 23 | 26 | 23 | 18 | 20 | 23 |
| json_extract d2 | 118 | 498 (5.8%) | 0 | 15 | 22 | 18 | 18 | 20 | 22 | 16 | 17 | 14 | 14 | 16 | 14 |
| json_extract d3 | 120 | 223 (2.6%) | 0 | 20 | 22 | 18 | 24 | 25 | 22 | 20 | 16 | 16 | 18 | 18 | 20 |
| json_extract d4 (exempt) | 120 | 87 (1.0%) | 0 | 3 | 2 | 2 | 3 | 3 | 2 | 4 | 2 | 4 | 2 | 3 | 3 |
| json_extract d5 (exempt) | 120 | 120 (1.4%) | 0 | 1 | 2 | 1 | 4 | 2 | 2 | 2 | 1 | 0 | 1 | 3 | 1 |
| list_transform d1 | 118 | 577 (6.7%) | 0 | 112 | 113 | 113 | 109 | 111 | 111 | 108 | 112 | 113 | 107 | 102 | 90 |
| list_transform d2 | 120 | 587 (6.8%) | 0 | 83 | 81 | 78 | 84 | 83 | 86 | 82 | 83 | 82 | 67 | 74 | 71 |
| list_transform d3 | 120 | 328 (3.8%) | 0 | 23 | 18 | 14 | 24 | 21 | 18 | 25 | 21 | 20 | 17 | 12 | 13 |
| list_transform d4 | 120 | 282 (3.3%) | 0 | 18 | 15 | 18 | 21 | 16 | 17 | 16 | 15 | 17 | 11 | 10 | 12 |
| list_transform d5 | 120 | 599 (6.9%) | 0 | 2 | 1 | 2 | 1 | 1 | 1 | 2 | 1 | 4 | 1 | 2 | 2 |

The two exempt cells (JSON extraction at difficulty 4 and 5, 1.0% and 1.4% of the training examples) stay near zero for every child: 2 to 4 of 120 at difficulty 4 and 0 to 4 of 120 at difficulty 5. This experiment cannot say how the children would do there with enough training examples.

## Exploratory: the nine untrained founders on sealed set 3

Not part of the plan and not in the analysis plan. Same runner, same scored file, greedy, each founder with its frozen template. No hypothesis is tested and no paired test was run on these rows; the intervals are Wilson 95% intervals computed from the summary counts. They place the children in the colony's standings and nothing more.

| Run | Parameters | Solved | Solve rate | Format valid | Same member on sealed set 2 (EXP-CZ-009) |
|---|---|---|---|---|---|
| Quinn (Qwen3.5-0.8B) | about 0.8B | 1,048 | 0.438 [0.418, 0.458] | 0.869 | 0.427 |
| Hazel seed 0 | 135M | 894 | 0.374 [0.354, 0.393] | 1.000 | - |
| Theo seed 0 | 135M | 885 | 0.370 [0.351, 0.389] | 1.000 | - |
| Solver control seed 0 | 135M | 884 | 0.369 [0.350, 0.389] | 1.000 | - |
| Graham (granite-4.0-350m) | 352M | 793 | 0.331 [0.313, 0.351] | 0.551 | 0.345 |
| Quentin (Qwen3-0.6B) | about 0.6B | 670 | 0.280 [0.262, 0.298] | 0.589 | 0.295 |
| Grace (Granite-4.0-H-350M) | about 340M | 585 | 0.245 [0.228, 0.262] | 0.998 | 0.234 |
| Erin (ERNIE-4.5-0.3B) | 361M | 470 | 0.196 [0.181, 0.213] | 0.689 | 0.198 |
| Mina (MiniCPM4-0.5B) | 434M | 433 | 0.181 [0.166, 0.197] | 0.598 | 0.182 |
| Sam (SmolLM2-360M) | about 362M | 365 | 0.153 [0.139, 0.168] | 0.776 | 0.158 |
| Rowan (RWKV-7 G1d 0.4B) | about 0.4B | 308 | 0.129 [0.116, 0.143] | 0.916 | 0.128 |
| Parent (SmolLM2-135M) | 135M | 301 | 0.126 [0.113, 0.140] | 0.418 | - |
| Bastien (Baguettotron 600M) | 608M | 131 | 0.055 [0.046, 0.065] | 0.104 | 0.065 |

1. The children, at 135M parameters, sit second, behind only the untrained Quinn, and ahead of every other untrained founder, all of which are 2.5 to 6 times larger. The gap to Graham is about 4 points and the intervals nearly touch; without a paired test this ordering is descriptive.
2. The children are compared here with untrained founders. The trained founders of EXP-CZ-010 and EXP-CZ-011 were not run on sealed set 3, and they solve far more on set 2 than any founder does untrained.
3. Every founder lands within 1.5 points of its sealed set 2 rate, so sealed set 3 looks neither harder nor easier than set 2 for the colony.
4. Read descriptively, no untrained founder would pass R1 on these numbers. Quinn, Graham and Quentin clear the 0.25 lower bound on solve rate but fail on format (below 0.90); the other six have lower bounds below 0.25.

## Deviations from the preregistration

All of these were decided and recorded before any child saw sealed set 3.

1. The specification chain. Two earlier specifications of this experiment stopped at their data gate before any child trained (see PREREGISTRATION.md). This one exempts JSON extraction at difficulty 4 and 5 from the per-cell minimum. The hypotheses keep the wording and tests of the first specification. The training set is 8,621 shared tasks.
2. Exploratory comparators. The first specification planned to run the nine founders and every finished EXP-CZ-010 and EXP-CZ-011 adapter on sealed set 3. The frozen manifest limits the comparators to the nine untrained founders (owner decision before the freeze).
3. Readings fixed before the freeze (owner decisions, in the manifest): the H17.5 bound is the one-sided 95% Wald bound of the paired difference; only seed-0 Q8_0 Theo and Hazel decide membership; a seed-0 result counts as not robust only if both replications reverse its sign; the guessing baseline comes from the 13 planned ledgers; Holm is over exactly the five seed-0 tests, with minimum differences compared in whole tasks.
4. Endpoints not fully reported. The preregistration lists GGUF bytes, peak memory, tokens per second, teacher spend and GPU minutes per arm. File sizes are reported above. Teacher spend for the training data was 0.67 USD for DeepSeek V4.1 Flash and 0.39 USD for MiMo V2.6 Flash, 1.06 USD in total, across the two earlier specifications; this experiment reuses those answers. Peak memory and GPU minutes are not in the frozen sources and are not reported. The run log records generation speed per run (80 to 788 tokens per second), but the runs were not set up as a speed comparison, so those numbers are not interpreted.

## Incident: the commitment was published after the runs

This is a real protocol slip, shared with EXP-CZ-010 and EXP-CZ-011. Our method says each commitment is pushed to the public repository and timestamped before its sealed run. The freeze roots were frozen at 04:30:59Z and submitted to OpenTimestamps at about 04:33Z. They were not pushed to the public repository before the runs, and the sealed set 2 driver for EXP-CZ-010 started at 04:32:02Z, before the timestamp was submitted.

So the external timing evidence is the Bitcoin attestation alone, and the 04:30:59Z freeze time is our own record, not independently established. All three roots (../../public-commitments/EXP-CZ-017-freeze.txt and its .ots proof) are anchored in Bitcoin block 973187, mined at 2026-10-26T04:42:29Z. Every EXP-CZ-017 run started after the anchor, the first at 06:46:24Z.

Otherwise, all 22 runs (13 planned, 9 exploratory) ran once, in order, with no void run and no repeat. Generated tokens: 673,123 for the planned runs and 1,855,321 for the exploratory runs (Bastien alone 1,130,905), 2.53 million in total against a cap of 27.0 million.

## Run ledgers

The ledgers are published in the release asset EXP-CZ-017-sealed-run-ledgers.tar.gz (tag exp-cz-017-reveal; SHA-256 in ../../public-commitments/reveal/EXP-CZ-017/README.md). Each ledger records a verdict for every task, so the solve counts here can be recomputed from the ledgers. The runner and checker source is not public, so recomputing verdicts relies on those recorded per-task verdicts.

| Run | Solved | Malformed | Tokens out | Ledger root | Result file SHA-256 |
|---|---|---|---|---|---|
| Parent (SmolLM2-135M-Instruct) | 301 | 1,392 | 211,031 | d2c13a7d3403562d69b868c1ec9fb9c1661462fb2e09a2e6092f54a4ca0c449c | 753811beb162886c070b5c25bd2a0f66ee5b81ce63ebff3d8fa6e155913b5e67 |
| Theo seed 0 Q8_0 | 885 | 1 | 36,789 | e14af63e7bcf5a518fbca9c7024da67037443880b0b26b422d16ccbf8bec9e61 | 2f3f82eaadba7833c0c44c680f87e4967ed7732fcee7612c2e0ea8d852fe0205 |
| Theo seed 0 Q4_K_M | 749 | 35 | 36,522 | 14736f75b5f645cffa62d10034b4ed34f257155aaaf7d5f1fe2965280792107c | 15c6204a32fd7c11b25cc2e90fa74f5c66eeb48ba4ecb769d87becb9b8745618 |
| Theo seed 1 Q8_0 | 876 | 0 | 36,647 | 6ebeaedca1cc0849e03fd0c154ffc361a474ce393889bd8822e21a872876aedc | b4fd76cbf0e0271487f3579eca4fb4e04b960d5e93111382a518f43daf016066 |
| Theo seed 2 Q8_0 | 879 | 2 | 37,656 | b95f540497335ec974e3a5bf533d1d3fec0737b5275243f3cf611db5eb73854d | 87177b21bb51daa92e3d243f4c7a13318888da3ee6dfa3a6e6c1a8b601a84574 |
| Hazel seed 0 Q8_0 | 894 | 0 | 42,174 | 7b9e3df1f6329a4267a227b13bbe8ad7a7fcbf4aded5934ff171569a77922f2f | 41441ddb7592ddf75f3bdb3de526a44c21beeb29480fd9e4a190d009322b74a2 |
| Hazel seed 0 Q4_K_M | 830 | 1 | 41,991 | 4aafca324a063effe0345396321d96b7faa8b9364dc8b4db71a06bb053048fca | 6b08627f6a18bcb8b22c46949a11b6c5dbcb30cd86e3f8f218af02eae6e2057f |
| Hazel seed 1 Q8_0 | 871 | 0 | 42,220 | 471ac446b8d36333603ce5e24d0e7a92fbdb41511feb19aa5e810373794be167 | 49cefb50fc5eb2b78459c88239d0892bf83bc5aaa45f753b8e1b8174e704e11b |
| Hazel seed 2 Q8_0 | 899 | 0 | 42,184 | e72e0be339bd502427e240669977139cec629d661979cbdd455953b41c7c1b76 | 7bff5d2e59f0d472bbbd0f714f41b66b01888db22478488e1be4dc7d45658e5c |
| Solver control seed 0 Q8_0 | 884 | 0 | 36,505 | e020fe391c3fc98add44f6a51acf3d38dc66e6b5af6ebdb863a4e9e6943409d7 | 5fce9e8c612412abf91094360b9fcb03e28605d5d844694d611d1eec01549ce1 |
| Solver control seed 0 Q4_K_M | 755 | 41 | 36,439 | 734957f529dc81988fc1f9dd916e9b9719398ed2f9ecb599b7f33161841f7bc8 | 39b9a1d2396fbf32872f6c87ff98104de9427be6e8838155a505604a0e413b66 |
| Solver control seed 1 Q8_0 | 854 | 2 | 36,451 | cf2425b54f41e048d49cc29df00c8b125fc88c715828949716248f98d4df63b5 | 65acac2692090bf745de427f3eb6eb0a92f64e23ca50cb1c0edd3a575be2840f |
| Solver control seed 2 Q8_0 | 864 | 3 | 36,514 | 0a64dc4ecf6610c9e1a7bca8f044f655dfcf2f7c49ab5b9ad7706d364fb39b19 | 93e47437fe08f1f8a0b9e7a5b886e2a6deba180f060a0620a4f6aa443327145b |

Exploratory runs (not in the plan):

| Run | Solved | Malformed | Tokens out | Ledger root | Result file SHA-256 |
|---|---|---|---|---|---|
| Sam untrained | 365 | 536 | 58,865 | 1ab75445ca0ae0517911195ab450486f4fc061b3a0211f1021f192e2c6173e97 | 952fd7a0bebfd68b3183fe3cebe4004cde9841c575deb9013c72235101b76d7e |
| Grace untrained | 585 | 5 | 32,418 | 893d245bf68d6ae1d07ba110fc821f06b9049f73adb19ee0eaba0659b3741017 | 6ff40eae9cfa7e6cf2b6b0f4aa305021f7d1dd8e73ef171e892075941d235432 |
| Quentin untrained | 670 | 983 | 93,643 | d4bc732cc1608efb728b4b7e220339e89ca11f57bb5fb6fd04eb17e8f22e52fe | e0b0a9a0467fb134c06d533c7e28f07685ecf3b935ed3b666935aafdb9919397 |
| Quinn untrained | 1,048 | 313 | 122,352 | bcb3bfc46e9841299f7bcd0dcef9eea3d06cbc6e74b248a1141c19a46705160e | 77c3cb8f6cc15f03af67a42e5558bd47f8bc249183f3be58944a76fb97f9d572 |
| Graham untrained | 793 | 1,074 | 143,188 | f43ed1639d3e396564c884197cc60eee57dec571e15c20536c45fa1b4688e192 | dca03a39eb3d746e56819e94de4fd3cf4c8f9b967cda01f01d90428c5f0eb148 |
| Rowan untrained | 308 | 202 | 32,682 | 67f68dce0bcb5b0613c3fea0491b600a32ba9568268bef6c354bc6aaf81b8121 | 6906d8a9bd3c2425464cff3d6b212bce7a7b205fa9bb39fe5b6d7f2b50e51c4c |
| Erin untrained | 470 | 744 | 111,608 | 3fe1a0e87903d236eedb94389bcbbc957afb8dbc6ccab4d9f9a0fe0d41545abf | bcbc27a58db99b43cd7ea20310a5aa9375a6c002511fce0c7afb6a030c3ebaea |
| Bastien untrained | 131 | 2,143 | 1,130,905 | 6fc6c406e8bd2641a484a30131b3334496c712b60ccde1fb7aa36fcd9e1dfe6d | a5bcf1a840828c1c6c29b28b1e7aaae8f1d58ba63448e89742d98da3715fe36b |
| Mina untrained | 433 | 963 | 129,660 | 6f6e18e154e5845022e0a4c34a453dcebac17338d7bae9c6e5091ccaab0a611d | 1e5e7df9af1980f6f7382aa31b03b0237d51188fd8a01a4ab6dc3ddfaebcff2b |

## What this does not show

- Generalisation. The sealed tasks come from the same generator families and difficulty levels as the training tasks; these are in-distribution gains on four synthetic families.
- Robustness across test sets. One sealed set (set 3), 2,393 scored tasks.
- Behaviour under other decoding. Greedy, 512-token cap, one template.
- Anything about other parents or larger models. One parent, SmolLM2-135M-Instruct; the founders compared are about 340M to 800M.
- That teachers never help. The teachers matched correct solver labels on tasks where both teachers were already correct. Teacher reasoning traces, logprobs, tasks only a teacher can answer, or a larger student could still differ.
- How the children do on hard JSON with enough training examples, or on arithmetic with a different recipe.
- How a child behaves inside a colony.

## Next

The colony can make small members of its own: a 135M parent trained on 8,621 checked answers nearly triples its solve rate and clears R1, with either teacher. On this evidence neither teacher showed a preregistered advantage over correct labels on the same tasks, which the generator supplies at no teacher cost. Solver labels are therefore a reasonable default to test for the next children, with teachers kept for tasks where no solver exists; a full cost comparison was not measured here. The children ship as Q8_0. Arithmetic is the open weakness at this size. A planned generator revision that states the JSON noun convention would let the exempt cells be gated normally. Open items: peak-memory and GPU-minute accounting, and five or more training seeds for the next children.
