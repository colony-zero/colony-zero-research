# EXP-CZ-009: Second casting

Run status: FROZEN 2026-10-25T03:32:59Z, before any member saw sealed set 2 (../../public-commitments/EXP-CZ-009.md).

## Question

How do the five new founding members (Graham, Rowan, Erin, Bastien, Mina; see ../../COLONY.md) compare with the first four, measured exactly as Season 0 measured the first four, on a fresh sealed set?

## Design

- All nine members run greedy on sealed set 2: 1,200 new tasks from the same four families and difficulties, generated from a new secret salt and sharing no task with sealed set 1.
- Each member uses one prompt template. The first four keep their Season 0 choice. The five new members chose theirs on the public dev split by the Season 0 rule before the freeze: Graham step-by-step; Rowan, Erin, Bastien and Mina the format-line template.
- Same runner, decoding, output cap (512 tokens) and checker as Season 0. Bastien's chat template always starts with a thinking section and cannot be switched off, so it runs that way, and its output cap is the same as everyone's.
- The analysis program is Season 0's with one fix made before the freeze: the five new members get their own arm labels. On Season 0's data it reproduces the published results exactly.
- Rules R1 to R4 are exactly as in EXP-CZ-001.

## Hypotheses (each can fail)

- H9.1 At least one new member passes R1.
- H9.2 Graham (attention only) and Grace (Mamba-2 hybrid), siblings from one lab of almost the same size, differ in sealed solves (exact McNemar, alpha 0.05, one preregistered pair).
- H9.3 The first four members' solve rates on sealed set 2 fall inside their Season 0 95% intervals, which checks that the two sealed sets are equally hard.

## Dev split results used for template choice (not standings)

| Member | Selected template | Dev solved of 400 |
|---|---|---|
| Graham | step-by-step | 127 |
| Erin | format line | 78 |
| Mina | format line | 75 |
| Rowan | format line | 52 |
| Bastien | format line | 27 (256 answers hit the 512-token cap while thinking) |

## What this cannot tell you

These are single members on synthetic tasks; the result says nothing about how a colony performs together.
