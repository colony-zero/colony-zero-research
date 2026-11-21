# EXP-CZ-005c run: stopped by its own time limit, before any model was tested

Status: BLOCKED on 2026-11-21 by a preregistered time limit on one verification step. No model was evaluated, so the
hypotheses are untested. Nothing here is a result about the models.

## The question

EXP-CZ-005b stopped at its power check, but one arm stood out on public development tasks: F, a fresh, larger adapter
trained from the base model, beat its parent by about five points. EXP-CZ-005c was designed to test that lead properly,
with no retraining. It takes the 22 frozen models from 005b and asks two questions on a fresh sealed test of 2,400
tasks and a fresh protected suite of 800: does F beat its parent, and does F beat the self-trained descendants (D)?

## What happened

The run started on 2026-11-21 at 12:31 UTC. Before launch, a rehearsal ran all 22 models and reproduced their 005b
answers byte for byte.

1. The frozen design was anchored in Bitcoin (block 976,905).
2. The fresh sealed test was generated on a separate machine with a new secret salt, 120 tasks in each of 20 cells,
   then imported and audited.
3. Its commitment was anchored in Bitcoin (block 976,918), after the design anchor, as the rules require.
4. The next step re-verifies those anchors before any model sees a sealed task. It ran past its 120-second limit and
   was stopped at 16:15 UTC. The rules, fixed in advance, treat any step that reaches its time limit as a stop, so the
   run ended there. The evaluation never started.

## Why it stopped

The verification step checks the two Bitcoin timestamps, then checks the authorization for each of the 22 models, and
each of those checks both timestamps again. That is 46 checks in a row at about 4.75 seconds each, roughly 218
seconds, inside a 120-second limit. The limit was carried over from 005b, which never reached this step. The rehearsal
skips real timestamp checks, so it could not catch the problem.

So this is a defect in our own tooling, and the stop was certain once the step ran. An independent reviewer traced the
46 checks in the code and in the timestamps, and confirmed the classification. Our first write-up blamed a network
stall; the reviewer's trace replaced that explanation.

## Budget

The scientific time budget had used 3,290 seconds (about 55 minutes) in total, including preparation, the rehearsal and
the closeout. About 430 seconds of that came after launch. No evaluation tokens were spent after launch.

## What comes next

The stop cannot change any threshold, seed, data or test set, so EXP-CZ-005c is closed. The sealed test it generated is
retired without ever being used. A successor will keep the same question and design, draw a new sealed test after its
own design anchor, and size the time limit of every step that touches the network from its actual number of calls and
their worst-case retries, with a test that counts those calls.

## What this cannot show

- Whether F beats its parent, or D, on sealed tasks. Nothing was evaluated.
- Anything about the models. The stop came from the tooling, not from any model output.
