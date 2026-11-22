# EXP-CZ-005d run: stopped at the first model test, before any model saw a sealed task

Status: INFRASTRUCTURE stop on 2026-11-22. A check built into our evaluation program failed before any model read a
sealed task, so the hypotheses are untested. Nothing here is a result about the models.

## The question

EXP-CZ-005c asked whether F, a fresh adapter trained from the base model, beats its parent and the self-trained
descendants (D) on a fresh sealed test. It stopped on a time limit in our own tooling before testing anything.
EXP-CZ-005d asks the same question with the same 22 frozen models. It draws a new sealed test of 2,400 tasks, and the
time limit of every step that touches the network is sized from its counted calls and their worst-case retries.

## What happened

The run started on 2026-11-22 at 00:28 UTC.

1. The frozen design was anchored in Bitcoin (block 976,971).
2. The new sealed test was generated on a separate machine with a new secret salt, then imported and audited.
3. Its commitment was anchored in Bitcoin (block 976,989), after the design anchor, as the rules require.
4. The step that stopped 005c passed this time, in about 8 seconds.
5. The first model test began at 04:53 UTC. The evaluation program checks the Bitcoin timestamps itself before it
   reads any task. That check failed in under a second, and the run stopped at 04:53:58 UTC.

## Why it stopped

The evaluation program has an older copy of the timestamp-check code built into it. That copy reaches the timestamp
checker through a remote connection that this run's machine is not allowed to use. The rest of the 005d tooling had
been moved to a local checker, but the copy inside the program was missed.

Our earlier checks could not see it. The rehearsal skips real timestamp checks, the automated tests replace the
program with a stand-in, and the static check only read our Python files, not code built into the program. Running the
same check by hand fails the same way, so every model test would have failed. An independent reviewer confirmed the
cause and the classification.

## What was exposed

Nothing. The check runs before the program reads any task, and the model server received no requests. The new sealed
test was never shown to a model, and no protected task was used.

## Budget

The scientific time budget used 13,515 seconds (about 3.75 hours) in total. That includes preparation, the rehearsal,
and a closeout window that also covers the time spent waiting for the review. About 1,809 seconds of it came after
launch, and 1,736 of those are a time reservation held open for the stopped step. No evaluation tokens were spent
after launch.

## What comes next

The stop cannot change any threshold, seed, data or test set, so EXP-CZ-005d is closed. Its sealed test is retired
unused. A successor will keep the same question and design and draw a new sealed test. It will also:

1. rebuild the evaluation program so its built-in check uses the local timestamp checker;
2. run that program's real check against a confirmed timestamp before launch;
3. add a check that reads code built into our programs for stale remote connections.

## What this cannot show

- Whether F beats its parent, or D, on sealed tasks. Nothing was evaluated.
- Anything about the models. The stop came from the tooling, not from any model output.
