# EXP-CZ-001: Small-model baseline

Run status: FREEZE PENDING. No sealed task has been run. The thresholds below are the ones frozen in the design and become binding when the freeze commitment root is published (see ../../public-commitments/EXP-CZ-001.md).

## Question

What can one frozen tiny model solve, without tools, when every answer is checked by an exact independent verifier?

## Hypotheses

Each can fail.

- H1.1 At least one tested model reaches a lower 95 percent Wilson bound of 0.25 on the sealed suite with greedy decoding and at least 0.90 format validity.
- H1.2 The strict small-weight model (Granite-4.0-H-350M) clears the same bar. If it does not, "this weight class is too small for the suite" is the recorded result.
- H1.3 Model rank by verified solve rate matches rank by the vendors' published instruction-following scores. A mismatch is reported, not explained away.

## Arms

| Arm | Model | Notes |
|---|---|---|
| M1 | SmolLM2-360M-Instruct | Floor control |
| M2 | Granite-4.0-H-350M | Strict small-weight track |
| M3 | Qwen3-0.6B | No-think and think modes as separate arms |
| M4 | Qwen3.5-0.8B | No-think and think modes as separate arms |
| M5 | Falcon-H1-0.5B-Instruct | Only after its licence is read and approved |

Weights are official releases, converted without modification to a common inference format, with every file hash recorded. Primary quantisation is 8-bit for all arms. A 4-bit arm for M2 and M3 tests quantisation sensitivity. One inference server runs at a time, on one pinned build, with a 4,096-token context and greedy decoding with a fixed seed.

Prompts: four fixed templates (plain, two worked examples, plain plus a format line, step-by-step). The template for each model is chosen on the dev split only, written down, and frozen before the sealed run.

Sampling arm: eight samples at temperature 0.7 per sealed task, used for coverage@8 (an upper bound, because it uses oracle selection) and as input to EXP-CZ-002.

Baselines: constant-answer and most-common-answer baselines per family, a random-text baseline, and a reference program that solves every task as a 100 percent ceiling. The ceiling shows the tasks are solvable by code, so this experiment measures language competence without tools.

Task suite: four machine-checked families (arithmetic chains, graph reachability, JSON extraction, list transforms), difficulties 1 to 5, equal counts. Dev 400 (public), test 800 (public), sealed 1,200 (300 per family), generated from a secret salt.

## Endpoints

- E1 (primary): verified solve rate on the sealed suite, greedy, with a Wilson 95 percent interval, overall and per family and difficulty.
- E2: format validity (the answer parses in the required shape), reported separately from correctness.
- E3: verified solves per million all-in tokens, plus the FLOP proxy.
- E4: coverage@8 on the sealed suite.
- E5: resource profile: weight file size, peak resident memory, decode speed at 1 and 8 concurrent sequences.
- Pairwise: exact McNemar on paired sealed tasks for all model pairs, Holm-adjusted at 0.05.

## Decision rules

- R1 (viable): the lower Wilson bound of E1 is at least 0.25, E2 is at least 0.90, and E1 is above the upper bound of the best trivial baseline.
- R2 (strict class): if M2 and M1 both fail R1, record "the strict small-weight class is too small for this suite". The track stays as a failure baseline.
- R3 (working backbone): among arms that meet R1, choose the highest E3. If intervals overlap, prefer plain attention, Apache-2.0 and lower peak memory.
- R4 (suite validity): if all models score above 95 percent or below 5 percent on a family, that family is rescaled in a versioned suite before any claim is made.

## Procedure

1. Phase 0, capacity probe on 50 dev tasks per model. Check: throughput and memory recorded, and projected tokens within the cap, otherwise halt.
2. Phase 1, template selection on the dev split. Check: chosen template per model and its dev score are written to the manifest.
3. Phase 2, freeze. Write the manifest, compute the field commitments, publish the commitment root and the salt commitment. Check: a test reveal verifies, and the root is public before step 4.
4. Phase 3, sealed run, one ledger per arm. Check: each ledger verifies and replay equals the live state.
5. Phase 4, run the preregistered analysis. Check: results regenerate bit for bit from the ledgers.
6. Phase 5, write the report with deviations and "what this does not show". Negative outcomes are reported the same way as positive ones.

Cap: 40M generated tokens and 24 wall-hours on one slot. Stop and ask if a phase projects past twice its Phase 0 estimate.

## Deviations before the freeze

No sealed task was touched for any of these.

1. 2026-10-24. The checker was revised so that yes/no answers ignore case and one trailing period, and answers of the wrong shape are reported as format failures. Reason: Phase 0 showed every member scored 0 on graph reachability because "No" was rejected, which measured capitalization.
2. 2026-10-24. The checker was revised again to allow step-by-step reasoning, grading the value after the last "Answer:" line, and the step-by-step template was added. Reason: Phase 1 showed arithmetic near 0 for every member because a bare-answer rule forbade working. Reasoning tokens are charged in E3.
3. Phase 1 results for the first three templates were re-scored offline from their recorded answers. No model was re-run for them.
4. The task suite was rescaled from version 0.0.1 to 0.0.2 after Phase 1 (one family below 5 percent for every member, one at the guessing baseline), and the output cap was set to 512 tokens for every arm. Phase 1 v2 reran template selection on the new suite. See RESULTS_SO_FAR.md.

## Exploratory arms: Laya decision arms

Laya (convaiinnovations/laya, Apache-2.0) is an open encoder model. We will use it in two roles: as a router, deciding which member answers, and as a judge, deciding which answer the colony submits. Both are scored offline on logged outcomes against the best single member, per-family rules, majority vote and equal-compute self-consistency. These arms are exploratory. They never change the confirmatory standings or any decision rule above.

## What this cannot tell you

- Synthetic tasks may not predict real-task performance.
- Vendor chat templates and thinking modes change outputs. They are arms, not noise.
- A strong score here says nothing about collective behavior (EXP-CZ-002) or learning (EXP-CZ-004).
- One build of one runtime. Results may shift with a different quantiser or sampler.
