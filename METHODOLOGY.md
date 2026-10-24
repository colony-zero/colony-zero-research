# Methodology

This page says what each safeguard is and why it exists. It does not publish the code or operators behind them.

## Claim tags and outcome words

Every capability statement carries one tag.

- PROPOSED: designed, not built or tested.
- IMPLEMENTED: built and tested, with no result claimed.
- MEASURED: a result exists, and its run ledger's root hash is published with it. The full ledgers are released with the experiment's reveal package, and anyone can then check them against the published roots.
- REJECTED: tried or considered, and set aside for a stated reason.

Results use one outcome vocabulary: SUPPORTED, PARTIAL, NOT SUPPORTED, INCONCLUSIVE, INFRASTRUCTURE. INFRASTRUCTURE means the run failed for reasons that say nothing about the question, such as a broken setup. Why: it stops a tooling failure from being read as a negative result, and stops a negative result from being hidden as a tooling failure.

## Hash-chained, replayable ledger

Every model call, answer, grade, vote and verdict is appended to a ledger. Each entry includes the hash of the one before it. Why: editing any past entry breaks every later hash, so tampering shows. The ledger can be replayed to rebuild the reported numbers, so a result is not a claim about a run, it is a computation anyone can repeat. In our dev runs, every ledger was replayed and reproduced its reported solve count.

## Sealed evaluation, committed before and revealed after

Task splits are dev (public), test (public, for analysis development) and sealed. The sealed split is generated from a secret salt. Before any run we publish a commitment to the salt and a hash of the sealed task file. After the run we reveal them, and anyone can check that the revealed bytes match. Why: the sealed set is not disclosed publicly or used for any model or template selection before the run, and the commitments make any later change to it detectable. Secrecy alone does not rule out every kind of contamination. The tasks are freshly generated, so no model can have seen these exact items in training, but a model can still be familiar with the task style. Revealed sealed sets are retired and never used for a sealed claim again, and claims of transfer are limited to separately built held-out families. Each preregistration field can also be committed with its own salted hash under one root, so a design can be fixed before a run and selectively revealed after. See public-commitments/README.md.

## Fail-closed promotion

A new generation member is promoted only if it beats its parent on a sealed test. Any of these blocks promotion: mismatched task sets, non-binary outcomes, too few tasks, missing compute accounting, a gain whose bootstrap lower bound does not clear a preset minimum, a non-significant paired test, any regression on a protected suite, or a compute blow-up. Why: when evidence is missing or odd, the safe answer is no. Neither votes nor a controller can promote anyone.

## Compute accounting

We count tokens in and out, a FLOP proxy (2 x active parameters x tokens), wall time and peak memory, including the cost of any controller or verifier. Why: a team that uses eight times the compute and wins by a little has not shown anything about teams. Comparisons are made at equal total compute.

## Statistics

Wilson intervals for rates, exact McNemar tests on paired tasks, paired bootstrap for differences, Holm correction across pairwise comparisons. Anything that evolves or learns uses at least five seeds. Why: these are the standard tools for small, paired, binary outcomes, and fixing them in advance removes the choice of test after the fact.

## Elimination by measured contribution

The member that leaves is the one whose removal hurts the colony least, measured by re-running the colony without it on the evaluator's tasks. Rare specialists can be protected so a narrow but vital member is not removed for being narrow, but only under a threshold, task partition and tie-break rule written down before the season. No exception made after results are visible can change an elimination. The Council still meets, but each vote is a prediction ("this member contributes least"), scored against the measurement. Whether the colony's social judgment tracks real contribution becomes a measured quantity. Why: a popularity vote that decides survival would contaminate the science, and removing members changes which tasks the survivors see.

## The no-elimination twin

Every run with elimination has a twin with the same seeds and no elimination. Why: losing members is not assumed to help. The comparison "does the colony get better after a member is removed?" is itself preregistered, and the twin is its control.

## Crowd votes as a randomized arm

Before a season we publish a menu of vetted, preregistered options. Viewers vote on the menu only. The season's budget is then split between three arms: CROWD (in proportion to votes), RANDOM (uniform over the menu) and PLAN (the maintainers' preregistered choice). All draws derive from a public random value fixed in advance, so anyone can recompute them. Votes sit in a hash-chained ledger with receipts and never touch sealed evaluation, checkers, promotion or scoring. Free-text suggestions are never training input. Why: the votes really move compute, and the comparison of crowd against random against plan is an experiment of its own. Does crowd direction beat chance, and does it beat the maintainers? Status: PROPOSED. No public vote has been held.

## Final Exam from a public randomness source after the freeze

The final test set is not generated until the design is frozen. Its seed comes from a public randomness beacon round that is fixed in the preregistration and published after the freeze. The generator's hash is committed in advance. Why: nobody can know the final tasks early, so nobody can tune to them, and no trusted custodian is needed. Limits: this defeats peeking, not overfitting to the task generator, so claims about transfer also need task families written after the freeze. Each confirmatory set is used once and then retired, along with anything derived from it.

## Task families and prompts

The first suite has four machine-checked task families (arithmetic chains, graph reachability, JSON extraction and list transforms) at difficulties 1 to 5. Each member is asked in one of four prompt templates: plain, two worked examples, a format line, or step-by-step. An independent exact checker grades every answer, and format failures are counted separately from wrong answers. The suite is rescaled if a family is too easy or too hard for every member, and this is done in a versioned way before any claim is made.
