# EXP-CZ-003a: The colony router against the best single member

This is a reader summary written after the run. It describes the frozen preregistration rather than a file published before the run. The frozen records that predate the run are the [manifest](../../public-commitments/reveal/EXP-CZ-003a/manifest.json), [freeze ledger](../../public-commitments/reveal/EXP-CZ-003a/freeze.jsonl), [freeze record](../../public-commitments/EXP-CZ-003a-freeze.txt), its [timestamp proof](../../public-commitments/EXP-CZ-003a-freeze.txt.ots), and [pre-run commit a6ea353](https://github.com/colony-zero/colony-zero-research/commit/a6ea353).

Run status: Reported 2026-10-29 (RESULTS.md). The design was frozen before sealed set 4 was generated. The freeze record was publicly committed before any sealed run; its proof is anchored in Bitcoin block 973489, mined 2026-10-28T03:10:30Z.

## Question

On fresh sealed tasks, can a router fitted on development data choose colony members well enough to beat the best single member at equal compute? Do trained members add value beyond the founders? Can a learned router beat fixed rules?

This is selection evidence, not collaboration evidence. The router chooses one member's answer for each task.

## Design

The pool has 27 frozen members: nine untrained founders, eight self-taught variants, eight teacher-taught variants, and two children, Theo and Hazel. Graham is included only as an untrained founder because his adapters failed their earlier parity gates. Every member uses its frozen template, settings, and recorded artifact identity.

All routers and the comparator were fitted or selected on development tasks 0 through 399 before sealed set 4 existed. The comparator was Quinn teacher-taught, selected by most development solves, then fewer format failures, then name: 354 of 400 solves and no format failures.

Sealed set 4 began with 3,600 new tasks. Nineteen prompt collisions with public or earlier prompts were excluded before any run, leaving 3,581 scored tasks. Every pool member answered every task once greedily. The comparator and the members used by the main router also answered four sampled versions per task for the self-consistency arms. Routed and voted arms were computed offline from those ledgers, so they used the same answer pool.

## Arms

| Arm | Role | Calls per task |
|---|---|---:|
| C0 | Best single member, Quinn teacher-taught, greedy | 1 |
| A1 | Main fixed rule, `rules_family_full`, greedy | 1 |
| A2 | Founders-only fixed-rule control | 1 |
| C1 | Best single member with self-consistency-4 | 4 |
| A3 | Main fixed rule with self-consistency-4 | 4 |
| C2 | Random router over 27 members, five fixed seeds, reported only | 1 |
| L1, L2 | kNN and logistic learned routers | 1 |
| L3 | Laya zero-shot learned router | 1 |
| L4 | Laya fine-tuned learned router | 1 |
| X1 | Fixed rule per family and difficulty, exploratory | 1 |
| X2 | Oracle ceiling, not realizable | n/a |

The main rule chose Quentin self-taught for arithmetic, Quentin teacher-taught for graph reachability, and Quinn teacher-taught for JSON extraction and list transforms. The founders-only rule used Graham for arithmetic, Quinn for graph reachability and JSON extraction, and Grace for list transforms.

## Hypotheses and margins

| ID | Hypothesis | Success rule |
|---|---|---|
| H3a.1 | A1 beats C0 | One-sided 95% lower bound of A1 minus C0 above +5 points, with A1 all-in FLOP proxy no higher than C0's |
| H3a.2 | A1 beats A2 | Lower bound above 0 after Holm adjustment; tested only if H3a.1 succeeds |
| H3a.3 | A3 beats C1 at four samples per task | Lower bound above 0 after Holm adjustment, with A3 all-in FLOP proxy no higher than C1's; tested only if H3a.1 succeeds |
| H3a.4 | A learned router beats rules | (a) beats A1 by at least 2 points, or is within 1 point at no more than 90% of A1's all-in FLOP proxy, and (b) Laya zero-shot or fine-tuned beats kNN or logistic |

The H3a.4 non-inferiority branch is not an equivalence test. If H3a.4 fails, the preregistered disposition was to keep rules and drop learned controllers. H3a.4 is a separate family and is tested whether or not H3a.1 succeeds.

## Statistics and power

The decision statistic is the one-sided 95% Newcombe method 10 lower bound for paired proportions. Exact two-sided McNemar, paired bootstrap intervals, and Wilson intervals are secondary and never decide a hypothesis. F1 tests H3a.1 at 0.05, then applies Holm over H3a.2 and H3a.3 if H3a.1 succeeds. F2 applies Holm within H3a.4 part (a) and part (b). There is no adjustment across F1 and F2 because they answer different preregistered questions.

kNN, logistic, and fine-tuned Laya each use seeds 0 through 4. Every seed must pass for a learned-router test to pass; the reported bound is the smallest seed bound and the p-value the largest seed p-value. Zero-shot Laya is run once because it has no fitted parameters.

The power plan used 3,600 tasks. At a 3-point gain, 4% discordance, and 94% both-correct, simulated power was 0.75 for the +2-point learned-router comparison. At a 1-point gain, 3% discordance, and 95% both-correct, simulated power was 0.90 for the Laya comparison. A non-void failed H3a.4 test with simulated power below 50% at its observed discordance is reported as INCONCLUSIVE rather than as no effect. The frozen rule did not say which alternative effect to simulate. That choice was made after scoring (the alternatives of the power table above), which is deviation 6 in RESULTS.md.

## Compute and failure criteria

All-in compute is a preregistered FLOP proxy: 2 times parameters times tokens for inference and 6 times parameters times tokens for training. It includes shared development work for every arm, plus that arm's router work and sealed inference. It is not measured energy, time, or money.

A run is void and reported if its ledger or inputs fail verification; its task, model, template, route record, or program differs from the committed design; its decoding differs from the registered settings; it uses more than one serving slot or more than one adapter; or it lacks a verdict for a task. A learned-router configuration outside the frozen components and job matrix is void. The fine-tuned arm's outcome does not change the other hypotheses.

## What this cannot tell you

- Whether routing works beyond these four synthetic task families or under other decoding, templates, or member pools.
- Whether this is collaboration. The router selects one answer; members do not reason together.
- Whether a learned router has no value in a pool with more headroom above fixed rules.
- Whether the all-in FLOP proxy measures energy, latency, cost, or real deployment performance.
- Whether the main router can be deployed simultaneously. The experiment separately tests that claim.
