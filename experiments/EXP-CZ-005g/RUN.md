# EXP-CZ-005g run: the fresh adapter passed the promotion gate for both parents on sealed tasks

Status: STAGE 3 PASS for both parents on 2026-11-25. Every step ran to the end, including scoring. For each of the two
parents, the fresh adapter F beat its parent on a new sealed test of 2,400 tasks in all five training seeds, and it did
not lose ground on the protected test. F also beat the self-trained descendants D. This is a dev-selected confirmation,
with the limits listed at the end.

## The question

EXP-CZ-005c, 005d, 005e and 005f asked whether F, a fresh adapter trained once from the base model on the lineage's
accumulated checked data, passes the promotion gate against its parent on a fresh sealed test, in at least four of five
seeds per parent. All four stopped on defects in our own tooling before anything was scored. EXP-CZ-005g asks the same
question with the same 22 frozen models. It draws a new sealed test of 2,400 tasks and a new protected test of 800
tasks, and it fixes the naming mismatch that stopped 005f.

## What happened

The run started on 2026-11-25 at 12:12 UTC.

1. The frozen design was anchored in Bitcoin (block 977,516). The first anchor check could not read the design file,
   because our launch script had saved it readable by its owner only. We changed the file permissions back to the
   earlier runs' values, with the contents and hashes unchanged, and an independent reviewer approved before the check
   ran again. This happened before any secret salt existed.
2. A live check confirmed that anchor and that no secret salt existed yet. The new sealed test was then generated on a
   separate machine with a new secret salt and seed. A check confirmed that both differ from every earlier one. The
   test was imported and audited.
3. Its commitment was anchored in Bitcoin (block 977,531), after the design anchor, as the rules require.
4. All 22 models answered the sealed test and the protected test, from 16:50 to 21:35 UTC.
5. The answers were committed, a post-run record was anchored in Bitcoin (block 977,578), and a public randomness
   beacon was read after that anchor. Scoring and the statistical gates then ran. The run finished at 23:13 UTC.

## Result

Tasks solved out of 2,400 sealed tasks:

| Parent | Parent model P | F, five seeds | D, five seeds | Seeds passing the gate |
|---|---:|---|---|---:|
| Theo | 894 (37.3%) | 998 to 1,011 (41.6% to 42.1%) | 941 to 953 (39.2% to 39.7%) | 5 of 5 |
| Hazel | 895 (37.3%) | 1,006 to 1,015 (41.9% to 42.3%) | 935 to 960 (39.0% to 40.0%) | 5 of 5 |

- Against its parent, F gained 4.3 to 5.0 percentage points per seed. The lower bound of every gain was at least 3.29
  points.
- On the protected test, every F seed solved 2.9 to 5.1 points more than its parent, so nothing was given up there.
- Compute per task stayed within 0.3% of the parent's.
- F beat D by 2.5 points for Theo (95% interval 1.8 to 3.2) and 2.6 points for Hazel (1.9 to 3.2). After the Holm
  correction for two parents, p = 0.00002 for each. We chose this comparison's direction after looking at earlier
  development results, and F and D differ in more than one way (see the limits).

For each parent, the seed-0 F adapter is registered as that lineage's next member.

## The claim, in the preregistered wording

For each parent, the result is reported as: "a dev-selected confirmation that fresh base retraining on accumulated
colony verified data (gen-1 plus G2(P)) passes the Stage 3 promotion gate against P." It is always reported beside
EXP-CZ-005b (D-101): incremental weight-space descent (D, a fresh rank-16 LoRA on merged P trained on G2(P) only) did
not show sufficient power or advantage to be expected to pass the same gate. That 005b result is a planning stop on
public dev data, not a sealed test of D, and this experiment does not convert it into one. A positive H5g.1 means fresh
base retraining on the cumulative lineage data is a viable Stage 3 replacement route for these two lineages; it does
not show that self-training, evolution or G2 itself is the cause (section 14).

The result is about these 22 fixed Q8_0 artifacts, the 017 serving protocol and the four Forge families; every retained
scope limit of the 005b spec, section 1 ("Retained base scope limits") applies.

## Budget

The scientific time budget used 28,341 seconds (about 7.9 hours) in total. That includes preparation, the rehearsal,
the run itself, and a closeout receipt of 1,816 seconds for our own work after the design was frozen. The run spent
2,364,599 evaluation tokens.

## What this cannot tell you

These limits are copied from the preregistration.

- Why F beats P, if it does. Rank, data, and retraining differ. No fresh rank-32 generation-1-only arm separates G2 from
  capacity or retraining.
- Whether evolution or self-training works in general or beats ordinary rejection-sampling fine-tuning.
- Whether D differs from F for one cause. Rank, weights, padded positions, optimizer steps, schedule, and G2-only compute
  differ. The direction is post-hoc.
- Whether the dev-selected effect holds. Only set 11 is a fair estimate for these artifacts.
- Anything scientific from sets 7, 8, 9 or 10 or from `ea626db1` or `8ca89515`. Sets 7 and 8 were never evaluated, and
  the set-9, set-10, `ea626db1` and `8ca89515` answers were never read or scored.
- Whether the fresh protected suite matches `8ca89515` or `ea626db1` in difficulty. It follows the same cells and
  source, but it holds different tasks.
- Whether the fresh protected suite is safe against an undiscovered leak. The claim relies on hashes, the five-key audit,
  rehearsal exclusion, and selection from rows no selector touched, not a hiddenness oracle.
- Whether the post-evaluation path is free of other production-only defects. The config-read audit, the
  production-shaped tests and live probe S1 cover what they read and run. A production branch none of them reaches stays
  untested until 005g runs it.
- Whether 1.25 is the right child-window floor on other hardware or models. It covered the 005f production timings with
  at least 77 s on every protected window.
- Whether explorers, network, or the image registry behave outside frozen bounds.
- Whether 120 s is operationally optimal.
- Whether the route still works after P3 or S1. A pass shows the route worked at that moment.
- Whether the coverage inventory found every boundary. It lists what the fixture observed and what the audit can see.
- Whether fresh base retraining stays affordable. The gate counts inference tokens, not training.
- Whether gains continue, how often future lineages pass, or results generalize to larger models, other bases, settings,
  or tasks.
- Preservation of a particular ability. Protection is the aggregate ADR-0006 rule on one fixed suite.
