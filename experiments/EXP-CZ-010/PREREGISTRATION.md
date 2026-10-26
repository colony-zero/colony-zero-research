# EXP-CZ-010: Targeted adapter for every founding member (self-taught)

Run status: Published after the runs; externally anchored no later than Bitcoin block 973187 (2026-10-26T04:42:29Z) (../../public-commitments/EXP-CZ-010.md). Our own freeze record gives 2026-10-26T04:30:59Z, together with EXP-CZ-011, before any adapter saw sealed set 2; that time is not independently established. Reported and revealed 2026-10-26 (RESULTS.md); sealed set 2 is retired.

## Question

Does one low-rank adapter per member, trained only on public practice problems and the member's own checked answers, raise that member's verified solve rate on sealed problems compared with the same member untrained?

## Design

- Every one of the nine founding members gets an adapter made by the same recipe, so nobody chooses afterwards who "needed" one.
- Training data: each member answers 1,996 public practice tasks (the four Forge families, a new public train split) 8 times at temperature 0.7, with its own prompt template and a 512-token cap. Its correct, well-formed answers become its training data, at most 2 per task, lowest sample number first (rejection-sampling fine-tuning, also known as STaR). A member that keeps fewer than 200 examples is still trained and reported, flagged as data-starved.
- The practice file was checked before training: every task whose prompt also appears in the dev or test splits, in sealed set 1 or 2, or earlier in the file was dropped. 4 were dropped (3 repeated sealed set 1, which is retired and public; 1 duplicate). No practice task overlaps sealed set 2, by id or by prompt.
- Adapter recipe, fixed: LoRA rank 16, alpha 32, dropout 0.05 on the attention and MLP projections (on recurrent or state-space blocks, the block's input and output projections; the module list per architecture was written down before training); loss on completion tokens only; AdamW, learning rate 2e-4, cosine decay with 3% warmup, batch 16 sequences, sequence cap 1,024 tokens, 2 epochs, seed 0. Training runs in Rust (Burn) on one 16 GB consumer GPU. The base weights never change.
- Checkpoint choice: the epoch-1 and epoch-2 adapters each answer dev tasks 0 to 399 greedily. The one with more solves is kept; ties go to fewer format failures, then to epoch 2.
- Parity gate: before an adapter counts, the trainer and llama.cpp must agree on next-token probabilities (largest top-10 difference at most 0.02 on three prompts). A member whose model cannot pass is reported as not run, never silently dropped.
- Serving: llama.cpp with the adapter loaded. Where llama.cpp cannot apply an adapter to an architecture, the adapter is merged into the base weights and quantised to Q8_0 like the base.
- Sealed run: each adapted member answers the 1,200 tasks of sealed set 2 greedily, same template and 512-token cap. The control is each member untrained, rerun on the same set with the same runner binary (the Season 0 runner cannot load an adapter). EXP-CZ-009's runs are a secondary reference reported beside it.

## Hypotheses (each can fail)

- H10.1 For at least five of the nine members, the adapted member solves more sealed tasks than the untrained member (exact McNemar, Holm-adjusted over the nine members, alpha 0.05).
- H10.2 At least one member that fails R1 untrained passes R1 adapted, with R1 exactly as in EXP-CZ-001.
- H10.3 Format validity (E2) does not fall for any member by more than 2 points.

## Decision rules

- R10.1: a member's adapter works if its McNemar test rejects after Holm and the adapted member solves more.
- R10.2: an adapter that lowers E2 by more than 2 points (more than 24 extra format failures of 1,200), or lowers E1 significantly, is recorded as harmful for that member.
- R10.3: H10.1 is supported only if at least five members meet R10.1.
- R1 as in EXP-CZ-001: Wilson lower bound of E1 at least 0.25, E2 at least 0.90, E1 above the guessing baseline's upper Wilson bound. The guessing baseline is read back from all ledgers in the analysis plan.
- A run is void, and reported, if its ledger fails verification, its result disagrees with its ledger, its task file, model, template or adapter hash differs from the manifest, it is not greedy, or it lacks one verdict per task. A void run counts as an untested hypothesis (p = 1).

## Interpretations fixed before the freeze

- Holm is over m = 9 in each family: the counted members plus any member excluded by the parity gate, entered as an untested hypothesis at p = 1. Graham's adapter failed the parity gate before the freeze, so he enters at p = 1 and the five-member threshold is unchanged.
- The untrained same-binary rerun is the primary control; EXP-CZ-009's ledgers are a secondary reference.
- Quinn counts in both arms, although his training used memory-only settings (smaller micro-batches) that leave the recipe unchanged.

## Endpoints

E1 to E4 as in EXP-CZ-001 on sealed set 2. Primary: the per-member paired difference, adapted minus untrained. Cost, reported and not tested: kept training examples, GPU minutes for sampling and training, adapter size.

## What this cannot tell you

Whether the gain carries over to problems unlike the Forge families; whether a teacher's answers would help more than a member's own (that is EXP-CZ-011); whether the gain survives inside a colony.
