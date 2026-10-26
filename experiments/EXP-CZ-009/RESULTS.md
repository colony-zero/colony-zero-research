# EXP-CZ-009 results: second casting

Status: REPORTED 2026-10-26. Frozen 2026-10-25T03:32:59Z (root 1d3dc845..., ../../public-commitments/EXP-CZ-009.md). Sealed run 2026-10-25T03:37:41Z to 04:17:33Z, after the freeze, with the frozen Season 0 runner. Analysis by the frozen analysis program (version 2, bound in the manifest), run twice with byte-identical output. Sealed set 2: 1,200 tasks, SHA-256 578bc7a8... as committed. Sealed set 2 is shared with EXP-CZ-010 and EXP-CZ-011 and will be revealed with them (../../public-commitments/reveal/EXP-CZ-009-011/README.md). Member names: ../../COLONY.md.

## Outcome

No new member is viable alone under the bar written before the run, so H9.1 is NOT SUPPORTED. Graham comes closest. His solve rate clears the bar (lower bound 0.319 against 0.25), but only 55.1% of his answers have the required shape (bar: 90%).

H9.2 is SUPPORTED. Graham, the attention-only Granite, solves 414 sealed tasks against 281 for Grace, his Mamba-2 hybrid sibling from the same lab at almost the same size (261 against 128 discordant tasks, exact McNemar p = 1.4e-11). They win in different places. Graham owns arithmetic. Grace has far better format, leads the colony on lists and beats Graham on JSON (95 against 9).

H9.3 is SUPPORTED. All four first-casting members land inside their Season 0 intervals, so there is no sign that sealed set 2 is harder or easier than sealed set 1.

Exploratory, not preregistered: a per-family rule chosen on dev data, which sends arithmetic to Graham, reaches 60.7% against 42.7% for the best single member.

## Hypotheses

| Hypothesis | Verdict | Evidence |
|---|---|---|
| H9.1 at least one new member passes R1 | NOT SUPPORTED | No member of the nine passes. Graham fails on format (0.551). Rowan passes on format (0.913) but sits at the guessing baseline on solves. |
| H9.2 Graham and Grace differ (exact McNemar, alpha 0.05) | SUPPORTED | 414 against 281 solved; only Graham 261, only Grace 128; p = 1.40e-11 (Holm over all 36 pairs: 1.96e-10). |
| H9.3 the first four fall inside their Season 0 95% intervals | SUPPORTED | Table below. Quinn and Grace sit in the lower half of their intervals. |

| Member | Season 0 (set 1) solve rate [95% interval] | Set 2 solve rate | Inside |
|---|---|---|---|
| Quinn (Qwen3.5-0.8B) | 0.4475 [0.4196, 0.4758] | 0.4267 | yes |
| Quentin (Qwen3-0.6B) | 0.2858 [0.2610, 0.3120] | 0.2950 | yes |
| Grace (Granite-4.0-H-350M) | 0.2508 [0.2271, 0.2761] | 0.2342 | yes |
| Sam (SmolLM2-360M) | 0.1633 [0.1435, 0.1853] | 0.1575 | yes |

## Standings (greedy, 1,200 sealed tasks of set 2, 95% Wilson intervals)

| Rank | Member | Solved | Solve rate | Format valid | Solves per million tokens | Rule R1 |
|---|---|---|---|---|---|---|
| 1 | Quinn (Qwen3.5-0.8B) | 512 | 0.427 [0.399, 0.455] | 0.871 | 1,633 | fail: format |
| 2 | Graham (granite-4.0-350m) | 414 | 0.345 [0.319, 0.372] | 0.551 | 2,045 | fail: format |
| 3 | Quentin (Qwen3-0.6B) | 354 | 0.295 [0.270, 0.321] | 0.593 | 2,431 | fail: format |
| 4 | Grace (Granite-4.0-H-350M) | 281 | 0.234 [0.211, 0.259] | 0.998 | 2,125 | fail: lower bound |
| 5 | Erin (ERNIE-4.5-0.3B) | 237 | 0.198 [0.176, 0.221] | 0.687 | 1,567 | fail |
| 6 | Mina (MiniCPM4-0.5B) | 218 | 0.182 [0.161, 0.204] | 0.598 | 1,268 | fail |
| 7 | Sam (SmolLM2-360M) | 189 | 0.158 [0.138, 0.179] | 0.758 | 1,225 | fail |
| 8 | Rowan (RWKV-7 G1d 0.4B) | 154 | 0.128 [0.111, 0.148] | 0.913 | 1,443 | fail: at the guessing baseline |
| 9 | Bastien (Baguettotron 600M) | 78 | 0.065 [0.052, 0.080] | 0.130 | 119 | fail |

Guessing baseline: 0.125 [0.107, 0.145]. The order is the same as on the dev split. Of the 36 pairs, 32 differ after Holm adjustment. The four that do not: Quentin and Graham (Holm p = 0.12), Erin and Grace (0.12), Rowan and Sam (0.13), Erin and Mina (0.13).

## By family (solve rate, 300 tasks each)

| Member | Arithmetic | Graph reachability | JSON extraction | List transforms |
|---|---|---|---|---|
| Quinn | 0.180 | 0.737 | 0.723 | 0.067 |
| Graham | 0.857 | 0.493 | 0.030 | 0.000 |
| Quentin | 0.027 | 0.500 | 0.613 | 0.040 |
| Grace | 0.010 | 0.500 | 0.317 | 0.110 |
| Erin | 0.000 | 0.500 | 0.287 | 0.003 |
| Mina | 0.000 | 0.500 | 0.223 | 0.003 |
| Sam | 0.010 | 0.500 | 0.100 | 0.020 |
| Rowan | 0.000 | 0.497 | 0.017 | 0.000 |
| Bastien | 0.190 | 0.070 | 0.000 | 0.000 |

1. Graham is an arithmetic specialist. He solves 257 of 300 arithmetic tasks, holding 51 of 60 at difficulty 4 and 38 of 60 at difficulty 5. The next best member solves 57. Beyond the yes/no guessing floor he solves almost nothing else.
2. Graph reachability still belongs to Quinn alone (73.7%, from 54 of 60 at difficulty 1 to 36 of 60 at difficulty 5). Seven members score 148 to 150 of 300 on this balanced yes/no family because they give the same answer almost every time. Counting the last "yes" or "no" in each answer: Sam, Quentin, Erin and Mina say yes 300 times out of 300; Grace says no 300 times, Rowan 299 and Graham 296.
3. Grace keeps the best format discipline in the colony (3 malformed answers of 1,200) and still leads list transforms, the weakest family.
4. Bastien's thinking mode cannot be switched off. 787 of his 1,200 answers hit the 512-token cap, and 672 of his 1,044 format failures are such answers. He generated 568,648 tokens, 61% of the whole run. When he does answer, he answers arithmetic (57 solved, second after Graham).
5. Rule R4 does not fire: no family has every member above 95% or below 5%.

## Decision rules

R1: no member passes. R2: "the strict small-weight class is too small for this suite" (Sam and Grace, as in Season 0). R3: no working backbone, because no member meets R1. R4: the suite is valid.

## Exploratory: colony decision arms

Not part of the preregistered rules. Every arm scores the members' greedy sealed answers against the best single member (Quinn, 0.4267).

| Arm | Calls per task | Solved | Against the best member (only this arm / only Quinn, p) |
|---|---|---|---|
| Perfect routing (ceiling, not realizable) | 1 | 0.712 | 342 / 0, p = 2.2e-103 |
| Per-family rule, chosen on dev | 1 | 0.607 [0.579, 0.634] | 241 / 25, p = 1.6e-45 |
| Majority vote of nine | 9 | 0.453 | 62 / 30, p = 0.0011 |
| Best single member | 1 | 0.427 | baseline |

1. On this set, the first four members alone have a ceiling of 642 tasks (53.5%). All nine reach 854 (71.2%). Of the 212 added tasks, 210 are arithmetic, and Graham is the only solver of 161 of them.
2. The per-family rule is computed by the frozen analysis program from the dev ledgers alone, which were committed before the freeze: arithmetic to Graham, graph reachability and JSON to Quinn, lists to Grace. No sealed answer enters the choice, so its 60.7% is out of sample. In Season 0 the same rule over four members gained 0.7 points, not significant. Here it gains 18.0 points. It is the strongest candidate so far for a preregistered colony arm.
3. A majority vote now beats the best single member; with four members in Season 0 it lost. This is exploratory and should not be read as a rule.

## Deviations and incidents after the freeze

None. All nine runs used the frozen runner and the frozen templates. No run was repeated. The analysis output regenerates bit for bit.

Two notes on the record. Before the freeze, the analysis program was fixed so the five new members get their own arm labels; the fixed version reproduces the EXP-CZ-001 results exactly. And the reused Season 0 runner writes `EXP-CZ-001` and its own built-in manifest digest into each ledger's start event, because the same binary is reused by design. Set 2 runs are identified by their run ids, the tasks file hash and the ledger roots below.

## Run ledgers

The ledgers contain sealed set 2, so they are released with the joint reveal of EXP-CZ-009, EXP-CZ-010 and EXP-CZ-011.

| Run | Solved | Malformed | Tokens out | Ledger root |
|---|---|---|---|---|
| Sam, greedy | 189 | 291 | 30,753 | 4d5e01957ad3ebd21a104a412573a01b17562d50c9e15c417b6d96d8bb22bdba |
| Grace, greedy | 281 | 3 | 16,190 | ecb491b0e80da4e7c91734ea28e2549f366f6d8089c41d24e50b89970edc0e26 |
| Quentin, greedy | 354 | 489 | 47,934 | 32f8733f378e8bfe4b957029433ba992927849ba8667abbd6e141be5457e5747 |
| Quinn, greedy | 512 | 155 | 58,552 | dc094f4d2b9de1225caf5848249ce4833847cd95844c924a7e316413264ce7a3 |
| Graham, greedy | 414 | 539 | 74,378 | b465b77a2083ccd04e21babd31320fc1ba9c54b08692eb1b5a1e7fbde7ec3c2f |
| Rowan, greedy | 154 | 104 | 16,101 | f62389c90da9693e16c0cbfa770c518461271bd6e10783bd86aa9f01cb0d4aed |
| Erin, greedy | 237 | 376 | 56,043 | 1e2c2ab53a03121ca04602392e512036fb6e3d4b61915a93e99c10f215de078b |
| Bastien, greedy | 78 | 1,044 | 568,648 | 300cd8f397208ab21c799912df616a2bb57a4cb63f57a0f59df0877c94585e5b |
| Mina, greedy | 218 | 483 | 69,049 | c6d71fdbc0b9cfd080d76778d814d54579416de01f89c84ec1f42cb8e5612e5c |

About 0.94 million tokens were generated in total.

## What this does not show

- Anything about colonies: every number above is one member answering alone, or an offline combination of those answers.
- Why Graham is good at arithmetic. The architecture contrast with Grace is confounded with training data and prompt template (Graham uses step-by-step, Grace the format-line template).
- Bastien's skill without his thinking mode; his result mostly measures the 512-token cap.
- Real-world skill: the tasks are synthetic and procedurally generated.

## Next

EXP-CZ-010 and EXP-CZ-011 train one adapter per member and compare each adapted member with these runs, task by task, on the same sealed set. Format, not skill, is what keeps the best members under the bar here (Quinn 87.1%, Graham 55.1%, Quentin 59.3%). For Season 1, the dev-chosen per-family rule (+18.0 points here) is the arm to preregister.
