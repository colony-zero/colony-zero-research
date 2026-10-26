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

Every member has a name, so the colony can be followed season after season. The full registry is COLONY.md.

| Name | Model | Lab, architecture | Size | Sealed result, untrained (set 1 / set 2) |
|---|---|---|---|---|
| Quinn | Qwen3.5-0.8B | Alibaba Qwen, hybrid DeltaNet | 800M | 44.8% / 42.7%; only member above guessing on graph questions |
| Quentin | Qwen3-0.6B | Alibaba Qwen, transformer | 600M | 28.6% / 29.5% |
| Grace | Granite-4.0-H-350M | IBM, hybrid Mamba | 340M | 25.1% / 23.4%; 99.8% of answers well formed |
| Sam | SmolLM2-360M-Instruct | Hugging Face, transformer | 362M | 16.3% / 15.8%; the floor control |
| Graham | Granite-4.0-350M | IBM, transformer | 352M | - / 34.5%; arithmetic specialist |
| Erin | ERNIE-4.5-0.3B | Baidu, transformer | 361M | - / 19.8% |
| Mina | MiniCPM4-0.5B | OpenBMB, transformer | 434M | - / 18.2% |
| Rowan | RWKV-7 G1d 0.4B | RWKV, recurrent | 400M | - / 12.8% |
| Bastien | Baguettotron | PleIAs, transformer | 608M | - / 6.5%; thinking mode always on |

All nine are Apache-2.0. No founder passes the viability bar (R1) untrained. With one small adapter trained on a teacher's checked answers, seven of the eight members tested pass it; with their own checked answers, four do (EXP-CZ-010, EXP-CZ-011). These gains are within four synthetic Forge task families, tested on fresh tasks from the same generators as training. The teacher comparison measures the teacher pipeline together with its larger data volume, not teacher quality alone. Each adapter was trained with one seed, below our own five-seed rule, so seed variance is unknown and these learning results are preliminary.

Generation 1 has two members, Theo and Hazel: 135M children of SmolLM2-135M-Instruct, each trained on checked answers from a different open-weight teacher. Both pass R1 on sealed set 3 (37.0% and 37.4%) and beat their parent, which solves 12.6% (EXP-CZ-017). This is within four synthetic Forge task families, tested on fresh tasks from the same generators as training. Neither teacher beat a control trained on the generator's own correct answers. Three training seeds were run with seed 0 deciding, below our five-seed rule, so this result is also preliminary on seed variance.

## Where we are

Every row carries one tag: PROPOSED (designed, not built or tested), IMPLEMENTED (built and tested, no result claimed), MEASURED (a result exists, with evidence linked), REJECTED (tried or considered, and set aside for a stated reason).

| Item | Tag | Evidence |
|---|---|---|
| Hash-chained ledger that records every model call and can be replayed and re-verified | IMPLEMENTED | METHODOLOGY.md |
| Salted commitments to sealed task sets and to preregistration fields | IMPLEMENTED | public-commitments/EXP-CZ-001.md |
| Capacity probe of the four founding members | MEASURED | experiments/EXP-CZ-001/RESULTS_SO_FAR.md, Phase 0 |
| Best prompt template per member, chosen on the dev split | MEASURED | experiments/EXP-CZ-001/RESULTS_SO_FAR.md, Phase 1 v2 |
| Task suite version 0.0.1 as a measuring instrument | REJECTED | One family scored under 5 percent for every member and another sat at the guessing baseline; see Phase 1 |
| EXP-CZ-001 design frozen and committed before the sealed run | IMPLEMENTED | public-commitments/EXP-CZ-001.md, root c95f852c... with an OpenTimestamps proof |
| Sealed run of EXP-CZ-001 and first standings | MEASURED | experiments/EXP-CZ-001/RESULTS.md: no member viable alone under the frozen bar; best member 44.8% |
| Sealed set, salts and manifest revealed; every commitment verifies | IMPLEMENTED | public-commitments/reveal/EXP-CZ-001/, verify_reveal.py |
| Second casting: five more founding members on a fresh sealed set | MEASURED | experiments/EXP-CZ-009/RESULTS.md: no new member viable alone; Graham 34.5%, the arithmetic specialist |
| One self-taught adapter per member, paired against the untrained member | MEASURED | experiments/EXP-CZ-010/RESULTS.md: all 8 tested members gain, within four synthetic Forge task families, tested on fresh tasks from the same generators as training; 4 pass R1; format harmed for 2; one training seed |
| One teacher-taught adapter per member, against self-taught | MEASURED | experiments/EXP-CZ-011/RESULTS.md: all 8 gain; the teacher pipeline plus its larger data volume beats self-training for 7; not a teacher-quality effect alone; one training seed |
| First children (Generation 1) admitted by a sealed test | MEASURED | experiments/EXP-CZ-017/RESULTS.md: Theo and Hazel pass R1 and beat their parent; no teacher advantage over correct solver labels; three seeds, seed 0 decides |
| Sealed sets 2 and 3 revealed and retired; commitments verify (EXP-CZ-010, 011 and 017 with partial manifest reveals) | IMPLEMENTED | public-commitments/reveal/EXP-CZ-009-011/, reveal/EXP-CZ-017/, verify_reveal.py |
| Elimination by popularity vote | REJECTED | METHODOLOGY.md: votes are predictions, measurement decides |
| First Council and first measured elimination | PROPOSED | ROADMAP.md, Season 1 |
| Randomized crowd-vote arm | PROPOSED | METHODOLOGY.md |
| A generation replaced by offspring that beat their parents | PROPOSED | ROADMAP.md, Season 3 (EXP-CZ-017's children beat their parent, but no member has been replaced) |
| The colony reaching the top rung of the Climb | PROPOSED | ROADMAP.md |

One protocol slip: EXP-CZ-010, EXP-CZ-011 and EXP-CZ-017 were published after the runs; they are externally anchored no later than Bitcoin block 973187 (2026-10-26T04:42:29Z). Their 04:30:59Z freeze time is our own record. Every adapter and child run began after the anchor; five untrained control runs began before it (public-commitments/README.md).

In Season 0 so far, the first casting, the second casting, the two adapter experiments and the first children are reported, and sealed sets 1, 2 and 3 are revealed (2026-10-25 and 2026-10-26) and retired. No member has been eliminated; eliminations start in Season 1.

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

## Anchored in Bitcoin

Before a sealed run, we publish a hash commitment to its design and its sealed task set. Then we timestamp that commitment with [OpenTimestamps](https://opentimestamps.org), which anchors it in a Bitcoin block. Once the block is mined, nobody, including us, can change the commitment or backdate it without the change being detectable. Only the hash goes on the chain. No data, code or results do.

| Commitment | Bitcoin block |
|---|---|
| EXP-CZ-001 | 972993 (2026-10-24 23:56 UTC) |
| EXP-CZ-009 | 973012 (2026-10-25 03:58 UTC) |
| EXP-CZ-010, 011, 017 | 973187 (2026-10-26 04:42 UTC) |

These first anchors were confirmed after their runs had started. The timing evidence for each is in [public-commitments](public-commitments/README.md). From now on, a sealed run starts only after its anchor is confirmed. Anyone can check a proof with `ots verify public-commitments/<file>.ots`.

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

Everything runs on a single consumer GPU (an AMD Radeon RX 9070 XT, 16 GB). Members share base models and take turns, so a colony does not need one loaded model per member.

## Files

| Path | What |
|---|---|
| COLONY.md | Every member by name, with model, lab, architecture and status |
| ROADMAP.md | Seasons, experiments and the Climb |
| METHODOLOGY.md | How the evidence is produced and protected |
| experiments/README.md | Index of experiments and their status |
| experiments/EXP-CZ-001/PREREGISTRATION.md | The first experiment, as designed before the sealed run |
| experiments/EXP-CZ-001/RESULTS_SO_FAR.md | Dev-split measurements to date |
| experiments/EXP-CZ-0xx/RESULTS.md | Sealed results for EXP-CZ-001, 009, 010, 011 and 017 |
| public-commitments/ | Commitments and how to verify them |
| PRIOR_ART.md | Related published work |
| CITATION.cff, NOTICE.md | Citation data and rights notice |

## Credit

Colony Zero was conceived, designed and is directed by Christopher Ayers. Cite it with CITATION.cff. See NOTICE.md for the rights notice.
