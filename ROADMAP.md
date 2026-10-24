# Roadmap

Every item here is PROPOSED unless it says otherwise. Thresholds are preregistered design choices, not predictions. Budgets are caps, not estimates. A stage starts only after the previous gate's decision is recorded, including a negative one.

## Ground rules for every experiment

- A preregistered manifest and field commitments exist before any sealed evaluation.
- Frozen weights are hashed. Task generators are deterministic. Held-out tasks are sealed. An independent exact checker grades every answer.
- Compute accounting is complete, including the cost of any controller or verifier.
- Anything that evolves or learns runs with at least five seeds, and run-to-run spread is reported.
- Pairwise tests use exact McNemar on paired tasks with Holm adjustment. Intervals are Wilson and paired bootstrap.
- Negative results use the same report template as positive ones.
- No uncontrolled self-modification and no continuous workload. Each run is a bounded job with a token cap.

## Seasons

Each season is one turn of the colony loop: casting or birth, trials, Council, measured elimination, next generation. The first Council runs in Season 1 as an experimental arm. Its votes are predictions, measured contribution decides, and a no-elimination twin is the control.

| Season | Generation | Experiments | Decision the season makes |
|---|---|---|---|
| 0 The Casting | Gen 0 | EXP-CZ-001 | Founding standings on sealed tasks |
| 1 The First Colony | Gen 0 | EXP-CZ-002 plus Council arm | First elimination. Does the colony beat its best member? |
| 2 Who Does What | Gen 0 | EXP-CZ-003 | Routing policy for the colony |
| 3 Inheritance | Gen 1 | EXP-CZ-004, EXP-CZ-005 | First generational replacement through the promotion gate |
| 4 Invention | Gen 2+ | EXP-CZ-006 | A colony-built component enters only if it beats established ones |
| 5 The Gap | Gen N | EXP-CZ-007 | Fraction of the gap to a frozen frontier model |
| 6 and on | Gen N+1 | promotion gate each generation | Stop rule: three consecutive generations fail promotion. Then the one-use Final Exam places the colony on the Climb |

## Experiments

| Stage | Experiment | Question | Primary endpoint | Success gate | If it fails |
|---|---|---|---|---|---|
| 1 | EXP-CZ-001 | What can one frozen tiny model solve, objectively verified? | Verified solve rate on sealed tasks, greedy decoding | See experiments/EXP-CZ-001/PREREGISTRATION.md | No member clears the viability gate: the class is too weak for this suite. Test a larger size lane as a disclosed control or change the suite |
| 2 | EXP-CZ-002 | At identical total tokens, does a small team beat one model and best-of-N? | Verified solve rate at equal tokens, budgets 1x to 8x | Team beats the best non-oracle best-of-N by at least 3 points with the Holm-adjusted interval above zero in one regime, and is not worse in the other | Record "no amplification found for this class" and stop the social line |
| 3 | EXP-CZ-003 | Does a learned router improve success per unit of compute? | Verified solves per all-in compute | A learned router beats rules by at least 2 points or cuts compute by 10 percent at equal solve rate | Ship rules and drop learned controllers |
| 4 | EXP-CZ-004 | Do verified skills transfer to unseen problems and across models? | Held-out solve delta, five seeds | Gain exceeds seed spread on unseen families and survives a change of model family | Stop skill claims and publish the null |
| 5 | EXP-CZ-005 | Does a descendant beat its predecessor? | Promotion gate on sealed tasks with a protected regression suite | Gate passes in at least four of five seeds | A fresh candidate or a simple fine-tuning control matches it: evolution adds nothing here |
| 6 | EXP-CZ-006 | Can the population produce a new testable component that beats established ones? | Held-out solve rate at equal compute | Beats a hand-built module and random search over five seeds, then an independent replication | No invention claim |
| 7 | EXP-CZ-007 | How much of the gap to a frozen frontier baseline closes? | Fraction of the gap closed, with interval | Lower bound above zero | Report the interval, including zero |
| 8 | EXP-CZ-008 | Can a swarm compress into one student? | Held-out solve rate of the student | Student beats the fine-tuning control | The swarm adds no distillable signal |

If EXP-CZ-002 is negative, the project becomes an evaluation harness plus skill and routing work. If EXP-CZ-003 is negative, the colony keeps a rules router. If EXP-CZ-004 and EXP-CZ-005 are negative, the earlier findings stand and the lineage story is dropped. EXP-CZ-006 and EXP-CZ-007 run only if their prerequisites are positive.

## The Climb

A public ladder with ten rungs. Every rung is PROPOSED. Placement uses a calibrated item bank on one latent scale.

| Rung | Name | Claim it supports | Pass criterion in short |
|---|---|---|---|
| 1 | Floor | Members are above chance on the instrument | 95 percent interval above chance in at least 4 families |
| 2 | Beat your best member | Coordination adds something beyond voting | Beats the best member and majority vote, with an interval excluding zero on at least 3 families |
| 3 | Beat a dense twin | The population is competitive per unit of compute | Ahead of one dense model of equal parameters and compute on the pooled scale |
| 4 | Transfer | Generalizes within a stated distribution | At least 8 families authored after the freeze, above threshold on half |
| 5 | Adapt | Learns new families faster | Reaches threshold in fewer examples on at least 5 families |
| 6 | Public floor | Standing in the small-model class | Beats the best published sub-1B model on two external benchmarks |
| 7 | Place on the scale | A number comparable to reference models | Placement interval narrower than the gap to the nearest reference |
| 8 | Bounded parity | Parity in two verifiable domains under a stated budget | Win-rate interval includes or exceeds 50 percent against a named model |
| 9 | Horizon | Long-task completion on a small suite | 50 percent time horizon with interval, against a reference |
| 10 | Breadth parity | Matches a named, dated frozen model on this bank only | At least 25 held-out families, within the reference's interval on 80 percent of them, independently reproduced |

The top rung does not mean human-level breadth, safety or reliability, or parity with any newer model. It means what the table says and no more.

Falsification clock: rung 2 must be cleared by a season named in advance. If it is not, the season report says "not found" and the program changes course in public.

## Deferred

Culture and institutions beyond the Council, any continuous broadcast, per-agent adapters, original architectures, and colonies of 32 or 100 members. Members are added only when a verified marginal value is shown.
