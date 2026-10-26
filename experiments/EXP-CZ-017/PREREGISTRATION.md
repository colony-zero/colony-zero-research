# EXP-CZ-017: First Birth, two teachers and a solver-label control

Run status: FROZEN 2026-10-26T04:30:59Z, before any child saw sealed set 3 (../../public-commitments/EXP-CZ-017.md). This page was published after the sealed run. The commitment was timestamped (Bitcoin block 973187, 2026-10-26T04:42:29Z) but not pushed here before the run; see the timing note on the commitment page and in RESULTS.md.

## Question

Can the colony make new members of its own, small models trained only on checked answers from a large open-weight teacher, and does the choice of teacher matter? Two children are made from the same parent, the same tasks and the same recipe; only the teacher differs. A third model, trained on the generator's own correct answers for the same tasks, separates what a teacher adds from what plain correct labels give.

## Why there were two earlier specifications

Two earlier specifications asked the same question and stopped at their data gate, before any child was trained and before sealed set 3 was used. The gate requires at least 6,000 tasks where both teachers have an accepted answer, and at least 150 in every family and difficulty cell. With thinking-off teacher answers, five hard cells fell short. With added thinking-on answers for those cells, only JSON extraction at difficulty 4 and 5 stayed short (87 and 120 tasks). Their failures trace to an unstated convention of the task generator (copy the noun exactly as written: "lenses", not "lens"), not to missing teacher skill. This specification keeps everything else and changes one thing: those two cells train with whatever shared tasks they have and are reported separately.

## The children

- Parent: SmolLM2-135M-Instruct (Hugging Face, Apache-2.0, revision 12fd25f77366fa6b3b4b768ec3050bf629380bac), the smallest model in the colony, format-line template.
- Theo: the parent trained on checked answers from DeepSeek V4.1 Flash 1017 (open weights, MIT).
- Hazel: the parent trained on checked answers from Xiaomi MiMo V2.6 Flash (open weights `XiaomiMiMo/MiMo-V2.6-Flash-RL`, MIT).
- Solver-label control: the parent trained on the generator's exact reference answer, written in the template's required form. It is a control, not a candidate member.
- Each child is its adapter merged into the parent's weights, converted to GGUF and quantised. Q8_0 is the primary file; Q4_K_M is the challenger.

## Data

- Tasks: 11,976 new public practice tasks (the four families), with every task dropped whose prompt also appears in dev, test, EXP-CZ-010's practice file, any sealed set, or earlier in the file.
- Teachers, both FP8 quantisations from one commercial inference provider, pinned with no fallbacks, at temperature 0.7, top_p 0.95, 512 tokens: samples 1 and 2 with thinking off on all tasks; samples 3 and 4 with thinking off, then samples 5 and 6 with thinking on, on the 2,625 tasks of the hardest cells that lacked an accepted answer from both teachers. Only the final answer is stored and trained on, never the hidden reasoning.
- Acceptance: correct, well formed and not truncated; the first accepted sample per task and teacher.
- Training set: the tasks where both teachers have an accepted answer: 8,621 tasks. Theo, Hazel and the solver control train on exactly these task ids, one example per task.
- Gate: at least 6,000 shared tasks and at least 150 in every cell except JSON extraction at difficulty 4 and 5 (exempt, reported separately).

## Recipe

EXP-CZ-010's adapter recipe on the attention and MLP projections: LoRA rank 16, alpha 32, dropout 0.05; completion-only loss; AdamW 2e-4, cosine with 3% warmup; batch 16; sequence cap 1,024; 2 epochs. Three training seeds per arm (0, 1, 2); seed 0 is the primary child, seeds 1 and 2 are replications and never pick a sealed winner. Epoch choice per arm and seed on dev 0 to 399, by EXP-CZ-010's tie rule. Parity check between the trainer and llama.cpp for the parent and every merged child.

## Sealed set 3

2,400 new tasks (600 per family, 120 per family and difficulty cell) from a new secret salt. A few easy prompts recur by chance, so every sealed task whose prompt also appears in a public file, in sealed set 1 or 2, or twice within set 3 was excluded before any run: 7 tasks. Every run uses the scored file of 2,393 tasks.

## Hypotheses (each can fail)

On sealed set 3, greedy, format-line template, 512 tokens, Q8_0 children of seed 0, exact McNemar, Holm over the five tests H17.1 to H17.4b:

- H17.1 Theo solves at least 5 points more than the parent, and the difference is significant.
- H17.2 Hazel solves at least 5 points more than the parent, and the difference is significant.
- H17.3 Theo and Hazel differ (two-sided, no direction predicted). This is the head-to-head.
- H17.4a and H17.4b Each child solves at least 2 points more than the solver control, and the difference is significant.
- H17.5 For each child, Q4_K_M loses no more than 2 points against Q8_0 (one-sided 95% lower bound of the paired difference above -0.02). If it fails, the child ships as Q8_0.

Seeds 1 and 2 are reported for every arm; a hypothesis that holds for seed 0 but reverses in both replications is reported as not robust.

## Decision rules and readings fixed before the freeze

- Minimum differences are compared in whole tasks: 100 x difference at least points x 2,393.
- H17.5 uses the one-sided 95% Wald lower bound of the paired difference, d - 1.6449 x sqrt(((b + c) - (b - c)^2 / n) / n^2), compared with -0.02.
- Replications: each seed is its own Holm family of five; a seed-0 success is not robust only if both replications reverse its sign.
- Membership: a child joins the colony only if its seed-0 Q8_0 run passes R1 exactly as in EXP-CZ-001 (Wilson lower bound of E1 at least 0.25, E2 at least 0.90, E1 above the guessing baseline's upper bound). R1 of the solver control and of seeds 1 and 2 is reported only. A child that fails R1 is recorded as born but not admitted. A birth eliminates no one.
- The guessing baseline is read back from the 13 planned ledgers.
- A run is void, and reported, if its ledger fails verification, its result disagrees with its ledger, its task file, model or template hash differs from the manifest, it is not greedy, or it lacks one verdict per task.

## Exploratory comparisons

After the 13 planned runs, the nine untrained founders run on sealed set 3 with their frozen templates, so the children can be placed in the colony's standings. These rows test no hypothesis. An earlier plan to also run the EXP-CZ-010 and EXP-CZ-011 adapters on set 3 was dropped before the freeze.

## Endpoints

E1 to E4 as in EXP-CZ-001, per family and per cell with the two exempt cells marked; each child's share of training examples per cell; file sizes, peak memory and speed; teacher requests, tokens and USD; GPU minutes per arm.

## What this cannot tell you

Whether the children learned anything beyond these four task families; whether a teacher's reasoning traces, logprobs or more data would help; whether a full-parameter or from-scratch child would do better; how the children would do on hard JSON with enough training examples; how a child behaves inside a colony.
