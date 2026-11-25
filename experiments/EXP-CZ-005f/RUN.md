# EXP-CZ-005f run: every model test finished, then a results step stopped, before any result was computed

Status: INFRASTRUCTURE on 2026-11-25. All 22 models finished both tests inside their time limits. The next step, which
gathers the answers for scoring, stopped on a naming mismatch in our own tooling. Nothing was scored, so the hypotheses
are untested. Nothing here is a result about the models.

## The question

EXP-CZ-005c, 005d and 005e asked whether F, a fresh adapter trained from the base model, beats its parent and the
self-trained descendants (D) on a fresh sealed test. All three stopped on defects in our own tooling before scoring
anything. EXP-CZ-005f asks the same question with the same 22 frozen models. It draws a new sealed test of 2,400 tasks
and a new protected test of 800 tasks, and it resizes the time limits that stopped 005e.

## What happened

The run started on 2026-11-24 at 21:43 UTC.

1. The frozen design was anchored in Bitcoin (blocks 977,425 and 977,426).
2. A live check confirmed that anchor and that no secret salt existed yet. The new sealed test was then generated on a
   separate machine with a new secret salt. A check confirmed that the new salt and seed differ from every earlier
   one. The test was imported and audited.
3. Its commitment was anchored in Bitcoin (block 977,433), after the design anchor, as the rules require.
4. The step that stopped 005c passed, and so did the first model test, where 005d stopped.
5. All 22 models finished the sealed test, each in 588 to 602 seconds.
6. All 22 models finished the protected test, each in 202 to 207 seconds. The test where 005e stopped passed. The new
   time limits left at least 1.37 times the time needed.
7. The next step, which gathers each model's answers into tables for scoring, stopped itself after half a second at
   05:06:56 UTC on 2026-11-25.

## Why it stopped

The sealed test has a set-specific name in the run's settings ("sealed-10"), and the settings check requires exactly
that name. The step that gathers the answers looks the test up under the plain name "sealed", which is not there.

Our rehearsal and our tests could not show this. Their settings carried both names, so the lookup worked there. No
earlier run had reached this step, because 005c, 005d and 005e all stopped before the model tests ended. An independent
reviewer confirmed the cause.

The frozen design anchored in Bitcoin lists the exact code the run may use, including both files involved. Fixing
either file inside this run would mean running code the anchor does not describe, and the rules forbid resuming a
stopped run by hand. So the run is closed as INFRASTRUCTURE.

## What was exposed

All 22 models answered both tests. Nobody has read or scored those answers, and they stay private. Both test sets are
now retired, and a successor draws fresh ones.

## Budget

The scientific time budget used 27,128 seconds (about 7.5 hours) in total. That includes preparation, the rehearsal,
the run itself (about 17,800 seconds), and a closeout window of about 15 minutes that also covers the wait for the
review. The run spent 2,105,815 evaluation tokens.

## What comes next

The stop cannot change any threshold, seed, data or test set, so EXP-CZ-005f is closed. A successor will keep the same
question and design, and draw a new sealed test and a new protected test. It will also:

1. look the sealed test up by its set-specific name everywhere after the model tests;
2. remove the extra name from the rehearsal and test settings, and refuse to start unless the rehearsal settings use
   exactly the same names as the run;
3. check every step after the model tests (gathering, commitment, scoring and the statistical gates) against the run's
   own settings before launch.

## What this cannot show

- Whether F beats its parent, or D, on sealed tasks. Nothing was scored.
- Anything about the models. The stop came from a naming mismatch in the tooling, not from any model output.
