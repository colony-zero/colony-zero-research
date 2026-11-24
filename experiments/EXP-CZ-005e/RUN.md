# EXP-CZ-005e run: stopped by a time limit in the protected test, before any result was computed

Status: BLOCKED at a time limit on 2026-11-24. One model's protected test ran into a time limit that our tooling had set
too tight. Nothing was scored, so the hypotheses are untested. Nothing here is a result about the models.

## The question

EXP-CZ-005c and EXP-CZ-005d asked whether F, a fresh adapter trained from the base model, beats its parent and the
self-trained descendants (D) on a fresh sealed test. Both stopped on defects in our own tooling before testing anything.
EXP-CZ-005e asks the same question with the same 22 frozen models. It draws a new sealed test of 2,400 tasks and
rebuilds the evaluation program so its built-in timestamp check runs locally.

## What happened

The run started on 2026-11-24 at 00:29 UTC.

1. The frozen design was anchored in Bitcoin (block 977,301).
2. A live check confirmed that anchor and that no secret salt existed yet. The new sealed test was then generated on a
   separate machine with a new secret salt, imported and audited.
3. Its commitment was anchored in Bitcoin (block 977,311), after the design anchor, as the rules require.
4. The step that stopped 005c passed, and so did the first model test, where 005d stopped.
5. All 22 models finished the sealed test. Six models finished the protected test of 800 tasks.
6. The seventh protected test ran into its time limit at 195 seconds, and the run stopped itself at 07:41:49 UTC.

## Why it stopped

Each model's time limit is 1.5 times the time measured in the rehearsal. The evaluation program then keeps a fixed 100
seconds of that limit for starting and stopping, and the model gets the rest. For the 800-task protected test, the
rest was about 195 to 208 seconds, and every model needed about 197 seconds. The margin was close to zero. On the
larger sealed test, the same rule left at least 1.7 times the time needed.

The rehearsal could not show this, because it used 40-task stand-ins that finish in seconds. Our admission checks
compared each limit with the phase total, not with the time a model needs at full size. An independent reviewer
confirmed the cause. Under the rules, a stop at a time limit is classed as BLOCKED and is never relabelled.

## What was exposed

All 22 models answered the sealed test, and seven models answered some or all of the protected test. Nobody has read
or scored those answers, and they stay private. Both test sets are now retired, and a successor draws fresh ones.

## Budget

The scientific time budget used 46,074 seconds (about 12.8 hours) in total. That includes preparation, the rehearsal,
the run itself (about 15,450 seconds), and a closeout window that also covers the time spent waiting for the review.
The run spent 709,111 evaluation tokens.

## What comes next

The stop cannot change any threshold, seed, data or test set, so EXP-CZ-005e is closed. A successor will keep the same
question and design, and draw a new sealed test and a new protected test. It will also:

1. size each time limit as 1.5 times the measured model time, plus the fixed 100 seconds for starting and stopping;
2. refuse to start unless every model's time is at least 1.25 times what it is expected to need, at full size.

## What this cannot show

- Whether F beats its parent, or D, on sealed tasks. Nothing was scored.
- Anything about the models. The stop came from a time limit in the tooling, not from any model output.
