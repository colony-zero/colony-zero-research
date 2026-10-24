# Colony Zero

A colony of tiny, different open models competes on fresh, machine-checked problems. The members hold a Council vote on who contributes least. The colony is then re-run without each member, and the member that measurably contributes least is eliminated. Survivors breed a next generation, and a newcomer joins only if it beats its parent on a sealed test. This repeats until three generations in a row fail promotion. Then a one-time Final Exam places the colony on the Climb, a public ten-rung ladder.

Created and directed by Christopher Ayers.

We make no claim of general intelligence. The top rung of the Climb is a narrowly defined benchmark result that must be independently replicated, and any report of it will name exactly what was measured.

This repository is the public research record. It holds the question, the high-level design, preregistrations, commitments and results. Implementation code is not published here.

## The idea

Most AI progress comes from making one model bigger. Colony Zero asks the opposite question: what happens when many small, different models work on problems together, judge each other, and are replaced generation after generation by offspring that must prove themselves?

Each season is one turn of the same loop, and each turn is also an experiment.

1. Casting. A founding generation of different model families enters the colony.
2. Trials. The colony works on fresh problems that a machine checker can grade exactly. The sealed problems are not disclosed or used for any tuning before the run, and a published commitment makes any later change detectable.
3. Council. Members vote on who contributes least. Each vote is a prediction, scored later.
4. Elimination. The member that measurably contributes least is removed. A twin colony with no elimination runs alongside as the control.
5. Next generation. Survivors produce offspring. An offspring enters only if it beats its parent on a sealed promotion test.
6. Repeat.

The colony is finished when it stops improving: three generations in a row fail promotion. A one-time Final Exam, drawn from a public random value that does not exist until after the colony is frozen, then places it on the Climb (see ROADMAP.md). If it tops out low, that ceiling is the result.

## The founding colony (Generation 0)

| Member | Family | Size | Licence | Observed so far (dev split only) |
|---|---|---|---|---|
| Granite-4.0-H-350M | IBM, hybrid Mamba | 340M | Apache-2.0 | Follows the answer format: 0 of 400 dev answers failed on format |
| SmolLM2-360M-Instruct | Hugging Face | 362M | Apache-2.0 | The floor control: lowest dev score |
| Qwen3-0.6B | Alibaba Qwen | 600M | Apache-2.0 | Writes step-by-step prose even when asked for a bare answer |
| Qwen3.5-0.8B | Alibaba Qwen, hybrid DeltaNet | 800M | Apache-2.0 | Highest dev score: 175 of 400 |

## Where we are

Every row carries one tag: PROPOSED (designed, not built or tested), IMPLEMENTED (built and tested, no result claimed), MEASURED (a result exists, with evidence linked), REJECTED (tried or considered, and set aside for a stated reason).

| Item | Tag | Evidence |
|---|---|---|
| Hash-chained ledger that records every model call and can be replayed and re-verified | IMPLEMENTED | METHODOLOGY.md |
| Salted commitments to sealed task sets and to preregistration fields | IMPLEMENTED | public-commitments/EXP-CZ-001.md |
| Capacity probe of the four founding members | MEASURED | experiments/EXP-CZ-001/RESULTS_SO_FAR.md, Phase 0 |
| Best prompt template per member, chosen on the dev split | MEASURED | experiments/EXP-CZ-001/RESULTS_SO_FAR.md, Phase 1 v2 |
| Task suite version 0.0.1 as a measuring instrument | REJECTED | One family scored under 5 percent for every member and another sat at the guessing baseline; see Phase 1 |
| Sealed run of EXP-CZ-001 and first standings | PROPOSED | experiments/EXP-CZ-001/PREREGISTRATION.md, freeze pending |
| Elimination by popularity vote | REJECTED | METHODOLOGY.md: votes are predictions, measurement decides |
| First Council and first measured elimination | PROPOSED | ROADMAP.md, Season 1 |
| Randomized crowd-vote arm | PROPOSED | METHODOLOGY.md |
| A generation replaced by offspring that beat their parents | PROPOSED | ROADMAP.md, Season 3 |
| The colony reaching the top rung of the Climb | PROPOSED | ROADMAP.md |

No season has been completed. No member has been eliminated. All numbers published so far are dev-split numbers, and dev results are not sealed results.

## Seasons

| Season | Generation | The question | Experiment |
|---|---|---|---|
| 0 The Casting | Gen 0 | What can each founding member solve alone? | EXP-CZ-001 |
| 1 The First Colony | Gen 0 | Does the colony beat its best member and best-of-N at equal compute? First Council and elimination | EXP-CZ-002 plus the Council arm |
| 2 Who Does What | Gen 0 | Does a learned router send each problem to the right member? | EXP-CZ-003 |
| 3 Inheritance | Gen 1 | Do skills transfer, and does a child beat its parent? | EXP-CZ-004, EXP-CZ-005 |
| 4 Invention | Gen 2+ | Can the colony build a new component that beats established ones? | EXP-CZ-006 |
| 5 The Gap | Gen N | How much of the gap to a frozen frontier model has the colony closed? | EXP-CZ-007 |
| 6 and on | Gen N+1 | Keep breeding until three generations in a row fail to improve | promotion gate, Final Exam |

## How we keep it honest

1. Every model call, vote and verdict goes into a hash-chained ledger that anyone can replay and verify.
2. Sealed problems come from a secret salt. We publish a commitment to the salt and to the task file before any run, and reveal them after.
3. Votes never decide by themselves. Measured contribution decides, and every elimination run has a no-elimination twin as a control.
4. Public votes steer a randomized share of the research, never all of it, so their effect can be measured.
5. Decision rules are written down before the run. Negative results are published the same way as positive ones.
6. Every capability statement carries one tag, and a MEASURED statement points to its evidence.
7. Prior art is acknowledged in PRIOR_ART.md for every mechanism that has a close predecessor.
8. No result is called general intelligence. Climb results are reported as the defined benchmark measurements they are, and the top rungs need independent replication.

## Hardware

Everything runs on a single consumer GPU. Members share base models and take turns, so a colony does not need one loaded model per member.

## Files

| Path | What |
|---|---|
| ROADMAP.md | Seasons, experiments and the Climb |
| METHODOLOGY.md | How the evidence is produced and protected |
| experiments/README.md | Index of experiments and their status |
| experiments/EXP-CZ-001/PREREGISTRATION.md | The first experiment, as designed before the sealed run |
| experiments/EXP-CZ-001/RESULTS_SO_FAR.md | Dev-split measurements to date |
| public-commitments/ | Commitments and how to verify them |
| PRIOR_ART.md | Related published work |
| CITATION.cff, NOTICE.md | Citation data and rights notice |

## Credit

Colony Zero was conceived, designed and is directed by Christopher Ayers. Cite it with CITATION.cff. See NOTICE.md for the rights notice.
