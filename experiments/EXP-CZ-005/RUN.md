# EXP-CZ-005 run: stopped by its own data rule

Status: BLOCKED on 2026-11-16, during data preparation. No model was trained, no epoch was selected and no evaluation
ran, so the three hypotheses are untested. Nothing here is a sealed result.

## The question

Does a descendant beat its parent? Each parent practices on public tasks. Its own checked answers become training data
for a small adapter on top of its own weights (arm D). D is compared with the parent (P), with the same parent trained
on solver-written answers to the same tasks (C), and with a fresh adapter on the base model (F). The two parents are
Theo and Hazel.

## What happened

Theo practiced first. Each of the four task families needed at least 50 checked answers. Theo cleared all four:

| Family | Checked answers kept | Needed |
|---|---:|---:|
| Arithmetic chains | 102 | 50 |
| Graph reachability | 1,997 | 50 |
| JSON extraction | 397 | 50 |
| List transforms | 885 | 50 |

Arithmetic was the expected risk. In a small rehearsal Theo kept none of 50, so passing here was not a given.

The next step builds the training files. One rule, fixed before the run, keeps the D and C files comparable: where Theo's
answer differs from the solver's, the difference may only be surface form (spacing, JSON key order, letter case, a
recognized answer wrapper). Reasoning or extra text is not allowed, any unexplained difference stops the experiment, and
Theo's answers are never rewritten to pass.

One of Theo's 3,381 kept answers broke that rule. On a list task Theo wrote 385 tokens of step-by-step working and then
the correct answer. The answer checker accepted it, because the final answer was right. The data rule rejected it,
because the whole answer was not bare. The solver's version was 19 tokens. The experiment stopped, as written, about
5.6 hours into the run. Hazel never started.

## Why it happened

Two of our own rules did not fit together. The selection rule took, for each task, the first answer the checker
accepted. The data rule then required that answer to be bare. The checker accepts correct answers with working around
them, so a long accepted answer could be selected and then refused. A 200-task rehearsal produced no such answer for
Theo, so the gap was not seen. This is a design error in the protocol, not a machine fault and not a finding about Theo.

The row was not removed, a different answer was not picked and the run was not resumed. Any of those would change the
rules after seeing the data.

## Before this run

Two earlier launch attempts failed on setup bugs before any model ran (a missing state file, then a missing tokenizer
file). Both are recorded and neither produced data. The time budget was split before the run counted: 72 hours for
scientific work (27.9 hours used) and a separate 4-hour cap for packaging and launch work (about 3 hours used).

## What comes next

A successor experiment may select, for each task, the first accepted answer that is also bare, fixed in advance for
both parents. It will say that it follows this stop, use fresh sampling with a new seed base and its own budget, and
treat what was seen here as development evidence. It needs its own review before it runs.

## What this cannot show

- Whether a descendant beats its parent. No descendant was trained.
- Anything about Hazel, who never ran.
- Whether self-training on bare answers helps. That is the successor's question.
