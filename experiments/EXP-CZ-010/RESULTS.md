# EXP-CZ-010 results: targeted adapter for every founding member (self-taught)

Status: REPORTED 2026-10-26. Frozen 2026-10-26T04:30:59Z together with EXP-CZ-011 (root 1468e1c6..., ../../public-commitments/EXP-CZ-010.md). Sealed run 2026-10-26T04:32:02Z to 06:10:21Z on one 16 GB consumer GPU: first the untrained control (8 runs), then the self-taught adapters (8 runs), all with one frozen runner binary (SHA-256 4e9d101a...). Analysis by the frozen paired-analysis program (SHA-256 955bb78a..., bound in the manifest) with the frozen analysis plan. Sealed set 2: 1,200 tasks, SHA-256 578bc7a8..., revealed 2026-10-26 and retired; the manifest reveal is partial (../../public-commitments/reveal/EXP-CZ-009-011/README.md). Timing: published after the runs; externally anchored no later than Bitcoin block 973187 (2026-10-26T04:42:29Z). The 04:30:59Z freeze time is our own record. Every adapter run began after the anchor; five untrained control runs began before it (see the incident below).

Read first. Every adapter here was trained once, with one training seed. Our methodology asks for at least five seeds for anything that learns, so this is a departure from that rule: seed variance is unknown, and the learning results are preliminary on that axis. All gains are within four synthetic Forge task families, tested on fresh tasks from the same generators as the training tasks.

The frozen analysis plan (analysis_plan.json) and the analysis output (analysis/results.json) are not published: both contain local file paths in a notes field, which our publication policy does not allow. The tests themselves are standard (exact McNemar, Holm, Wilson intervals) and can be recomputed from the per-task verdicts in the ledgers, but the frozen plan that maps runs to tests cannot be checked from this repository.

## Outcome

Training each member on its own checked answers raised its sealed solve count for all 8 members that were tested, so H10.1 is SUPPORTED (8 of 8 against a bar of 5). Graham was not tested, because his adapter failed the parity gate; he enters the Holm family of nine at p = 1. The gains run from +4.5 points (Sam) to +40.2 points (Quinn, 42.7% to 82.8%).

H10.2 is SUPPORTED: Grace, Quentin, Quinn and Rowan fail R1 untrained and pass it adapted.

H10.3 is NOT SUPPORTED. Format validity fell by more than 2 points (24 tasks) for two members: Erin has 169 more malformed answers than untrained and Grace 26. Under R10.2 both adapters are recorded as harmful on format, even though Grace's adapter more than doubles her solves and passes R1.

The untrained control, rerun with the adapters' runner, reproduced EXP-CZ-009's sealed results exactly for all 8 members. That is a runner-determinism check, and it means the choice of control does not change any result here.

## Hypotheses

| Hypothesis | Verdict | Evidence |
|---|---|---|
| H10.1 for at least five of the nine members, the adapted member solves more sealed tasks than the untrained member (exact McNemar, Holm over nine, alpha 0.05) | SUPPORTED | 8 of 8 tested members gain, every Holm p below 3e-8. Graham not tested (parity gate), counted at p = 1. |
| H10.2 at least one member that fails R1 untrained passes R1 adapted | SUPPORTED | Grace, Quentin, Quinn and Rowan. |
| H10.3 format validity (E2) does not fall for any member by more than 2 points | NOT SUPPORTED | Erin +169 malformed answers, Grace +26; the limit is 24 of 1,200. The other six members have fewer malformed answers than untrained. |

R10.1: all 8 adapters work. R10.2: no adapter lowers E1 significantly; the Erin and Grace adapters are recorded as harmful on format. R10.3: met (8 of at least 5).

## Standings (greedy, 1,200 sealed tasks of set 2, 95% Wilson intervals)

| Rank | Member | Untrained solved | Self-taught solved | Self-taught solve rate | Format valid, untrained to self-taught | Solves per million tokens, self-taught | R1 self-taught | Only self-taught / only untrained | Holm p |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Quinn (Qwen3.5-0.8B) | 512 (0.427) | 994 | 0.828 [0.806, 0.849] | 0.871 to 0.975 | 2,817 | pass | 494 / 12 | 4.5e-128 |
| 2 | Quentin (Qwen3-0.6B) | 354 (0.295) | 771 | 0.643 [0.615, 0.669] | 0.593 to 0.977 | 4,831 | pass | 420 / 3 | 9.3e-120 |
| 3 | Grace (Granite-4.0-H-350M) | 281 (0.234) | 587 | 0.489 [0.461, 0.517] | 0.998 to 0.976 | 4,372 | pass | 315 / 9 | 3.5e-80 |
| 4 | Rowan (RWKV-7 G1d 0.4B) | 154 (0.128) | 565 | 0.471 [0.443, 0.499] | 0.913 to 0.997 | 4,787 | pass | 415 / 4 | 1.3e-116 |
| 5 | Erin (ERNIE-4.5-0.3B) | 237 (0.198) | 375 | 0.313 [0.287, 0.339] | 0.687 to 0.546 | 532 | fail: format | 322 / 184 | 2.7e-9 |
| 6 | Mina (MiniCPM4-0.5B) | 218 (0.182) | 369 | 0.308 [0.282, 0.334] | 0.598 to 0.737 | 2,351 | fail: format | 155 / 4 | 3.6e-40 |
| 7 | Sam (SmolLM2-360M) | 189 (0.158) | 243 | 0.203 [0.181, 0.226] | 0.758 to 0.973 | 1,653 | fail: lower bound | 55 / 1 | 6.3e-15 |
| 8 | Bastien (Baguettotron 600M) | 78 (0.065) | 147 | 0.123 [0.105, 0.142] | 0.130 to 0.254 | 223 | fail: all three conditions | 109 / 40 | 2.8e-8 |
| - | Graham (granite-4.0-350m) | not run | not run | - | - | - | - | - | 1 (untested) |

Guessing baseline: 0.125, upper Wilson bound 0.1449, read back from all 24 ledgers in the analysis plan. "Untrained" is the same-binary rerun, the primary control.

## The untrained control reproduces EXP-CZ-009

The frozen Season 0 runner that made the EXP-CZ-009 ledgers cannot load an adapter. So, by an owner decision before the freeze, the primary control is a fresh untrained run of each member with the adapters' runner, and EXP-CZ-009's ledgers are a secondary reference only. For all 8 members the rerun matches EXP-CZ-009 exactly in solved tasks, malformed answers, output tokens and solves per family. The two comparisons (adapted against the rerun, and adapted against EXP-CZ-009) give identical discordant counts and p values for every member. Greedy decoding with this inference-server build gave the same answers under two runner binaries. The ledger roots differ, as expected, because the run ids and experiment labels differ.

## By family (solved of 300, untrained to self-taught)

| Member | Arithmetic | Graph reachability | JSON extraction | List transforms |
|---|---|---|---|---|
| Quinn | 54 to 287 | 221 to 270 | 217 to 262 | 20 to 175 |
| Quentin | 8 to 293 | 150 to 150 | 184 to 230 | 12 to 98 |
| Grace | 3 to 9 | 150 to 291 | 95 to 184 | 33 to 103 |
| Rowan | 0 to 178 | 149 to 298 | 5 to 77 | 0 to 12 |
| Erin | 0 to 221 | 150 to 152 | 86 to 0 | 1 to 2 |
| Mina | 0 to 0 | 150 to 150 | 67 to 173 | 1 to 46 |
| Sam | 3 to 4 | 150 to 163 | 30 to 64 | 6 to 12 |
| Bastien | 57 to 92 | 21 to 55 | 0 to 0 | 0 to 0 |

1. The gains are not uniform. Quentin, Quinn, Rowan and Erin learn arithmetic, which most of them could not do untrained. Grace and Rowan stop giving one constant answer on the balanced yes/no graph family and reason (291 and 298 of 300).
2. Quentin and Mina still score exactly 150 of 300 on graph reachability after training, the constant-answer floor.
3. Erin trades one family for another. She gains 221 arithmetic tasks and loses all 86 JSON tasks she solved untrained. Her self-taught run produces 609,963 output tokens, about 508 per task against the 512-token cap, compared with 56,043 untrained. So most of her answers now run to or near the cap, which is the likely source of the extra format failures. The ledgers were not inspected answer by answer for this report.
4. Bastien's thinking mode still dominates after training: 570,241 output tokens and 895 malformed answers of 1,200.

## Training and cost (reported, not tested)

| Member | Kept examples | Chosen epoch (dev 0 to 399 solves, epoch 1 / epoch 2) | Serving | Served file bytes | Parity, max top-10 difference |
|---|---|---|---|---|---|
| Sam | 882 | 1 (86 / 85) | adapter | 34,764,896 | 0.0017 |
| Grace | 1,171 | 2 (176 / 193) | adapter | 30,190,176 | 0.0006 |
| Quentin | 1,367 | 2 (241 / 253) | adapter | 40,397,152 | 0.0044 |
| Quinn | 2,128 | 1 (337 / 316) | adapter | 43,316,384 | 0.0017 |
| Rowan | 1,017 | 1 (190 / 145) | merged, Q8_0 | 523,649,152 | 0.0002 |
| Erin | 1,364 | 1 (129 / 129, tie broken by fewer format failures) | adapter | 24,200,224 | 0.0005 |
| Bastien | 689 | 2 (49 / 52) | adapter | 55,882,784 | 0.0026 |
| Mina | 884 | 2 (116 / 117) | adapter | 33,446,528 | 0.0015 |

No member was data-starved: all kept at least 200 examples. The parity tolerance is 0.02. Generated tokens in the sealed run: 863,270 for the control and 1,463,371 for the self-taught arm, 2.33 million in total against a cap of 9.83 million. Wall time: control 36 minutes, self-taught arm 62 minutes. GPU minutes for sampling and training are an endpoint in the preregistration, but they were not recorded in the frozen sources, so they are not reported.

## Deviations from the preregistration

All of these were decided and recorded before any adapter saw sealed set 2.

1. Control. The first draft of the design said the untrained run comes from EXP-CZ-009. The frozen manifest instead makes the same-binary untrained rerun the primary control, because the Season 0 runner cannot load an adapter and pairing against it would mix the runner with the adapter. EXP-CZ-009's ledgers are reported beside it. The two give identical results.
2. Graham is not counted. His adapted model returns NaN logits in llama.cpp on two of the three parity prompts, whether the adapter is loaded or merged, and also with half precision disabled. An earlier bug in the parity check had let him pass without a real comparison; it was fixed, and the check fails. Under the parity gate he is reported as not run and enters the Holm family of nine at p = 1. The five-member threshold is unchanged.
3. Training file: 1,996 tasks, not 2,000, after dropping 4 tasks whose prompts repeat in other splits or in the file. None overlaps sealed set 2.
4. Training answers were sampled with concurrent requests, which are not bit-reproducible run to run. This affects training data only; the kept answers are whatever the recorded ledgers hold. Sealed runs are sequential.
5. Rowan's adapter is merged into the base weights and served as Q8_0, because llama.cpp cannot apply an adapter to his target modules.
6. Trainer changes during training: the parity-check fix and a later correction to it; a chunked output head for the Qwen3.5 architecture; memory-only settings for Quinn and Bastien (smaller micro-batches, and for Quinn weights kept resident; adapters byte-identical). The recipe (batch of 16 sequences, rank, learning rate, epochs, seed) is unchanged. Quinn is counted by owner decision before the freeze.
7. Runner: the sealed runs use one frozen runner binary (4e9d101a...). The dev epoch choices for Sam and Quentin were made with an earlier build of the same runner (d10a713a...), recorded in the manifest.

## Incident: the commitment was published after the runs

This is a real protocol slip. Our method says each commitment is pushed to the public repository and timestamped before its sealed run. The freeze roots of EXP-CZ-010, EXP-CZ-011 and EXP-CZ-017 were frozen at 04:30:59Z and submitted to OpenTimestamps at about 04:33Z. They were not pushed to the public repository before the runs, and the sealed set 2 driver started at 04:32:02Z, before the timestamp was submitted.

So the external timing evidence is the Bitcoin attestation alone, and the 04:30:59Z freeze time is our own record, not independently established. All three roots (../../public-commitments/EXP-CZ-010-freeze.txt and its .ots proof) are anchored in Bitcoin block 973187, mined at 2026-10-26T04:42:29Z. Five runs started before that block: the untrained control runs for Sam, Grace, Quentin, Quinn and Rowan (04:32:02Z to 04:42:28Z). They are untrained base models, and their solve counts equal EXP-CZ-009's sealed results exactly. Every adapter run started after the anchor, the first at 05:08:02Z.

Otherwise, all 16 runs ran once, in order, with no void run and no repeat. Serving several adapters from one server was found not to be equivalent to serving one, and was not used.

## Run ledgers

The ledgers are published in the release asset EXP-CZ-009-011-sealed-run-ledgers.tar.gz (tag exp-cz-009-011-reveal; SHA-256 in ../../public-commitments/reveal/EXP-CZ-009-011/README.md). Each ledger records a verdict for every task, so the solve counts here can be recomputed from the ledgers. The runner and checker source is not public, so recomputing verdicts relies on those recorded per-task verdicts.

| Run | Solved | Malformed | Tokens out | Ledger root | Result file SHA-256 |
|---|---|---|---|---|---|
| Sam untrained control | 189 | 291 | 30,753 | 3272a92ee64a752341f56c397a2dd9eb801ed6ba64b7e6de4bab61fd8d74b2e2 | 8f3907a7372d7d5af9faf5e8792c02061e2964bd830365413928ecbae3a064bf |
| Grace untrained control | 281 | 3 | 16,190 | b6c162b5b909fd20c22841cde70db8dabccb63c0e0ff0068b58da13701f773da | b25e3acafee17702086fa63eb2be1ddee1c03ffa634e3f28fe36033a7bf59f41 |
| Quentin untrained control | 354 | 489 | 47,934 | 1a132089194c34bdb0fdc370c91c2811a28184ece5fb619a06e75637cea7b8e7 | 3a7e4802abd6e06bde464653effacbe2b72ba99baa347ef9a1fee9967ef80558 |
| Quinn untrained control | 512 | 155 | 58,552 | 05152666fb437b4be48b023deb140f1b309a4654cc75adb65f6f28ec1c079cdf | d03ea0d7859f406a5f1c7b99a45d5a6c9c7e384fc4b3aaf4096ad7679e4a0416 |
| Rowan untrained control | 154 | 104 | 16,101 | 0329bf592517eab40b71d099b8a9c5d8f756631e3be5de290b2af68095bd03fb | 0899c8ef18f9106241cca6b58a697f685c3bd3b89f3c244236856a8422ed2a9d |
| Erin untrained control | 237 | 376 | 56,043 | 9bead72ccd8e0944942ce8d3ab2aef37ea089c89b5185099b4dc0a9e8dd75599 | 9442c891a4710641d7c2db00a3563a875841d2788d91b2b0339d241951df75aa |
| Bastien untrained control | 78 | 1,044 | 568,648 | 21739a4a7fd3c4a823d0ff5c411b667413fc0b3f18c714e7ac3eb85734b03066 | 5e1ca3d18bd5b99dd4aa24145963c2b0fc288a0f32042f4b0d504664345ec982 |
| Mina untrained control | 218 | 483 | 69,049 | b085fbdbe83ba455c95cfba333a3ef467c112c0ca4812a3483987a1d24b49aae | 4e9ce39a3406c1bdd9c0db111a3b7aca3fac59991d29871fb409bb1969c461ff |
| Sam self-taught | 243 | 32 | 23,434 | 1c1010e9f71cf0a0e649a40f43d0520a0a3f95415e40228fe8cd3f1b3be9c552 | de902ea4b7c1e5fd2675d8d402363831659ad674f9111a212a9619d94db85445 |
| Grace self-taught | 587 | 29 | 18,249 | f8e83207319c989ad04c3fcdae2f57e082fcce2c48ccafb43e1bfcb51bc7195f | 407dfcb38f1344fe6be27c0f1f5236c4b66a55ba0cc1140d6025a4930266c7da |
| Quentin self-taught | 771 | 28 | 61,922 | 4b115f160d46986a7ec9516048bbcf5e4d083c65e93b3b774fb4fbc1e5138401 | 72b63cf7c46c363bec3b81db7605f82ad11f1f9d57ec3eec2b84450aa4b48d08 |
| Quinn self-taught | 994 | 30 | 97,986 | 78a91294e3881c4c1917c36d0d4ac4015a0cc424d582fbb1c1d4601d880e7eb0 | 6f4ca1c510a4fc22ae2b31ae733a277f118436be3b2d3960dd1f80ef9661d8ae |
| Rowan self-taught | 565 | 4 | 27,441 | 4a73c432158c0ed7b4efd110722180e61da33163892a0b171f1ea0ee7f11263a | 6163ccfbb78dd8dcd6dc08817672fa7070305f85d30321e61e8547b0e7477f95 |
| Erin self-taught | 375 | 545 | 609,963 | 1607df816d570624272550f4b3e9ba6133b170cc7057c9e44b93aefd321c9c37 | bef5badf78c3aff87839c5cf28aa32df9a45d10ca746c481bf77d74a28c0b79d |
| Bastien self-taught | 147 | 895 | 570,241 | 0cd9db7e235bdb5d6754e57a04804e450f2a4d846628bd61dde5298b9701ad45 | 15a7e5959aa8838b02cf56e87b069760ab7e10c630830718e55ac24a58a614ef |
| Mina self-taught | 369 | 316 | 54,135 | c13a4c1b63d43b0fdac06904b597c46362d4f3414d550d78b0a93e3c3db47c73 | 04e9ce137bd449b0011a199cb4032a9730f12b7f3b3f12f11056739a761bf9bc |

## What this does not show

- Generalisation. The sealed tasks come from the same generator families and difficulty levels as the training tasks. These are in-distribution gains on four synthetic task families, not evidence of broader skill.
- Robustness across test sets. There is one sealed set (set 2), 1,200 tasks.
- Behaviour under other decoding. Every run is greedy with a 512-token cap; members that ramble (Erin, Bastien) are judged partly on the cap.
- Anything about larger models. All members are small, about 340M to 800M parameters.
- Training-seed variance. Each adapter was trained once, seed 0.
- Graham. His adapters were never run on a sealed set.
- Other quantisations. Every comparison uses Q8_0 base files (merged Q8_0 for Rowan).
- Colonies. Every number is one member answering alone.
- Why a member gains. Data volume, family mix and architecture are not separated.

## Next

Self-training on checked answers is a strong lever for these members on these task families: every tested member improved, and four now clear R1. It does not always help format, and for Erin it shifted skill from JSON to arithmetic while making her answers run long. EXP-CZ-011 compares these self-taught adapters with teacher-taught ones on the same sealed tasks. Open items: GPU-minute accounting, a fix for Graham's NaN logits, and more training seeds.
