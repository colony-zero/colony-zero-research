# EXP-CZ-008 pilot: stopped by its futility rule

Status: dev pilot BLOCKED on 2026-11-13. No sealed set, salt or evaluation set was built, so nothing here is a sealed result.

## The question

Can the verified work of the Season 1 team (T3 over Graham, Quinn and Quentin) be trained into one member, Quinn, so that
she beats a plain control that gets the same compute to practise on her own?

## What the pilot measured (public dev data only)

The team solved the training tasks once. Each correct, re-executed program became a candidate lesson. A control gave
Quinn her own samples on the same tasks, matched to the team on charged compute in every family and difficulty cell.
A lesson counts as teacher-unique only when it came from Graham or Quentin and Quinn had no verified answer to that task
in her own samples.

| Measure | Value |
|---|---|
| Candidate training examples (n_train) | 2,673 |
| Teacher-unique examples from Quentin | 157 |
| Teacher-unique examples from Graham | 0 (all 997 of his retained examples were tasks Quinn also solved) |
| Teacher-unique share | 5.87% |

## Why it stopped

The rule, written before the pilot began, needs a teacher-unique share of at least 2% and at least one qualifying example
from each of Graham and Quentin. Graham had none, so the pilot is BLOCKED. The rule was not changed after these counts
were seen. On this pool the extra signal the team could give Quinn comes from Quentin alone.

## Deviations during the pilot

Before any lesson was counted, three cost-matching rules were found unworkable and amended, each reviewed by a second
model: sample counts from 1 to 64 instead of the ladder 4, 8 and 16; the sample count frozen from a separate cost probe
before generation; and matching on charged compute, with model FLOPs required to be at least equal (any excess favours
the control). Kit bugs found on the way were fixed with tests.

## What this cannot show

- Whether compressing a team into one student works with a team whose members know different things.
- Anything about Quentin as the student, larger models, or sealed tasks.
