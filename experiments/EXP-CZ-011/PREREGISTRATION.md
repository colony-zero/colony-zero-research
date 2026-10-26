# EXP-CZ-011: Outside teacher

Run status: Published after the runs; externally anchored no later than Bitcoin block 973187 (2026-10-26T04:42:29Z) (../../public-commitments/EXP-CZ-011.md). Our own freeze record gives 2026-10-26T04:30:59Z, together with EXP-CZ-010, before any adapter saw sealed set 2; that time is not independently established. Reported and revealed 2026-10-26 (RESULTS.md); sealed set 2 is retired.

## Question

Does a tiny member learn more from a large open-weight teacher's checked answers than from its own checked answers, on the same practice problems and the same adapter recipe?

## Design

- Every one of the nine founding members gets a second adapter, made by EXP-CZ-010's recipe with one change: the training answers come from an outside teacher instead of from the member itself.
- Teacher: DeepSeek V4.1 Flash 1017, open weights `deepseek-ai/DeepSeek-V4.1-Flash-1017` (Hugging Face commit 1bae0e1088993b9b82de08f59de5be5a34e42170), MIT licence, served by a commercial inference provider as an FP8 quantisation of those weights, provider pinned with no fallbacks, thinking off. The training answers are final answers of the kind a member gives, not hidden reasoning. Before any sampling, the licence and the provider's terms were checked under our rule on training data (no outputs from a model or service whose terms forbid it).
- Requests went through a proxy that pinned the model, the provider and the thinking mode and refused every request once recorded spend reached 15 USD.
- Tasks: EXP-CZ-010's practice file (1,996 public tasks). The teacher answers each task 4 times at temperature 0.7, top_p 0.95, 512 tokens, once per prompt template the members use (three templates). The provider's sampling is not reproducible run to run; the kept answers are whatever the recorded ledgers hold.
- Selection per member: the teacher run on that member's template, then EXP-CZ-010's rule (correct and well formed, at most 2 per task, lowest sample number first), tokenised for the member's own model. Fewer than 200 kept examples means data-starved, still trained and reported.
- Adapter recipe, parity gate, serving path and checkpoint choice: exactly EXP-CZ-010's.
- Each member then exists in three versions measured on the same 1,200 sealed tasks of set 2: untrained (the same-binary rerun shared with EXP-CZ-010), self-taught (EXP-CZ-010) and teacher-taught (this experiment).

## Hypotheses (each can fail)

- H11.1 For at least five of the nine members, the outside-taught member solves more sealed tasks than the untrained member (exact McNemar, Holm over nine, alpha 0.05).
- H11.2 Outside-taught versus self-taught, per member: exact McNemar, Holm over nine, two-sided. No direction is predicted; the count of members significantly better each way is the result.
- H11.3 Format validity (E2) of the outside-taught member does not fall more than 2 points below the untrained member for any member.

## Decision rules

- H11.1 is supported if at least five members show a Holm-significant gain over the untrained member.
- H11.2 has no direction: the result is the number of members significantly better each way after Holm.
- H11.3 holds if no counted member's E2 falls more than 2 points (24 tasks of 1,200) below the untrained member.
- Holm is over m = 9 in each family; Graham, excluded by the parity gate before the freeze, enters each family as an untested hypothesis at p = 1. Void runs follow EXP-CZ-010's rule.

## Amendments before any adapter trained on teacher data

1. Teacher endpoint, before any teacher answer existed. The first plan pinned the model developer's own endpoint, whose terms explicitly allow distillation. The routing service refused every request, because that endpoint may train on prompts and our account excludes such endpoints. No answer was produced and nothing was spent. The teacher is instead the FP8 quantisation of the same weights from a provider that does not train on or retain data.
2. Teacher inputs. One member template (Quinn's) is few-shot: every prompt carries two worked examples from dev tasks 400 to 479, the fixed example pool that is never scored. The teacher therefore saw those 80 public examples and their answers inside Quinn's prompts, exactly as Quinn does. It never saw dev tasks 0 to 399 (used for checkpoint choice), the test split, or any sealed set. Found by an independent review while that sampling was running; sampling was stopped, this amendment written, then resumed.
3. Provider terms, corrected reading. The provider's terms contain a general clause against using the service to build services that compete with it. Its business is hosted inference; training small research adapters on its outputs does not create a competing inference service, and the terms place no other restriction on the use of outputs. This reading is recorded as the basis for use until written confirmation from the provider is obtained.

## Endpoints

E1 to E4 as in EXP-CZ-001 on sealed set 2. Cost: teacher requests, tokens and USD spent, kept examples per member, GPU minutes for training, adapter size.

## What this cannot tell you

Whether a different teacher, more samples, or the teacher's reasoning traces would help more; whether gains carry over to tasks unlike the Forge families; whether a teacher-taught member behaves differently inside a colony.
