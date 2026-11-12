# EXP-CZ-002b results: Season 1 Council and measured elimination

Status: REPORTED and REVEALED 2026-11-11. Sealed run r001, scored once.
Score file `score.json` SHA-256 938afc62dd3f4106ea2827805f71274d3ad0e0754f3724aff4b5a80904a63dc7 (schema
cz.exp002b.score.v1, mode sealed, kit manifest 534c1cdc). Nothing below was computed before POSTRUN and BEACON were
anchored.

## Result in one paragraph

Measured elimination removed Grace. The four-member team T3(F) and the three-member team without Grace, T3(F minus
grace), solved exactly the same 2,436 of 3,000 sealed tasks at the 4x budget: zero tasks went either way. Under the
frozen rule that is NONINFERIOR (H2b.1), not SUPERIOR, and both regime tests (H2b.3) are NONINFERIOR. Measured
removal did not beat random removal (H2b.2): the team without Grace solved 5 tasks the team without Graham missed and
the reverse happened 0 times, exact McNemar p = 0.0625, NOT SUPPORTED. The plain reading is narrower than the labels:
Grace was never called on the sealed set, so removing her could not change anything. This run shows that measured
contribution found an idle member. It does not show that eliminating an active member is safe (see "Grace was idle").

## Primary and secondary tests (V, 3,000 tasks, 4x)

| Test | Comparison | Difference (points) | Discordant pairs | Statistic | Label |
|---|---|---|---|---|---|
| H2b.1 primary | E minus N | 0.00 | 0 and 0 | Tango 95% [-0.13, +0.13]; McNemar p = 1.0 | NONINFERIOR (delta 2.0) |
| H2b.2 | E minus R | +0.17 | 5 and 0 | exact McNemar p = 0.0625; Holm p = 0.0625 | NOT SUPPORTED |
| H2b.3 decomposable | E minus N, 1,500 tasks | 0.00 | 0 and 0 | noninferiority p = 3.2e-8; Holm p = 9.5e-8 | NONINFERIOR |
| H2b.3 sequential | E minus N, 1,500 tasks | 0.00 | 0 and 0 | noninferiority p = 3.2e-8; Holm p = 9.5e-8 | NONINFERIOR |

N is T3(F) with all four members, E is T3(F minus e) with e = grace, R is T3(F minus r) with r = graham. The
secondaries are confirmatory because H2b.1 reached NONINFERIOR (fixed-sequence gatekeeping, one Holm family at 0.05).
The paired bootstrap sensitivity interval for H2b.1 is [0, 0] (10,000 resamples, seed 0). No arm was void; the
DEGENERATE label was not assigned (see below).

## Reported-only metrics

Realizable accuracy (verified exact solve of the final answer, metrics_v2 denominator 3,000):

| Arm | 1x | 2x | 4x | Coverage at 4x | Mean charged cost at 4x |
|---|---|---|---|---|---|
| N, T3(F) | 10.13% | 56.13% | 81.20% | 83.13% | 409.6 |
| E, T3(F minus grace) | 10.13% | 56.13% | 81.20% | 83.13% | 409.6 |
| R, T3(F minus graham) | 10.13% | 56.13% | 81.03% | 81.93% | 412.3 |
| P, placebo on F | 10.13% | 56.13% | 81.20% | 83.07% | 402.3 |
| U_tool, union of four sampled T1 runs | 8.23% | 43.80% | 73.17% (accuracy) | 73.17% | 847.0 |

U_tool realizable accuracy is null by definition (non-realizable union reference); its row shows accuracy. The
budget cap is equal across arms; charged cost may differ under it.

Per family at 4x (realizable accuracy; U_tool coverage):

| Family | N and E | R | P | U_tool |
|---|---|---|---|---|
| arith_chain | 100.0% | 100.0% | 100.0% | 92.7% |
| graph_reach | 100.0% | 99.9% | 100.0% | 91.7% |
| json_extract | 70.1% | 70.0% | 70.1% | 36.3% |
| list_transform | 54.7% | 54.3% | 54.7% | 72.0% |

Episode stop reasons: N and E identical (agree 1,948, agree after repair 363, budget 4, fallback 685). R differs a lot
(agree 1,451, after repair 71, budget 178, fallback 1,300): without Graham the team agrees far less often and falls
back far more, yet loses only 5 tasks net, because the fallback answers are about as good.

Executor results across all evaluation ledgers: 72,619 ok, 8,518 error (program errors, scored as such), 34
cpu_limit, 17 mem_limit, 0 internal. Sandbox incidents: 0. Peak GPU memory figures are Corsair results, not 16 GB
evidence (D-37c).

## Grace was idle

Grace held no T3 role in F (roles: arith_chain quinn and quentin; graph_reach graham and quinn; json_extract quentin
and graham; list_transform quinn and graham). Her only entry in F's configuration was the list_transform route of the
A2 fallback router. On V she took 0 turns in T3(F) and 0 in P. All 685 fallback episodes in N (404 list_transform,
265 json_extract, 16 arith_chain) took their answer from the team's own round-0 candidates, the same in N and E, so
the router entry naming her was never consulted. E therefore ran the same episodes as N, token for token (2,827,360
recorded tokens in both ledgers), with the same outcome on every task.

The preregistered DEGENERATE rule compares configuration identity (role table, router rules, member hashes, every
setting). F and F minus grace differ in that router entry, so the identities differ, the kit recorded
`degenerate: false` at SELECT, and the scorer applied the noninferiority labels. That is the rule as frozen and it is
reported as frozen. In substance H2b.1 and H2b.3 are what the spec calls DEGENERATE: accuracy preserved by
construction, not evidence of noninferiority. The signal was visible before V: on S, c(grace) = 0 in every family
with zero discordant tasks, and T3(F minus grace) recorded exactly T3(F)'s tokens (D-62); in the dev pilot her
removal discordance was 0 (D-59). The identity test should be behavioral (which members can act on any task), not
syntactic; that is a kit defect for the next experiment, not a change to this result.

## Selection on S (1,200 tasks, 4x)

| Member | c(m) | 95% interval | only_full | only_without | Protected |
|---|---|---|---|---|---|
| quentin | +104 | [86, 123] | 104 | 0 | yes, json_extract (+104) |
| quinn | +97 | [74, 120] | 118 | 21 | yes, arith_chain (+27) and list_transform (+70) |
| graham | 0 | [-3, 3] | 1 | 1 | no |
| grace | 0 | [0, 0] | 0 | 0 | no |

Grace and Graham tied on c(m) = 0; the frozen tie-break (fewer only_full) picked e = grace. The only candidate for r
was graham, so the R draw on block 975374 gave r = graham with certainty. Protection was not void and no reduced
configuration was configuration-identical by the kit's rule.

## Council (descriptive, preregistered)

The four members voted before any leave-one-out result existed (COMMIT-COUNCIL, anchored). Two of the four scored
ballots did not parse and count as uniform rankings: Graham's (no OVERALL line) and Grace's (no ARITH_CHAIN line).

| Voter | Least-useful pick | Confidence | Hit against e | Brier | Spearman with c(m) |
|---|---|---|---|---|---|
| quinn | quinn (itself) | 95 | no | 0.902 | 0.316 |
| quentin | graham | 86 | no (graham tied with e on c = 0) | 0.740 | 0.738 |
| graham | INVALID, uniform | | | | |
| grace | INVALID, uniform | | | | |

Borda aggregate (uniform ballots add 1.5 to everyone): graham 4.0, grace 6.0, quinn 6.0, quentin 8.0. The Council's
pick is Graham, which is r, not e. On V the team without the Council's pick solved 5 fewer tasks than the team
without e (H2b.2, not significant). Baselines: a uniform voter hits 0.25 with expected Spearman 0; ranking by the
packet's dev T1 solve totals picks Grace (a hit) with Spearman 0.738, as good as the best voter. Per-family Spearman is
undefined for graph_reach (every c_f is 0) and ranges from -0.775 to +0.775 elsewhere. With four voters and 24
orderings none of this can be tested; the Council can only be described.

## Compute

| Phase | Tokens recorded | Cap | Job wall hours | Cap |
|---|---|---|---|---|
| Selection on S (20 jobs) | 12,374,053 | 19,000,000 | 3.76 | 6 |
| Evaluation on V (12 tuples) | 63,604,228 | 97,000,000 | 18.34 | 27 |

Every sealed job passed on its first run; there were no retries. Caps count every sealed ledger of a phase, including
the per-member SC runs that T3 and P read for their fallback (D-59).

## Commitment chain

| Record | File SHA-256 | Anchored |
|---|---|---|
| COMMIT-COUNCIL.txt | 734e83e7... | block 975331 |
| COMMIT-PREGEN.txt | (research repo) | block 975331 |
| COMMIT-PRERUN-S.txt | 5eb2f7d7... | block 975342, before any S task was read |
| SELECT.txt | bc6fb291... | block 975368, before V was generated |
| R draw | block 975374 hash, two explorers | H_SELECT + 6 |
| COMMIT-PRERUN-V.txt | e622d8f2... | block 975377, before any V task was read |
| POSTRUN.txt | c45c43a8... (record b12e3ff1) | block 975487, before scoring |
| BEACON.txt | record 84f7ea25 | H_POSTRUN + 6 |

## Deviations from the preregistration

1. Section 15 cap ruling (D-59): the token and wall caps count the per-member SC runs that T3 and P read, which the
   pilot report had omitted. The kit binds caps recomputed by that rule. Decided at the pilot gate, before freeze.
2. Freeze-plan command fixes (D-61): the plan's inventory glob would have missed the extensionless EXP-CZ-002
   inventory files, and its cz path did not exist. Both overlap audits used the full 13-file inventory from the set 5
   overlap audit and the staged pinned cz binary (SHA-256 f1b8c196). Plan text only; no kit file, binary or bound
   hash changed.
3. Queue daemon restart (D-62): colonyd had loaded its launcher check before the 002b sealed jobs existed and skipped
   them as EXP-CZ-002 jobs. It was restarted while idle. No job had started; no data changed.
4. POSTRUN record writer (D-65): tools/linux/exp002_postrun.py is bound to EXP-CZ-002's 22-tuple layout. The 002b
   record was written by an equivalent hash-only script in the same line grammar (93 file hashes under the evaluation
   root plus 12 ledger roots), checked for symlinks and an exact inventory. The beacon used the EXP-CZ-002 beacon tool
   unchanged.
5. Gate decisions: D-49 calls for Claude and Codex consensus at freeze-class gates. Codex was out of quota from
   2026-11-10, and Chris delegated the PRERUN-S, SELECT, PRERUN-V and POSTRUN gates to Claude alone (D-61 to D-65).
   No preregistered rule was changed after any result was seen.

## What this cannot show

- Whether elimination helps colonies in general: one pool of four, one elimination, one seed, one task suite with an
  executable shortcut.
- Whether removing an active member is safe. The removed member was idle on V (above), so H2b.1 and H2b.3 carry no
  evidence about that.
- Whether measured removal beats random removal. H2b.2 was not supported; 5 to 0 discordance is suggestive at best,
  and the random pick had a single candidate.
- Why a member contributes. Leave-one-out measures marginal value under rule C, not skill; synergies are not
  measured.
- Whether the Council's judgment tracks contribution. Half its scored ballots did not parse, and four voters can only
  be described.
- Whether T3 beats its placebo (P matched N within 0.1 point of coverage) or the tool union. Neither is tested here.
- Anything about trained members, larger models, other families or transfer.

## Published material and what is withheld

The reveal is in ../../public-commitments/reveal/EXP-CZ-002b/ with a SHA256SUMS list. It holds the four freeze-record versions (PREGEN, PRERUN-S, PRERUN-V, POSTRUN), the SELECT and R-draw records, the POSTRUN and BEACON records, score.json, both sealed task sets (S, 1,200 tasks; V, 3,000 tasks) with their generation summaries and sealed manifests, the Council ballots and both salt files. Each file's SHA-256 matches the value committed for it. Both sets are now retired. The release asset exp-cz-002b-ledgers.tar.gz holds the 63 result, ledger and timing files of selection and evaluation and the per-arm outcome files.

Withheld because they fail the publication scanner's zero-findings rule and their bytes are hash-bound, so they cannot be edited: KIT_MANIFEST.json (it records model file locations on the run host) and the Council summary ballots.json (it records the run host's name). Their committed hashes stay public, but they cannot be rechecked from this repository. Also withheld: the timing sidecars of the ut-grace and ut-graham runs (program stderr tails that contain sandbox file paths), server logs, host identity sidecars and driver checks. The POSTRUN record lists every withheld file's hash. The generator and preparation code are not published, so the sets cannot be regenerated from the salts here; the salts let anyone check the salt commitments.
