# EXP-CZ-005b run: stopped at its power check, before the sealed test

Status: BLOCKED on 2026-11-20 by its preregistered power stop. Every model was trained and evaluated on public
development tasks, but the sealed test never ran, so the hypotheses are untested. Nothing here is a sealed result.

## The question

Does a descendant beat its parent? This is the successor to EXP-CZ-005, which stopped during data preparation. Each
parent practices on public tasks. Its own checked answers become training data for a small adapter on top of its own
weights (arm D). D is compared with the parent (P), with the same parent trained on solver-written answers to the same
tasks (C), and with a fresh, larger adapter on the base model trained on the parent's earlier data plus the new answers
(F). The parents are Theo and Hazel. Each trained arm has five seeds.

Following EXP-CZ-005, the selection rule was fixed in advance: for each task, take the first checked answer that is also
bare. Sampling was fresh, with a new seed base and its own budget.

## What happened

The run started on 2026-11-19 at 02:08 UTC and stopped 35.3 hours later. Every step before the stop passed: practice
sampling for all eight parent and task-family pairs, 30 trainings, 30 epoch selections, a futility check (passed) and
evaluation of all 33 models on a 1,200-task power set.

Then the power check ran. Before the power set was scored, a simulator was frozen together with its code hashes. It
resamples the observed power-set results to estimate how likely the main test would be to succeed on 2,400 sealed
tasks. The main test asks whether D passes the promotion gate against its parent in at least four of five seeds. The
rule, fixed in advance, needs an estimated power with a median of at least 0.80 and a 10th percentile of at least 0.60.

| Parent | Estimated power, median | 10th percentile |
|---|---:|---:|
| Hazel | 0.015 | 0.000 |
| Theo | 0.010 | 0.000 |

The check failed by a wide margin, so the run stopped, as written, and the sealed set was never built. An independent
reviewer reproduced part of the simulation exactly.

## Why it stopped

Training helped, but the descendant's gain was small. Accuracy on the power set (public development tasks, exact
match, mean of five seeds):

| Parent | P (parent) | D (own answers) | C (solver answers) | F (fresh, larger) |
|---|---:|---:|---:|---:|
| Hazel | 0.379 | 0.402 | 0.391 | 0.433 |
| Theo | 0.377 | 0.398 | 0.388 | 0.428 |

The untrained base model scored 0.126. Every trained model beat its parent, consistently across seeds, but D's gain was
about two points. A gain that size cannot be expected to pass the promotion gate in four of five seeds on 2,400 sealed
tasks. This is a finding about the size of the effect, not a machine fault.

## Budget

The time budget was split before the run counted: 72 hours for scientific work (55.7 hours used in total, including
earlier preparation and the closeout) and a separate 4-hour cap for packaging and launch work (1.75 hours used).

## What comes next

The stop cannot change any threshold, seed, data or arm, so EXP-CZ-005b is closed. F, the fresh larger adapter, was the
strongest arm by about three points over D. That is a lead for a new experiment, with its own design and review, not a
result of this one.

## What this cannot show

- Whether a descendant beats its parent on sealed tasks. The sealed test never ran.
- Whether F truly beats D. That comparison was not a tested hypothesis here, and F also had a larger adapter and more
  training data.
- Anything the exact-match checker cannot score.
