# EXP-CZ-001: results so far

Tag: MEASURED, on the dev split only. Dev results are not sealed results. The dev split is public and was used to choose prompt templates, so none of these numbers is a ranking or a standing. No sealed task has been touched. The sealed run has not happened (see PREREGISTRATION.md).

Date of all three phases: 2026-10-24. Decoding was greedy with a fixed seed. Weights were official releases at pinned revisions, with file hashes verified, run at 8-bit quantisation. Every ledger verifies and replays to its reported solve count.

## Phase 0: capacity probe

50 public dev tasks per model (13, 13, 12, 12 per family), one prompt template. This is a throughput and memory check. It says nothing about model quality.

| Model | Solved /50 | Tokens in | Tokens out | Gen tok/s (end to end) | Projected out tokens per model | Projected hours per model |
|---|---|---|---|---|---|---|
| Granite-4.0-H-350M | 4 | 4,157 | 760 | 77.5 | 182,400 | 0.65 |
| SmolLM2-360M-Instruct | 2 | 4,427 | 1,229 | 131.7 | 294,960 | 0.62 |
| Qwen3-0.6B | 0 | 3,400 | 6,305 | 335.2 | 1,513,200 | 1.25 |
| Qwen3.5-0.8B | 5 | 3,400 | 4,197 | 236.4 | 1,007,280 | 1.18 |

Projection basis: 12,000 generations per model. All four models together: about 3.0M generated tokens and 3.7 hours, against caps of 40M tokens and 24 hours. The Phase 0 check passed.

An incident: the first run gave identical answers and token counts for all four models, because a stale server kept answering after its model was swapped. That run was discarded. The probe now refuses to measure unless the server reports exactly the expected model file, and servers are stopped before and after each model. The second run passed that check for all four models.

Phase 0 findings that led to checker fixes: graph reachability scored 0 of 13 for every model because the checker rejected "No" for a reference of "no" (a capitalization effect, fixed). Qwen3-0.6B writes step-by-step prose even when told to give a bare answer. Arithmetic and list transforms scored 0 for every model on 50 tasks, which is too few to conclude anything.

Ledger roots for the four Phase 0 runs (second run):

| Model | Ledger root |
|---|---|
| Granite-4.0-H-350M | 10f99a8b4bd6d32bacb9c45f2e6b12db18b99f0711ebaab72e1f778a453fd0dd |
| SmolLM2-360M-Instruct | f37ee83f0de06538b6043a597c9742c89653bd106b06317ab1e625b71c9b6024 |
| Qwen3-0.6B | 7fdda34302b6053ee18dedca1e2256d5d7a040b30d73f09a1c992ae40169ad16 |
| Qwen3.5-0.8B | ee2bc44ff65c7376b93c61f6d00721f6f3bb66e4f0ec747a3684cb01a8ee0fdf |

## Phase 1: template selection, task suite 0.0.1

400 dev tasks (100 per family), four templates, checker v3, 256-token output cap. Cells are solved of 400.

| Model | P1 | P2 | P3 | P4 | Selected |
|---|---|---|---|---|---|
| Qwen3.5-0.8B | 73 | 161 | 104 | 169 | P4, 169 |
| Granite-4.0-H-350M | 87 | 90 | 94 | 110 | P4, 110 |
| Qwen3-0.6B | 59 | 91 | 108 | 85 | P3, 108 |
| SmolLM2-360M-Instruct | 54 | 56 | 54 | 13 | P2, 56 |

Per family for the selected templates (solved of 100):

| Model | arith_chain | graph_reach | json_extract | list_transform | Output tokens | Hit the 256 cap |
|---|---|---|---|---|---|---|
| Qwen3.5-0.8B (P4) | 100 | 44 | 22 | 3 | 49,680 | 52 |
| Granite (P4) | 44 | 54 | 12 | 0 | 26,339 | 0 |
| Qwen3-0.6B (P3) | 1 | 46 | 59 | 2 | 17,703 | 3 |
| SmolLM2 (P2) | 0 | 46 | 6 | 4 | 9,714 | 7 |

Findings. List transforms failed the suite-validity rule R4: every model scored under 5 percent. Graph reachability sat at the guessing baseline: 54 of 100 dev answers were "no", and the models scored 44 to 54. The output cap was hit 52 times for Qwen3.5. The suite version 0.0.1 is REJECTED as a measuring instrument for these reasons, and it was rescaled before any claim. Arithmetic did discriminate once reasoning was allowed.

Ledger roots for all 16 Phase 1 runs:

| Model | Template | Solved | Ledger root |
|---|---|---|---|
| Granite-4.0-H-350M | P1 | 87 | 06d70623da66f9b1422fcdfc91b105e09180f1fc59ff80d487263506bdfe632a |
| Granite-4.0-H-350M | P2 | 90 | 9e1acc0bd6433d7293295b3d338fefe7d0b1ccbe1f4b7a6d2b3b12ce29f5d104 |
| Granite-4.0-H-350M | P3 | 94 | ee93bf67e13392197196ab1cedafde57d83a839433d7a458b12fa30dbe9e6daa |
| Granite-4.0-H-350M | P4 | 110 | 023894af995dc36d324f4b8b13d8459d4797d11fed399b28f99a6a7d84b1b28b |
| SmolLM2-360M-Instruct | P1 | 54 | 0843dc3c78efbabc5c5b5c9ed5c7e9e72ea6e4be1e449aa5daa6116c255bd320 |
| SmolLM2-360M-Instruct | P2 | 56 | 9933bb04e060583185855ad742aef551315db89d7cd44d704d891cb4aed71251 |
| SmolLM2-360M-Instruct | P3 | 54 | a01610bab72ba5320c0548e3eac9bcd7c41ea95d00e9cc831d6d32d8f3de9f80 |
| SmolLM2-360M-Instruct | P4 | 13 | 5890262af9a39f658d399532cf3bff31075c273bf999f8fc206ad07c2b9f6ec5 |
| Qwen3-0.6B | P1 | 59 | 80cec2e1197446cf65b2b53fa0b50f9558340a0bcdec4ae9b1c957c105a9805d |
| Qwen3-0.6B | P2 | 91 | 672dc25bc6f12d9756ebc26ed1c5e829e56e83588e6f801d958f5e21b59a9e6f |
| Qwen3-0.6B | P3 | 108 | 6ed57ba81ab8c3f56884471f3cb403ce4c589cd27288aabbdc844cc05e903e06 |
| Qwen3-0.6B | P4 | 85 | db4a37756c3cd6fc97108fea5e322c2eaf312c9ef610d09d666425a63b5c30bf |
| Qwen3.5-0.8B | P1 | 73 | e3d2430afd44298bcd2a242166d9e7d514acca3a550e6163b4d7fbe9c3b0e33a |
| Qwen3.5-0.8B | P2 | 161 | 480c6df25a2839764977e270de206a6627e6a7c72b317149e0b6d49d253f8ff1 |
| Qwen3.5-0.8B | P3 | 104 | f3fca07bcdbe907e40c3a0f70c7a2bcf76a3e23f6659d38b1e6aada374ce8acc |
| Qwen3.5-0.8B | P4 | 169 | 8481cbac2117910ff2fa3bab05003fafcb7df05fde89eb6be8f834c0bdfaa636 |

## Phase 1 v2: template selection, task suite 0.0.2

400 public dev tasks (100 per family), 512-token output cap for every arm, checker v3. Selection rule: most dev solves; ties go to fewer format failures, then P1, P3, P2, P4. Cells are solved of 400.

| Model | P1 | P2 | P3 | P4 | Selected |
|---|---|---|---|---|---|
| Qwen3.5-0.8B | 86 | 175 | 106 | 175 | P2, 175 (tie with P4; 51 vs 122 format failures) |
| Qwen3-0.6B | 51 | 88 | 107 | 93 | P3, 107 |
| Granite-4.0-H-350M | 84 | 97 | 98 | 97 | P3, 98 |
| SmolLM2-360M-Instruct | 65 | 57 | 68 | 19 | P3, 68 |

Per family for the selected templates (solved of 100):

| Model | arith_chain | graph_reach | json_extract | list_transform |
|---|---|---|---|---|
| Qwen3.5-0.8B (P2) | 21 | 80 | 65 | 9 |
| Qwen3-0.6B (P3) | 1 | 50 | 54 | 2 |
| Granite (P3) | 0 | 50 | 37 | 11 |
| SmolLM2 (P3) | 0 | 50 | 14 | 4 |

Findings.

1. Graph reachability is now balanced: exactly 50 yes and 50 no per 100. Three of four members score exactly 50, which means they give the same answer to every graph. The old unbalanced set hid this. Only Qwen3.5 (80) is clearly above chance.
2. List transforms cleared R4 after rescaling but stay hard: the best score is 11 of 100.
3. Reasoning helps arithmetic only for some members. With the step-by-step template P4, Qwen3.5 solves 99 of 100 arithmetic tasks and Granite 35. The selection rule maximizes the total, so it picks templates that trade arithmetic for other families.
4. With the 512-token cap, P4 still hits the cap on 91 of 400 tasks for SmolLM2 and 37 for Qwen3.5. The selected templates hit it on 17 or fewer.
5. R4 (every model below 5 or above 95 percent on a family): no family triggers it.

Ledger roots for all 16 Phase 1 v2 runs:

| Model | Template | Solved | Ledger root |
|---|---|---|---|
| SmolLM2-360M-Instruct | P1 | 65 | 9ae092a3c70e2eed31e2c526d30247bfe3010c0fbe49d43780de410dc5f0a3e0 |
| SmolLM2-360M-Instruct | P2 | 57 | a9e4416d0185dfd6d45d4e7b814a0d560e327be6f6789a19042896ed24286c8a |
| SmolLM2-360M-Instruct | P3 | 68 | badca3e222a12355bccabf747111be04eb4a16f6334526d2a70e40a489ea9d8c |
| SmolLM2-360M-Instruct | P4 | 19 | f17d5f9e8fde71d1d81bbe63c0905ff98bde23c6de99fcd6271a1fdd73167cab |
| Qwen3-0.6B | P1 | 51 | be7a2adc0477079b3e776412846f4523ddfdb9b4d4559a2f62cebdf032a30f94 |
| Qwen3-0.6B | P2 | 88 | ec538f40ad008420423a0cb9ec0fc10eba75edc7d06c8946335eb4bc1ebc1146 |
| Qwen3-0.6B | P3 | 107 | 08304a5db733f9b8d2f13f5305ccb0ab0f1b8a495d9c76922aa60971a3cbfc00 |
| Qwen3-0.6B | P4 | 93 | 4b79ce08740c7ffa7b2c72f9aa47c68660942438ce9e8ddc4afd4b8d610133f2 |
| Qwen3.5-0.8B | P1 | 86 | be81f6f497c3faa454d3f86fde4b85705e7f28530b999467723385f3f2c87e7d |
| Qwen3.5-0.8B | P2 | 175 | e4a71fbcf837b92d395745036beea807a67fafca96ad2200002c956e33a3ed6b |
| Qwen3.5-0.8B | P3 | 106 | 863d04be1ad72b083e9e828a6b4b851452c0a518e491a3cd0d0e58800398b8f6 |
| Qwen3.5-0.8B | P4 | 175 | d2cc98c36b0d0b7e835c2db67090d1edeaca6d6ee4b62fb284f78eff19172cae |
| Granite-4.0-H-350M | P1 | 84 | 86d09817a963fd4aa3c4fd3bcdf6aa56decc55b740d2f13f0432279133875099 |
| Granite-4.0-H-350M | P2 | 97 | fdbb13fc9f865684b1279c62e05d58bf55cf2aa300d081f247d1d95971ecb747 |
| Granite-4.0-H-350M | P3 | 98 | 96366c1ca698820a807cf16b809453ee41e61fd63fe4dec6b0910ae58fb59230 |
| Granite-4.0-H-350M | P4 | 97 | 8055d4eb624e4b31260001b48cf592839d7be7174c1c55fa61808299caa7d56b |

Contamination note: the first run of this matrix (Granite, P1) overlapped for a few minutes with another job on the same GPU. Answers are unaffected, because decoding was greedy and seeded, but that run's wall time and speed are not comparable.

The ledgers themselves are not in this repository yet. They are released with the experiment's reveal package, and anyone can then check each one against the root above.

## What this does not show

Any ranking. Dev-split numbers choose templates. A ranking comes only from the sealed run after the freeze. The suite was changed twice on the strength of dev results, which is exactly why the sealed set stays untouched.
