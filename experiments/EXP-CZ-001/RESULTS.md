# EXP-CZ-001 results: Season 0, the first casting

Status: REPORTED. Frozen 2026-10-24T23:45:20Z (root c95f852c..., timestamped), sealed run 2026-10-24T23:47Z to 2026-10-25T00:51Z, analysis by the frozen analysis program run twice with byte-identical output. The sealed set, both salts and the full manifest are now revealed, and every commitment checks out (../../public-commitments/reveal/EXP-CZ-001/README.md). Member names: ../../COLONY.md.

## Outcome

No founding member is viable alone under the bar written before the run. H1.1 is NOT SUPPORTED. H1.2 is NOT SUPPORTED, and rule R2 records "the strict small-weight class is too small for this suite". Both near misses are narrow and in opposite directions. Quinn solves 44.8% of sealed tasks, far above the 12.5% guessing baseline, but only 86.4% of its answers have the required shape (bar: 90%). Grace formats 99.8% of its answers correctly, but the lower bound of its solve rate is 22.7% (bar: 25%).

## Standings (greedy, 1,200 sealed tasks, 95% Wilson intervals)

| Rank | Member | Solved | Solve rate | Format valid | Solves per million tokens | Coverage@8 | Rule R1 |
|---|---|---|---|---|---|---|---|
| 1 | Quinn (Qwen3.5-0.8B) | 537 | 0.448 [0.420, 0.476] | 0.864 | 1,716 | 0.604 [0.576, 0.632] | fail: format |
| 2 | Quentin (Qwen3-0.6B) | 343 | 0.286 [0.261, 0.312] | 0.586 | 2,371 | 0.387 [0.360, 0.415] | fail: format |
| 3 | Grace (Granite-4.0-H-350M) | 301 | 0.251 [0.227, 0.276] | 0.998 | 2,272 | 0.329 [0.303, 0.356] | fail: lower bound |
| 4 | Sam (SmolLM2-360M) | 196 | 0.163 [0.144, 0.185] | 0.775 | 1,255 | 0.298 [0.273, 0.325] | fail |

Guessing baseline: 0.125 [0.108, 0.145]. All six pairwise differences are significant after Holm adjustment (exact McNemar); the closest pair is Quentin and Grace, p = 0.047.

## By family (solve rate)

| Member | Arithmetic | Graph reachability | JSON extraction | List transforms |
|---|---|---|---|---|
| Quinn | 0.193 | 0.810 | 0.700 | 0.087 |
| Quentin | 0.017 | 0.497 | 0.610 | 0.020 |
| Grace | 0.000 | 0.500 | 0.387 | 0.117 |
| Sam | 0.003 | 0.500 | 0.140 | 0.010 |

1. The balanced yes/no graph family separates reasoning from guessing. Quentin (49.7%), Grace (50.0%) and Sam (50.0%) score at the guessing level. Only Quinn does clearly better: 81%, falling from 54 of 60 at difficulty 1 to 42 of 60 at difficulty 5.
2. Quinn solves 58 of 300 arithmetic tasks; the other three solve 6 between them.
3. JSON extraction collapses at difficulty 4 for everyone (Quinn: 60 of 60 at difficulty 3, 18 of 60 at difficulty 4).
4. List transforms are the weakest family, and the smallest member, Grace, leads it. Nobody solves a difficulty-5 list task.
5. Rule R4 does not fire: no family has every member above 95% or below 5%.

H1.3 (rank by solve rate matches rank by published vendor IFEval scores) is pending until the vendor values are sourced and cited.

## Exploratory: can the colony decide better than its best member?

These arms were fixed before the run and never change the rules above. Laya, an open encoder model, routed each task to one member, or judged which member's answer to submit; its routing choices were committed before any member saw a sealed task.

| Arm | Model calls per task | Solved | Against the best member |
|---|---|---|---|
| Perfect routing (ceiling) | 1 | 0.526 | +7.8 points |
| Laya kNN judge | 4 | 0.462 | +1.4 points, p = 0.064, not significant |
| Best member per family | 1 | 0.455 | +0.8 points, p = 0.23 |
| Laya logistic router | 1 | 0.454 | +0.7 points, p = 0.30 |
| Laya kNN router | 1 | 0.451 | +0.3 points, p = 0.61 |
| Best member alone (Quinn) | 1 | 0.448 | baseline |
| Majority vote of four | 4 | 0.442 | worse, p = 0.039 |
| Laya logistic judge | 4 | 0.402 | worse |
| Best member, majority of 4 samples at temperature 0.7 | 4 | 0.354 | worse |
| Laya with no training | 4 | 0.288 | worse |

The colony holds real headroom: picking the right member for every task would solve 52.6%. Nothing tested here captures it yet, and naive teamwork (a vote of four, or resampling the best member) does worse than the best member alone.

## Incident

After the freeze, the encoder step that embeds the sealed answers for the Laya judges first ran on the wrong machine and was stopped. It was rerun on the intended machine, whose embeddings reproduce the original development embeddings to a maximum absolute difference of 1.1e-5. The judge models, routes and analysis program are the frozen ones, and the frozen routing program reproduced the committed routes byte for byte before any judge ran.

## Run ledgers

The eight sealed run ledgers and the development ledgers are release assets of this repository (tag exp-cz-001-reveal), with their SHA-256 values in the reveal README.

| Run | Solved | Ledger root |
|---|---|---|
| Sam, greedy | 196 | 9b671cb5301f4c954193260d3e5d7af61606d192e4dd3f34c62b38cca048104b |
| Quentin, greedy | 343 | 92fca8a682448520c698a782c332deef94643c13c0ab4e7554aaa7af6fff03ee |
| Quinn, greedy | 537 | 9bc7d224c02f879441d9cad5649482fbe6f12cf4567f916595236a93084e9ce6 |
| Grace, greedy | 301 | 4945b8b3b5e9b539e4879231737364cff574f5b2494deff072d1658d0ca6a3ac |
| Sam, 8 samples | 1,349 of 9,600 | 47ce44c788e8231b375291948b5311a706f05cedeafc1331704c990f03708d86 |
| Quentin, 8 samples | 2,660 of 9,600 | 50b32431e47e06fdca4924f251efa686af3f297c7717b42c7e9be45afa1cef55 |
| Quinn, 8 samples | 3,511 of 9,600 | 91d00353c686a60773e6a8be3ffce86647dddae88790e79c0ff4cc525b493d01 |
| Grace, 8 samples | 2,289 of 9,600 | dc8103a968228050690e5d53e2646219c9388b84008e0f27e2c62209cc1236fa |

About 1.49 million tokens were generated in total, against a cap of 40 million.

## What this does not show

- Anything about colonies working together: every number above is one member answering alone, or an offline combination of those answers.
- Real-world skill: the tasks are synthetic.
- Thinking modes, other quantisations and Falcon-H1: those arms were trimmed before the freeze.
- Whether a trained decision-maker can capture the headroom: only the frozen arms were tested.

## Next

A second casting adds five more founding members (COLONY.md) on a fresh sealed set, and targeted fine-tuning for the members that need it, each preregistered and committed before its sealed run. Season 1 then asks whether a colony policy can capture the 7.8-point headroom at equal compute.
