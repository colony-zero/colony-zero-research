# EXP-CZ-003a results: the colony router against the dev-selected best member

Status: REPORTED and REVEALED 2026-10-29. Sealed set 4 and its salt are revealed and retired (../../public-commitments/reveal/EXP-CZ-003a/). The design was frozen before any sealed run, publicly committed before those runs, and anchored in Bitcoin block 973489. The post-run record was committed before scoring and anchored in block 973627. Sealed set 4 contains 3,581 scored tasks.

Read first. This is selection evidence, not collaboration evidence: a router chooses one member's answer per task. A1 is a fixed per-family lookup rule: it maps the known synthetic task-family label to one selected member. A3 takes four samples from that same selected member, followed by self-consistency voting. The comparator was Quinn teacher-taught, chosen before the sealed run from development tasks alone. It also turned out to be the strongest individual member on sealed set 4.

## Outcome

- H3a.1 is SUPPORTED. A1, the `rules_family_full` router, solved 96.5% of 3,581 sealed tasks, against 87.5% for C0, the dev-chosen best single member. The gain is 9.0 points; its one-sided 95% lower bound is 8.2 points, above the 5-point margin. A1's all-in FLOP proxy was slightly lower than C0's.
- H3a.2 is SUPPORTED. On this sealed set, the full-pool rule scored 36.6 points above the founders-only rule; the added members it selected were trained variants.
- H3a.3 is SUPPORTED. At four samples per task, four samples from the selected member followed by self-consistency voting beat comparator voting alone by 8.9 points, with a lower all-in FLOP proxy.
- H3a.4 is formally INCONCLUSIVE under a post-scoring interpretation of an underspecified power rule. No valid learned-router arm met the registered gate: kNN and logistic each solved 96.7%, 0.17 points above A1, far short of the 2-point margin; their all-in FLOP proxies were higher. Their bootstrap upper limits are only +0.5 points over A1, so the valid-arm intervals exclude the registered gain. Laya zero-shot solved 40.9%. The fine-tuned arm was void and produced no result. This is not ordinary sample-size uncertainty: the post-scoring power calculation used alternatives chosen after scoring, and some were impossible at the observed discordance. The frozen scorer printed NOT SUPPORTED because it did not implement the power rule.

H3a.1 supports milestone M1a, selection. The stage 3 learned-router gate is INCONCLUSIVE, so its preregistered failure disposition is not triggered. As an interim operational choice outside that gate, the colony runs the rules router because no valid learned-router arm showed the registered advantage. Almost the whole A1 gain comes from `arith_chain`.

## Hypotheses

| Hypothesis | Verdict | Evidence |
|---|---|---|
| H3a.1 A1 beats C0 by more than 5 points, with all-in FLOP proxy at most C0's | SUPPORTED | 3,457 vs 3,133 solved; only A1 355, only C0 31; +9.05 points; lower bound +8.19; margin-test p = 9.0e-16; McNemar p = 7.5e-71; bootstrap 95% [+8.0, +10.1]. FLOP proxy 1.554e16 vs 1.602e16. |
| H3a.2 A1 beats A2 | SUPPORTED | 3,457 vs 2,147; only A1 1,334, only A2 24; +36.6 points; lower bound +35.2; Holm p < 1e-300; bootstrap [+35.0, +38.2]. |
| H3a.3 A3 beats C1 at four samples per task, with FLOP proxy at most C1's | SUPPORTED | 3,463 vs 3,146; only A3 327, only C1 10; +8.85 points; lower bound +8.06; Holm p = 9.9e-66; bootstrap [+7.9, +9.8]. FLOP proxy 1.876e16 vs 2.067e16. |
| H3a.4 learned router gate | INCONCLUSIVE (scorer: NOT SUPPORTED) | No valid arm meets the registered gate. Laya zero-shot is 55.9 points below kNN and logistic. Fine-tuned tests T7, T11, T14, and T15 are void, not tested. |

## Standings

| Arm | What it is | Solved | Rate [Wilson 95%] | Format rate | All-in FLOP proxy |
|---|---|---:|---|---:|---:|
| X2 | Oracle ceiling, not realizable | 3,529 | 98.55% [98.10, 98.89] | n/a | n/a |
| A3 | Rules plus self-consistency-4 | 3,463 | 96.70% [96.07, 97.24] | 100.0% | 1.876e16 |
| kNN | Learned router on base-Laya embeddings | 3,463 | 96.70% [96.07, 97.24] | 99.8% | 1.803e16 |
| logistic | Learned router on base-Laya embeddings | 3,463 | 96.70% [96.07, 97.24] | 99.7% | 1.791e16 |
| A1 | Main fixed rule, greedy | 3,457 | 96.54% [95.89, 97.09] | 99.6% | 1.554e16 |
| X1 | Fixed rule by family and difficulty, exploratory | 3,452 | 96.40% [95.74, 96.96] | 99.9% | 1.586e16 |
| C1 | Comparator plus self-consistency-4 | 3,146 | 87.85% [86.74, 88.88] | 100.0% | 2.067e16 |
| C0 | Quinn teacher-taught, greedy | 3,133 | 87.49% [86.37, 88.53] | 100.0% | 1.602e16 |
| A2 | Founders-only fixed rule | 2,147 | 59.96% [58.34, 61.55] | 99.4% | 1.545e16 |
| Laya zero-shot | Yes/no learned router | 1,463 | 40.85% [39.26, 42.47] | 83.6% | 5.691e16 |
| C2 | Random router, seed 0 | 1,351 | 37.73% [36.15, 39.33] | 82.4% | 1.519e16 |
| Laya fine-tuned | Learned router | void | void | void | void |

kNN and logistic files were byte-identical across seeds 0 through 4, so all five seeds had the same result. Laya zero-shot had one seed by design. Laya fine-tuned was void.

## H3a.4 tests

| Test | Learned router vs A1 | Margin | Solved (learned / A1) | Only learned / only A1 | Lower bound | FLOP condition | Holm p |
|---|---|---:|---|---|---:|---|---:|
| T4 | kNN | +2 points | 3,463 / 3,457 | 19 / 13 | -0.10 points | n/a | 1 |
| T5 | logistic | +2 points | 3,463 / 3,457 | 14 / 8 | -0.06 points | n/a | 1 |
| T6 | Laya zero-shot | +2 points | 1,463 / 3,457 | 21 / 2,015 | -57.1 points | n/a | 1 |
| T7 | Laya fine-tuned | +2 points | void, not tested | n/a | n/a | n/a | n/a |
| T8 | kNN | -1 point | as T4 | | -0.10 points | not met: 1.16 x A1 | 1 |
| T9 | logistic | -1 point | as T5 | | -0.06 points | not met: 1.15 x A1 | 1 |
| T10 | Laya zero-shot | -1 point | as T6 | | -57.1 points | not met: 3.66 x A1 | 1 |
| T11 | Laya fine-tuned | -1 point | void, not tested | n/a | n/a | n/a | n/a |
| T12 | Laya zero-shot vs kNN | 0 points | 1,463 / 3,463 | 12 / 2,012 | -57.2 points | n/a | 1 |
| T13 | Laya zero-shot vs logistic | 0 points | 1,463 / 3,463 | 13 / 2,013 | -57.2 points | n/a | 1 |
| T14, T15 | Laya fine-tuned vs kNN, logistic | 0 points | void, not tested | n/a | n/a | n/a | n/a |

The all-in FLOP proxy includes shared development work. The shared charge alone exceeded 90% of A1's total, so no learned router could meet the preregistered 10% reduction condition. This proxy is not measured energy, time, or money. The frozen scorer uses `1` as an internal placeholder for a void test; it is not a p-value and is shown as `n/a` above. The fine-tuned arm could not have made H3a.4 supported: the oracle is only 2.01 points above A1, and even a best-case recovery could not clear the +2-point lower-bound margin.

### Low-power reading for H3a.4

The power rule used the frozen decision rule, 20,000 multinomial draws, seed 0, and the alternatives in the preregistration's power table. It reproduced that table at 0.74 and 0.89, against planned values of 0.75 and 0.90. The rule did not name an alternative, so using the preregistration's own alternatives was a post-scoring choice recorded as deviation 6.

| Test | Comparison | Observed discordance | Alternative | Power |
|---|---|---:|---|---:|
| T4 | kNN vs A1, +2-point margin | 0.89% | 3-point gain, impossible below 3% discordance | 0 |
| T5 | logistic vs A1, +2-point margin | 0.61% | 3-point gain, impossible | 0 |
| T6 | Laya zero-shot vs A1, +2-point margin | 56.9% | 3-point gain | 0.05 |
| T8, T9, T10 | kNN, logistic, Laya zero-shot vs A1, non-inferiority | as above | no difference | 0 |
| T12 | Laya zero-shot vs kNN | 56.5% | 2-point gain; 1-point gain | 0.26; 0.08 |
| T13 | Laya zero-shot vs logistic | 56.6% | 2-point gain; 1-point gain | 0.26; 0.08 |
| T7, T11, T14, T15 | Laya fine-tuned | void, not tested | n/a | n/a |

Any reading gives near-zero power for part (a) because the oracle is only 2.01 points above A1. The data still rule out the registered effects: kNN and logistic have bootstrap upper limits of +0.5 points over A1, and Laya zero-shot trails kNN and logistic by at least 54 points.

## Where the gain comes from

| Family | n | C0 | A1 | A2 | C1 | A3 | kNN | logistic | X2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| arith_chain | 894 | 537 | 861 | 718 | 566 | 884 | 872 | 867 | 894 |
| graph_reach | 897 | 896 | 896 | 712 | 897 | 896 | 896 | 896 | 897 |
| json_extract | 893 | 850 | 850 | 615 | 848 | 848 | 850 | 850 | 857 |
| list_transform | 897 | 850 | 850 | 102 | 835 | 835 | 845 | 850 | 881 |

A1 and C0 used the same answers on JSON extraction and list transforms. A1's full 324-task gain came from arithmetic: 861 against 537. On arithmetic, Quinn teacher-taught solved 60.1% and Quentin self-taught solved 96.3%.

The comparator was also the strongest member on sealed set 4: 87.5%, ahead of Quinn self-taught at 82.4% and Quentin self-taught and Quentin teacher-taught at 61.7% each. No founder solved more than 11.4% of list transforms, which is why A2 had 102 of 897 there.

Leave-one-out results are descriptive. Removing Quinn teacher-taught cost 11.4 points, bootstrap interval [-12.5, -10.3]. Removing Quentin self-taught cost 0.4 points, [-0.9, 0.0], because Quinn self-taught then took arithmetic at 94.6%. Removing Quentin teacher-taught changed nothing important: Grace teacher-taught took graph reachability and gained one task. Quentin teacher-taught is therefore the elimination candidate, with the full pool as its no-elimination twin. The other 24 members were never selected by A1.

## Deployment and secondary measures

Every sealed run stayed within its own memory limit. The deployment probe for the three simultaneous A1 servers did not: it used 2.80 GB above a 13.46 GB baseline, against a 1.47 GB limit, and peaked at 16.26 GB. About 11.3 GB of the 16 GB consumer GPU was already occupied when the probe began; the cause was not identified. A screen-capture program was open with a preview during sealed runs, but its memory share was not measured. Therefore this experiment does not show deployment feasibility for A1. The same 2.80 GB would fit at the sealed-run baseline, but that configuration was not measured.

The largest single sealed-run usage was 2.63 GB for Sam untrained, against a 12.74 GB limit. The sealed-run baselines were 2.18 to 2.19 GB. The screen-capture program cannot be ruled in or out as part of the deployment-probe cause, and it does not affect any solve rate.

| Arm | Member tokens/task | Router tokens/task | Marginal FLOP proxy | Member tasks/hour | Router CPU seconds/task |
|---|---:|---:|---:|---:|---:|
| C0 | 273.3 | 0.0 | 1.566e15 | 11,232.4 | not measured |
| A1 | 206.5 | 0.0 | 1.086e15 | 11,853.5 | not measured |
| A2 | 211.0 | 0.0 | 9.939e14 | 45,098.3 | not measured |
| C1 | 1,083.5 | 0.0 | 6.208e15 | 4,097.1 | not measured |
| A3 | 818.6 | 0.0 | 4.299e15 | 4,503.8 | not measured |
| kNN | 251.5 | 100.0 | 1.671e15 | 10,238.5 | 1.203 |
| logistic | 236.9 | 100.0 | 1.556e15 | 10,617.5 | 1.203 |
| Laya zero-shot | 214.6 | 13,824.0 | 4.246e16 | 11,169.3 | 29.122 |

Tasks per hour for routed arms are estimates, apportioned from member-run wall time by output tokens. Only C0 and C1 are direct measurements. Rule-router time was not separately measured.

## Route records

The bound route program wrote seven records: base-Laya embeddings for all 3,581 sealed prompts, one Laya zero-shot record, and five Laya fine-tuned records. The scorer reproduced every embedding record task and a 360-task zero-shot sample selected by the hash of block 973633. Both checks passed. The sample-id SHA-256 was `34f1b0e7...`. Fine-tuned records were not checked because their artifacts failed the binding check first.

## Deviations from the preregistration

No frozen file was edited.

1. Route records and scoring called the integrity gate without the experiment folder it needs. Each ran unchanged with a wrapper that supplies the folder; the gate then runs in full. This was committed before either step produced output.
2. Route records stopped at the first record because a delete of a file that did not yet exist reported failure. A wrapper forced only that delete to report success. This could mask a failed deletion. The routes folder was empty before launch, and the bound script checked that every new record existed after writing it.
3. The post-run hash command was garbled by shell quoting and exceeded the command-line limit. A wrapper sent the same SHA-256 loop intact from the results folder with relative paths. The deviation was committed before the post-run record existed; three record lines matched direct hashes.
4. At scoring, loading each fine-tuned seed rewrote one small tokenizer file, so the scorer correctly voided the arm. Restoring that file in a copy reproduced the bound hash for all five seeds. The weights and every other file were unchanged. The owner chose to report the arm as void, with no re-score.
5. At review, several registered reported-only outputs were absent from the frozen scorer: per-cell accuracy, bootstrap intervals, format rates, leave-one-out contributions, peak memory, and secondary compute. A new unbound script computed them after scoring and rebuilt every arm's counts exactly, except the void arm. These outputs decide nothing.
6. At review, the frozen scorer was found not to implement the SPEC power rule. It labelled H3a.4 NOT SUPPORTED. The rule was applied after scoring using the SPEC power-table alternatives. Every failed H3a.4 test had power of 26% or less. The reported verdict is INCONCLUSIVE, with the scorer's label shown. H3a.1 through H3a.3 are unaffected.

Exact McNemar p-values that the scorer printed as 0 because of floating-point underflow were retained in the internal appendix. Deviations 1 through 3 were summarized publicly with the post-run record before scoring.

## What this does not show

- Generalisation beyond four synthetic task families, one sealed set, and the registered templates and decoding.
- Collaboration between members. This router only selects an answer.
- That learned routers have no value in another pool or where fixed rules leave more headroom.
- Whether the gain comes from a colony or one specialist. Here, as on sealed set 2, it comes almost entirely from arithmetic and Quentin self-taught.
- Tools, repair, or verification.
- Transfer beyond Forge v0.0.2 task families. This is not evidence of general intelligence, AGI, or parity with frontier models.
- Whether a cost-aware learned router could save compute. No arm optimized cost.
- Whether members can be retrained on a 16 GB consumer GPU to the same result. Each trained member was trained once.
- Deployment feasibility. The deployment probe did not pass.
- Freedom from contamination beyond the checks performed. Nineteen of 3,600 tasks with an exact or canonical prompt collision were excluded, and task-id collision audit found none. The checks do not detect semantic overlap or prior exposure to the templates.
- Every zero-shot route-record line. Only the 360-task beacon-selected sample was reproduced; the other 3,221 lines were not.
- What a model or adapter does on its own. Results belong to a frozen member-plus-template system, not weights or adapter alone.
- Other settings. Every member ran at Q8_0 with bound decoding; router and comparator selection used development tasks 0 through 399, with one sealed set and one greedy pass.
- The fine-tuned Laya router's solve rate, its comparison with other learned routers, or its placement among them.
