# EXP-CZ-004 pilot: stopped at the competence floor

Status: pilot BLOCKED on 2026-11-14 at its first phase (P0). No library was written, no new task family was authored
and no sealed set was built, so nothing here is a sealed result.

## The question

Do verified skills that one member learns transfer to problem families it has never seen, and to a model from a
different lab? The two fixed recipients are Quinn (Qwen, 0.8B) and Graham (IBM Granite, 350M).

## The gate that stopped it

Before any skill work, the preregistration requires both recipients to show basic competence on the four old task
families, so that a later transfer test is not run on models that cannot do the work at all. Each recipient answers
200 public calibration tasks (50 per family) with no library at a 4x compute budget. Each needs at least 40/200
overall and at least 5/50 in every family. A recipient that fails is not replaced; the experiment stops.

| Recipient | Overall | Arithmetic chains | Graph reachability | JSON extraction | List transforms |
|---|---|---|---|---|---|
| Quinn | 42/200 | 3/50 | 22/50 | 10/50 | 7/50 |
| Graham | 44/200 | 1/50 | 20/50 | 8/50 | 15/50 |

Both pass overall. Both fail the arithmetic floor, so P0 is BLOCKED. The rule was not changed after these counts were
seen. The run used 100,087 tokens and about four minutes on one machine; every record was complete and every cost was
metered.

## Why arithmetic failed

The arithmetic answers were well formed and wrong (for example 105 where the answer was 85), not parse failures. The
fixed answer contract asks for the answer directly as JSON, with Qwen's thinking mode off. Chained arithmetic in one
step, with no working shown, is beyond these two models. A rehearsal run that let Quinn reason at length (and was not
evidence) reached 20/50 on arithmetic, so this result does not show the models cannot do arithmetic with reasoning.
Changing the protocol after seeing the scores would have been tuning to pass, so it was not done.

## Kit defects fixed before this run

Rehearsals on public dev data, outside the queue, found five harness defects before the run that counts. Each was
fixed with a test, none changed a threshold, task or recipient:

- the checker for list tasks expected a different task schema than the task generator wrote;
- the answer instruction conflicted with each task's own reply line, so correct answers were scored as unparsed;
- Quinn ran in thinking mode, unlike every other colony kit, and ran out of tokens before answering;
- the 4x budget funded one attempt instead of the specified solo search;
- correct list answers given as JSON arrays were passed to the checker in the wrong text form.

## What this cannot show

- Whether skills transfer. No skill was learned or tested.
- Whether these recipients pass with an answer contract that allows reasoning, or with tools. That would be a new
  preregistration, not a change to this one.
- Anything about larger models or sealed tasks.
