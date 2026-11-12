# EXP-CZ-002b preregistration

This is the specification text frozen at candidate commit a7dc7a0 (file SHA-256 8eed6db70e329e8464c6c9fee65031dea381a657f7efbb4cb5f169b092762688), published after the run with the results. It was bound before any sealed task existed through COMMIT-PREGEN (kit manifest and source hashes) and anchored in Bitcoin block 975331. Publication edits, and nothing else: a private secrets path, host names, run-host directory paths and one tool directory name are replaced with generic words, and one formula is written with "over" instead of a slash, so this file's hash differs from the frozen one. The original title says DRAFT SPEC because the file kept its working name; this is the version that was frozen and run.

---

# EXP-CZ-002b: Season 1 Council and measured elimination (DRAFT SPEC)

Status: APPROVED 2026-11-09 at the experiment-class gate (D-58; section 22 answered as recommended; no Codex review
ran, Chris approved directly). Not frozen, no manifest, no salt. Nothing here read a sealed task, ran a model or saw a result. Every number a pilot must
set is marked TBD-PILOT. Numbers marked PROPOSED are design choices fixed at spec approval, never by the pilot.

Sources: D-56 (the decision this spec carries out; it is final), the supporting consensus codex-next-question-r2,
docs/ROADMAP.md (ground rules, Season 1), docs/FRONTIER.md (random-elimination control), docs/COLONY.md (members,
1B weight class D-55), ADR-0006 (preregistration, sealed sets, fail-closed), ADR-0011 (measured contribution decides,
votes are predictions, no-elimination twin), ADR-0012 (confirmatory set generated after the design is frozen),
experiments/EXP-CZ-002 (the template, pool, T3 protocol, freeze and publication machinery), and D-21, D-25, D-37,
D-41 to D-55. EXP-CZ-003a is cited only for what it found; its router and its elimination candidate are not imported.

## 1. Question

After the Council predicts which member is least useful, does removing the member with the lowest measured marginal
contribution preserve or improve the colony's verified accuracy, compared with an unchanged no-elimination T3 twin,
on a fresh sealed evaluation partition that was not used for selection? And does measured removal beat a
preregistered random removal?

## 2. Why this experiment exists

Season 1 (The First Colony) has two decisions: does the colony beat its best member, and the first elimination
(ROADMAP, D-21). EXP-CZ-002 answered the amplification half: T3 covered 81.6% of sealed set 5 against 74.0% for the
pooled tool union (H2.1 SUPPORTED). It did not show that T3 beats its placebo P (H2.3 NOT SUPPORTED: identical
novel solves). Its Council ran only as a reported-only add-on (D-46 answer 6). No member has been eliminated under a
controlled design. A stage advances only after the previous gate's decision is recorded, so Season 1 closes here.

The controlled test of elimination is also one of the four Season 1 "firsts" in docs/FRONTIER.md: leave-one-out
elimination against a no-elimination twin and a random-elimination arm, and Council votes scored as forecasts of
peer contribution.

## 3. Design in one paragraph

The EXP-CZ-002 pool of four founders forecasts, as the Council, which member contributes least; the ballots are
committed hash-only before any contribution result exists. A dev pilot on public tasks sets the open parameters by
preregistered rules. The kit is frozen. A fresh sealed selection partition S is generated and every leave-one-out T3
configuration runs on it once; the member with the lowest measured contribution that is not niche-protected is
chosen and the selection record is committed and anchored. A random member is then drawn from a public Bitcoin
block value. Only after that, a second fresh sealed evaluation partition V is generated. Arms E (T3 without the
measured pick), N (unchanged T3) and R (T3 without the random pick), plus the anchors P and U_tool(4x), run once on V
at the same 4x budget on the Radeon 8050S. The primary test is one hierarchical rule on E minus N: noninferiority
first, then superiority.

## 4. Pool and eligibility

- Pool F: the frozen EXP-CZ-002 pool, Graham, Quinn, Grace and Quentin (experiments/EXP-CZ-002/POOL.json, D-48),
  with the same GGUF hashes, templates, chat settings and X1/X2 templates and example hashes as the EXP-CZ-002 kit.
  All four are founders (Generation 0) and all are within the 1B weight class (D-55: at most 1.1B stored
  parameters; the largest is Quinn at about 0.8B).
- Why this pool: N must be the T3 colony that EXP-CZ-002 measured, so P and U_tool stay comparable as anchors and
  the Season 1 elimination happens to the colony that Season 1 built. Juno (MiniCPM5-1B, D-55) is not cast here: it
  has no X templates, no T1 history and no EXP-CZ-002 role, and adding it would change the colony being tested.
- Elimination eligibility: every member of F is a candidate unless niche-protected (section 7.4). Exactly one
  member leaves in E and exactly one in R.
- The experiment does not change the member registry. Archiving E's member (docs/COLONY.md: an eliminated member
  keeps its name and row) is a separate registry-class gate after the report (section 14).

## 5. Tasks, partitions and overlap audit

- Forge v0.0.2, checker v3, all four families (arith_chain, graph_reach, json_extract, list_transform),
  difficulties 1 to 5, as in EXP-CZ-002. Regimes as in EXP-CZ-002: decomposable (arith_chain, list_transform) and
  sequential (graph_reach, json_extract).
- Dev 0-399 (public): pilot only. Dev 400-479: example pool, never scored (X1 examples, unchanged).
- Selection partition S (sealed, new salt S): PROPOSED 1,200 final tasks, 300 per family, 60 per family/difficulty
  cell. Used only to measure contribution, apply niche protection and score the Council. Never scored for any
  hypothesis.
- Evaluation partition V (sealed, new salt V, independent of salt S): TBD-PILOT size from the ladder 2,400, 3,000 or
  3,600 final tasks (section 11), balanced 120, 150 or 180 per cell. Generated only after the selection record is
  anchored (section 13), so V does not exist while selection happens (ADR-0012 spirit).
- Both partitions follow the EXP-CZ-002 generation rule: Forge creates a fixed candidate headroom per cell (150 per
  cell for the S size; for V, 1.25 times the per-cell final count, rounded up), `cz sealed-prep` filters against
  every public set, and the first survivors per cell in Forge order form the final domain.
- Overlap audit, run on each final domain before it is committed: zero overlap with every public split, with every
  earlier sealed set and consumed attempt (sets 1 to 5, including EXP-CZ-002 attempts 001, 003, 004 and 005), and,
  for V, zero overlap with S. Overlap inside a final domain or against the inventory voids that attempt; ordinary
  prep exclusions and headroom trimming do not.
- Salts live only in a private secrets directory on the storage host, mode 0600, as in EXP-CZ-002. They are
  never printed, copied to the Corsair, put in a gate packet or delegated.

## 6. Arms

| Arm | What it is | Produced by | Role |
|---|---|---|---|
| N | T3 configured from the full pool F by rule C | `cz-toolprobe team --arm T3` | Control (no-elimination twin, ADR-0011) |
| E | T3 configured from F minus the measured pick e by rule C | `cz-toolprobe team --arm T3` | Primary arm |
| R | T3 configured from F minus the random pick r by rule C | `cz-toolprobe team --arm T3` | Secondary control (FRONTIER) |
| P | N with tool output blanked, fuel still charged | `cz-toolprobe team --arm P` | Descriptive anchor, outside every test |
| U_tool(4x) | Pooled independent T1 `family` samples from F, round-robin, summed cost up to 4x | sampled runs, offline | Descriptive anchor, outside every test; realizable accuracy is null |
| Council | Member ballots forecasting least useful member | ballot job, section 8 | Scored forecasts; never selects |

E, N and R run on identical V tasks, with identical seeds (seed 0), templates, sampler settings, executor limits,
runtime and budget. They differ only in the member set given to rule C. No EXP-CZ-003a router, member or elimination
candidate is used anywhere. Budgets 1x and 2x are reported as prefixes of the 4x runs and enter no test.

## 7. Definitions

### 7.1 Cost and equal compute

As in EXP-CZ-002 section 7. The cost of an episode is prompt tokens plus generated tokens over every model call,
every member and every turn (prompt tokens count in full even when the server cache reuses them), plus the executor
charge `ceil(fuel_used x r over 1e9)` per call. The budget unit 1x and the rate r are re-measured in the pilot by the
EXP-CZ-002 formulas (TBD-PILOT; the EXP-CZ-002 values, 258.165 tokens and r = 18, are references only). Each arm's
answer at budget B is the last candidate whose cumulative cost was at most B when it appeared.

Equal all-in charged compute means: E, N and R are scored at the same per-task cap B = 4x on the same cost
definition, which includes every controller, verifier, repair and fallback call. The one-time selection overhead (the
leave-one-out runs on S and the Council) is a season cost. It is reported separately, and amortized per evaluation
task as a reported-only figure; it does not enter the primary comparison.

### 7.2 Configuration rule C

For any member set M, rule C builds T3(M) exactly as the EXP-CZ-002 kit built T3, restricted to M:

- T3 roles per family: X is the member of M with the most dev 0-399 T1 `family` solves in that family (seed 0, 002b
  pilot runs), Y the second; ties by committed POOL.json order. TBD-PILOT: the role tables for F and each F minus m.
- A2 fallback inside T3: the family rules router refit on dev 0-399 over M only, best-single fallback as in
  EXP-CZ-002, self-consistency at the T3 budget. TBD-PILOT: the router rules for F and each F minus m.
- Repair: once, as in the EXP-CZ-002 T3 protocol. Every other T3 setting is unchanged.

Rule C is applied by code, never by hand. If M has fewer than two members with at least one dev T1 solve in some
family, rule C cannot be applied and the pilot stops (section 12).

A configuration is identified by its canonical protocol identity (role table, router rules, member hashes, every
setting). Two member sets whose configurations have the same identity are "configuration-identical". This matters:
in EXP-CZ-002, Grace held no T3 role and no A2 routing rule, so removing her may leave T3 unchanged (EXP-CZ-003a saw
the same effect: removing quentin-teacher changed nothing).

### 7.3 Measured contribution (selection partition only)

For each member m of F, on S at 4x:

- c(m) = (S tasks the final answer of T3(F) solves) minus (S tasks the final answer of T3(F minus m) solves). The
  outcome is verified exact solve of the final answer (realizable accuracy, checker v3), the same outcome as the
  primary endpoint.
- only_full(m) = tasks T3(F) solves and T3(F minus m) does not; only_without(m) = the reverse.
- Family-level contribution c_f(m): the same difference within family f.
- Paired percentile bootstrap, 2,000 task resamples, seed 0, for c(m) and each c_f(m), as `cz contribution`.

The formula reads only S outcomes from these five configurations. It never reads V, the Council ballots, dev
outcomes or EXP-CZ-002 sealed results. A configuration-identical reduced pool is not rerun: its outcome vector is
T3(F)'s by definition (the Corsair is self-deterministic, docs/ADMISSION_CORSAIR.md item 5), and this is disclosed.

### 7.4 Niche protection (frozen)

A member m is protected if, in at least one family f, the lower bound of the 95% paired bootstrap interval for
c_f(m) is above zero and c_f(m) is at least 2% of that family's S tasks (6 of 300). This protects a specialist whose
overall contribution is low because it hurts slightly elsewhere. If every member is protected, protection is void
and all members are candidates. Both thresholds are PROPOSED and fixed at approval; the pilot reports, as a
diagnostic only, which members dev data would protect.

### 7.5 The measured pick e and its tie-breaks

e is the unprotected member with the lowest c(m). Ties go, in order, to fewer only_full(m), then more
only_without(m), then member id ascending (the `cz contribution` order). The `cz contribution` eligibility flag
(interval upper bound at or below zero) is reported but does not gate: exactly one member always leaves.

### 7.6 The random pick r (preregistered random control)

- Candidates for r: unprotected members other than e, ordered by member id. Excluding e keeps H2b.2 testable; if r
  could equal e, the test would be empty by construction a third of the time. H2b.2 therefore asks whether measured
  choice beats a random other choice.
- Randomness: the hash of the Bitcoin block at height H_SELECT + 6, where H_SELECT is the height of the first block
  that confirms the OpenTimestamps proof of SELECT.txt (section 13). Nobody can know it before selection ends.
- Draw: index = int(SHA-256("EXP-CZ-002b R" || block_hash_hex || "," joined candidate ids), as a big-endian integer)
  mod k, where k is the number of candidates. The draw code and the string format are frozen in the kit and the draw
  is recomputable by anyone from public data.
- If there are no candidates (every other member protected), R is VOID and H2b.2 is NOT TESTABLE.

## 8. Council protocol

- Voters: the four members of F. No viewer votes exist yet (ADR-0010); none are added.
- Information packet, frozen in the kit: member cards from docs/COLONY.md (name, lab, architecture, size), the four
  family descriptions, the EXP-CZ-001 sealed standings, and each member's dev 0-399 T1 `family` solve counts by
  family from the EXP-CZ-002 r2 pilot. Everything in it predates EXP-CZ-002b. No S, V or 002b pilot result enters.
- Questions, five per voter: rank all four members, including itself, from least to most useful to the colony,
  overall and in each family; give a confidence from 0 to 100 that its least-useful pick is right.
- Generation: a fixed ballot template with a strict line format, greedy seed 0 (the scored ballot), plus seeds 1 to 4
  at the EXP-CZ-002 sampler settings for stability, reported only. A ballot that does not parse is recorded INVALID
  and scored as a uniform ranking. Cap 1M tokens (D-46 answer 6).
- Commitment: ballots are generated first, before any 002b leave-one-out run is scored (dev or S), and committed
  hash-only as COMMIT-COUNCIL.txt with an OpenTimestamps proof. The selection binary takes no ballot input; a kit
  negative test proves that a ballot file cannot reach it.
- Scoring, after SELECT, against measured S contribution: top-1 hit rate of each least-useful pick (chance 0.25);
  Spearman correlation of each ranking with c(m) (overall) and c_f(m) (per family); Brier score of the stated
  confidence on the top-1 pick; the Borda-aggregated Council pick against e. Baselines: uniform, and a heuristic that
  ranks by dev T1 solves. Also reported against dev leave-one-out, descriptively.
- The Council is a preregistered descriptive endpoint, outside the inferential family. With four members there are
  only 24 possible orderings, so the smallest exact permutation p-value is 0.042; no Holm-adjusted test could pass.
  A null is publishable (FRONTIER).

## 9. Hypotheses

| ID | Hypothesis | Fails if |
|---|---|---|
| H2b.1 (primary) | E is noninferior to N on V at 4x (step 1), and if so superior (step 2) | Step 1: lower limit of the 95% paired interval for E minus N is at or below minus delta |
| H2b.2 | E beats R on V at 4x (measured removal beats random removal) | Holm p >= 0.05 |
| H2b.3 (one test per regime) | E is noninferior to N in the decomposable and in the sequential regime | Holm-adjusted interval lower limit at or below minus delta |

Council scoring (section 8) is preregistered and reported, never a hypothesis test that can confirm a claim.

## 10. Endpoints

- Primary: H2b.1, paired difference in verified exact solve rate of the final answer (realizable accuracy over the
  full V task set, `metrics_v2` denominator), E minus N, at 4x.
- Secondary (Holm family): H2b.2, H2b.3 decomposable, H2b.3 sequential.
- Reported only: realizable accuracy and coverage of every arm at 1x, 2x and 4x; P and U_tool(4x) as anchors (U_tool
  realizable accuracy null, crates/cz-toolprobe/src/metrics_v2.rs); E and R against P; per-family and per-cell
  accuracy; c(m), c_f(m), protection status and tie-break path on S; Council scores; cost per task split into prompt,
  generated and executor charge; mean charged cost per arm (E's may be lower than N's; the cap is equal); one-time
  selection overhead; FLOP proxy; executor `internal` count and sandbox incidents (both must be 0); peak GPU memory
  (labelled as Corsair results, never 16 GB evidence, D-37c); stop reasons and budget-stop truncation notes.
- Claims (D-32): deployment feasibility, inference only. Training reproducibility: not applicable.

## 11. Statistics, sample size and power

The primary rule, frozen, one hierarchy on one endpoint at alpha 0.05:

1. Noninferiority: compute the two-sided 95% Tango score interval for the paired difference E minus N. If its lower
   limit is above minus delta, E is NONINFERIOR. delta is PROPOSED at 2.0 points (smaller than the 3-point minimum
   effect EXP-CZ-002 used, so "preserved" means within two points).
2. Superiority, only if step 1 passes: exact two-sided McNemar on the discordant pairs. If p < 0.05 and the observed
   difference is positive, E is SUPERIOR.

Outcome labels, assigned by the scorer: SUPERIOR; NONINFERIOR; INFERIOR (upper limit of the interval below zero and
lower limit at or below minus delta); INCONCLUSIVE (any other failure of step 1); DEGENERATE (E is
configuration-identical to N, see below). Because step 2 is reached only through step 1 on the same endpoint, the
hierarchy keeps the familywise error at 0.05 without splitting alpha. The paired bootstrap interval (10,000
resamples, seed 0) is reported as a sensitivity check only.

Secondaries: H2b.2 by exact McNemar, H2b.3 by the Tango noninferiority score test (p-values for Holm) with Holm-adjusted
intervals, one Holm family at 0.05. They are confirmatory only when H2b.1 reaches at least NONINFERIOR
(fixed-sequence gatekeeping); otherwise they are reported with the same numbers, labelled exploratory.

DEGENERATE case: if T3(F minus e) is configuration-identical to T3(F), E is not rerun on V (its outcomes are N's by
definition), H2b.1 and H2b.3 are labelled DEGENERATE (accuracy preserved by construction, not evidence of
noninferiority), and H2b.2 becomes the single confirmatory test at alpha 0.05. This rule is preregistered before any
result exists; the report states it plainly.

Sample size, the power rule: the pilot runs T3(F) and each T3(F minus m) on dev 0-399 at 4x and takes d_dev, the
largest paired discordance between T3(F) and any reduced configuration that is not configuration-identical
(TBD-PILOT). Power is computed by Monte Carlo of the exact frozen step-1 rule (Tango interval) under a paired
multinomial model with true difference zero and discordance d_dev split evenly, 20,000 replicates, seed 0. n_V is the
smallest of 2,400, 3,000 and 3,600 with power at least 0.80 (TBD-PILOT); if none reaches 0.80, the status is OPEN for
a spec change. For scale (normal approximation, delta 2 points, true difference 0): at d = 0.10, 2,400 tasks give
about 0.87; at d = 0.15, 3,000 tasks give about 0.81; at d = 0.20 even 3,600 give about 0.76 (OPEN). If every
reduced configuration is configuration-identical, n_V is 2,400 and power is computed for H2b.2 instead, at the
largest dev discordance between T3(F) and any reduced configuration that R could draw.

## 12. Dev pilot (public tasks; runs unattended after this spec is approved, D-45)

All runs on the Corsair 8050S as colonyd jobs, `LLAMA_ARG_CACHE_RAM=0` (D-50), run tag fresh for 002b.

0. Council ballots (section 8), committed as COMMIT-COUNCIL before step 3 is scored.
1. Smoke: T3(F) on dev 0-39, twice; ledgers identical.
2. `cz-exec bench --n 200` and A0 greedy for Quinn on dev 0-399: 1x and r (TBD-PILOT).
3. T1 `family` seed 0 for each member on dev 0-399 at 8x: rule C role tables and routers for F and each F minus m
   (TBD-PILOT). Whether F's roles equal the EXP-CZ-002 frozen roles is reported.
4. T3(F) and each non-identical T3(F minus m) on dev 0-399 at 4x, seed 0: d_dev, dev leave-one-out (diagnostic
   only), mean tokens per task.
5. P and U_tool(4x) samples on dev 0-399, seed 0: anchors and token estimates.

Choices fixed from the pilot by rule and written to the kit: 1x and r; role tables and routers per member set;
configuration identities and the list of configuration-identical reduced pools; d_dev and n_V; token and wall caps
(section 15). The report's top-level status is FREEZABLE or BLOCKED, as in EXP-CZ-002 section 11a.

Pilot stops (ask for a spec change, never re-tune): rule C cannot be applied to some member set; N's dev realizable
accuracy at 4x is above 97% (no room to show harm or gain); the power rule is OPEN; any required unit is incomplete
or budget-censored under the D-52 rule. The dev leave-one-out ranking never selects anything; selection happens only
on S.

## 13. Commitment sequence

Each public file holds labelled SHA-256 lines only, is pushed to the public research repo and stamped with
OpenTimestamps (tools/ots_check.py, two explorers), as in the EXP-CZ-002 freeze plan.

| Step | Record | Binds | Before |
|---|---|---|---|
| 1 | COMMIT-COUNCIL.txt | ballot file hashes, ballot template and packet hashes | any 002b leave-one-out score |
| 2 | COMMIT-PREGEN.txt | private freeze record, canonical kit manifest, binaries, scorer, selection code, R-draw code, salt S and salt V commitments | generation of S |
| 3 | COMMIT-PRERUN-S.txt | freeze record, S file hash, S overlap summary | any S task read by a model |
| 4 | SELECT.txt | S ledger roots of the five configurations, c(m) table, protection, e | generation of V |
| 5 | COMMIT-PRERUN-V.txt | SELECT hash, the R block hash and r, V file hash, V overlap summary (including against S) | any V task read by a model |
| 6 | POSTRUN.txt | private POSTRUN record (ledger roots of every V tuple) | scoring |
| 7 | BEACON.txt | beacon record, as in EXP-CZ-002 | scoring release |

The sealed driver and the scorer rebuild the canonical kit manifest from what they load and stop on any mismatch
before a sealed task is read (D-53 pattern). Amendments, if ever needed, follow the D-54 pattern: written before any
score exists, scope stated, hash-only, anchored before scoring, disclosed.

## 14. Gates

Classes follow D-49 and the gate reviewer (colony_gate_review.py). Packets carry no salt value, task content or sealed
path; the next-kit packet redaction (`_redact_packet_text`, PACKET_REDACTIONS.json) strips host, salt, sealed and
task paths, closing the EXP-CZ-002 defect (OPERATIONS.md item 13).

| Step | Who |
|---|---|
| Approve this spec | Consensus gate, class experiment |
| Build and test the 002b kit, smoke, bench, pilot, pilot scoring, kit to FREEZABLE, dry run with injected mismatches | Unattended (D-45) |
| A pilot stop or any wish to change an arm or rule | Consensus gate, class experiment (spec change) |
| COMMIT-COUNCIL push (hash-only) | Consensus gate, class freeze |
| Freeze: PREGEN, salts S and V created on the storage host, S generation, prep and audit, PRERUN-S | Consensus gate, class freeze; salt work is a main-session action, never delegated |
| Selection runs on S | Unattended once the freeze is approved |
| SELECT push, R draw, V generation, prep and audit, PRERUN-V | Consensus gate, class freeze |
| Evaluation runs on V | Unattended |
| POSTRUN and BEACON pushes (hash-only) | Consensus gate, class freeze |
| Scoring after the beacon; REPORT.md draft | Unattended |
| Reveal S and V salts and sets | Consensus gate, class reveal |
| Publish the report or results | Per the owner ruling of 2026-11-08, a consensus gate; see section 18 |
| Archive E's member in docs/COLONY.md | Consensus gate, class registry, after the report |
| Any download, spend, host change (fast lane), family system | Downloads: consensus (open weights only, sha256). Spend, host, family: Chris only |

A job that fails twice is parked and reported (D-45). Kill switch: runs/gate-review.off.

## 15. Compute and accounting

- Host: the Corsair AI Workstation 300, Radeon 8050S, inside colony.slice, within the 55 GiB GPU
  budget (D-44). Every arm, the pilot and both sealed phases run on this one host (D-42); the RX 9070 XT fast lane is
  not used. the storage host does orchestration, storage, Git, OpenTimestamps and the light CPU sealed-set generation, prep
  and audit only, as in EXP-CZ-002. No API, no teacher or judge model; spend cap 0 USD.
- Token caps: recorded prompt plus generated tokens across all sealed ledgers of a phase. Selection-phase cap and
  evaluation-phase cap are each 1.5 times the pilot's measured mean tokens per task for that phase's tuples, times
  the phase's task count, rounded up to the next million (TBD-PILOT). The pilot measures real multi-turn prompt
  resends, the failure that stopped EXP-CZ-002 r005. For scale only: EXP-CZ-002 r006 used 76.3M tokens for about 22
  tuples on 2,400 tasks; 002b runs up to five T3 tuples on S and three T3 tuples, P and four U_tool member runs on V.
- Wall caps: 1.5 times the pilot-scaled estimate per phase (TBD-PILOT). Caps persist across retries and resumes.
- Run layout: sealed runs under the sealed runs root for EXP-CZ-002b (selection and evaluation folders). Any
  superseded or failed attempt is quarantined to a sibling superseded folder,
  as `tools/linux/cz_runs_layout.py` (`quarantine_root`) computes it; `inventory_files` refuses a quarantine
  directory inside the scanned runs root (the EXP-CZ-002 defect, OPERATIONS.md item 16). Live checkpoints are not
  involved; no training runs.

## 16. Stopping rules

- Science: none stops the run early. Every arm runs once on V and is scored by the frozen rule. A null, negative,
  INCONCLUSIVE or DEGENERATE result is not rerun and does not resize V.
- Safety: any sandbox escape, successful network attempt or file access outside the sandbox library directory stops the run, voids the arm
  and is reported.
- Infrastructure: an executor `internal` result stops the run (resume retries); twice parks the job. A void arm makes
  its tests INFRASTRUCTURE, not NOT SUPPORTED. A void N or E voids H2b.1; a void R makes H2b.2 NOT TESTABLE.
- Budget: the phase token cap or wall cap stops the run. A stopped phase is not scored; a fresh attempt needs a
  freeze-class gate and a fresh sealed set, with all evidence preserved (D-54 pattern).
- Sealed integrity: overlap in a final domain, a V task in S, any sealed task found in a public file, or a changed
  bound file voids that attempt before scoring. A V generated before SELECT is anchored voids V.
- Selection integrity: any evidence that selection read a ballot, a V task or a dev leave-one-out result voids the
  selection; the selection is redone on a fresh S.

## 17. Required evidence

Hash-chained ledgers with `turn`, `tool_call`, `attempt` and `verdict` events and timing sidecars for every pilot,
S and V tuple; host_id and llama_env per job (D-50); the canonical kit manifest and every bound hash (binaries,
executor, scorer source and binary, rule C code, selection code, R-draw code, ballot template and packet, role
tables, routers, configuration identities); the ballot file; the c(m) table with intervals; the R block height and
hash; all seven public records with OpenTimestamps proofs; the scorer output with `reported_metrics_v2`; REPORT.md
with "Deviations from the preregistration" and "What this cannot show".

## 18. Publication

- Chris ruled on 2026-11-08 that Colony Zero publication no longer waits for him; publication is a D-49 consensus
  gate. Before it can run as one, docs/DECISION_REGISTER.md needs an entry recording that ruling, and
  `OWNER_ONLY` in the gate reviewer (colony_gate_review.py) (which still lists `publish`) must change; until then the
  reviewer escalates publish gates to Chris.
- Method details of the elimination operator are YELLOW under docs/PUBLICATION_POLICY.md (selection operators in
  detail). The publication gate decides that explicitly; the result page, commitments and released ledgers are
  GREEN after the scan.
- Every public text (REPORT, result page, released ledgers and manifests) passes
  `tools/linux/cz_publish_scan.py --json <paths>` with zero findings before staging; host aliases, secrets roots,
  ssh key paths and host IPs are rejected. Staging follows the EXP-CZ-002 PUBLISH_PLAN pattern (reviewed commits,
  clean worktrees, a POSTRUN allowlist for released tuples). Consumed but unscored attempts stay sealed.
- Salts and sets of S and V are revealed with the results (reveal gate) and then retired.

## 19. What must exist before freeze

1. This spec approved at the experiment-class gate, with section 22 answered.
2. The next-kit tooling accepted: `cz_publish_scan.py`, `cz_runs_layout.py`, `metrics_v2.rs` and the gate-packet
   redaction, with its open review findings closed by consensus (commit ca680d7 is fix round 2).
3. A 002b kit: rule C as code, the selection program (sections 7.3 to 7.5), the R-draw program (7.6), the ballot job
   and parser (8), and the scorer for sections 10 and 11 (Tango interval and test, exact McNemar, Holm, the outcome
   labels including DEGENERATE, metrics_v2). A kit-only build with every non-kit entrypoint compiled out, as D-53.
4. Negative tests: selection refuses ballot, V and dev inputs; scorer refuses mismatched task sets; driver stops on
   an injected manifest mismatch; quarantine inside the runs root is refused; a gate packet with a salt, sealed or
   host path is redacted and recorded; the scanner rejects a planted host path.
5. A FREEZABLE pilot report binding every TBD-PILOT value, and COMMIT-COUNCIL anchored.
6. A 002b freeze plan with executable blocks, modelled on experiments/EXP-CZ-002/FREEZE_PLAN.md, including fixed
   paths for both partitions and the inventory for both overlap audits.
7. A dress rehearsal on dev data of the full chain (selection, SELECT, R draw on a test block value, evaluation,
   scoring), on the exact candidate commit.
8. The secrets directory on the storage host present as a physical non-symlink directory; no salt yet.

## 20. What this cannot show

- Whether elimination helps colonies in general. One pool of four, one elimination, one seed, one task suite with
  an executable shortcut. ROADMAP's five-seed rule targets things that learn or evolve; this is one selection event,
  not a lineage.
- Whether removal helps when the removed member was idle. If E is DEGENERATE, the result shows only that measured
  contribution found a member the configuration did not use.
- Why a member contributes. Leave-one-out measures marginal value in this configuration under rule C, not skill;
  Shapley-style synergies (ADR-0011) are not measured.
- Whether the Council's judgment tracks contribution in any statistical sense. With four voters and 24 orderings the
  Council can only be described.
- Anything about trained members, Juno, larger models, other families or transfer. In-family claims only; no claim
  of general intelligence (D-04).
- Whether T3 beats its placebo. EXP-CZ-002 did not show it (H2.3) and this experiment does not test it.

## 21. Deviations from D-56 and the consensus, fixed in this draft

1. Selection uses a sealed selection partition S, not public dev. D-56 requires a fresh evaluation partition not
   used for selection; the consensus says "dev-measured". Public dev 0-399 already fixed every EXP-CZ-002 choice, and
   its T3 results were visible before the Council. S plays the role of dev for selection only: the contribution
   formula reads no evaluation data.
2. R draws among unprotected members other than e, so H2b.2 is never empty by construction.
3. The primary interval is the Tango score interval, deterministic and well behaved for paired differences with low
   discordance; EXP-CZ-002's paired bootstrap stays as a sensitivity check.
4. A DEGENERATE outcome label and its rule are added, because rule C can make a reduced configuration identical to N.
5. The Council is a descriptive endpoint, not a hypothesis, because four voters cannot reach significance.

## 22. Open questions for the gate

1. DEGENERATE risk: Grace held no EXP-CZ-002 T3 role and no router rule, so E may equal N. Accept the preregistered
   DEGENERATE rule (recommended: it is honest, and H2b.2 then carries the confirmatory test), or restrict candidates
   to members that hold a role or routing rule (changes the question)?
2. delta = 2.0 points for noninferiority? Recommended: yes.
3. S size 1,200 and the niche thresholds (interval lower bound above zero and at least 2% of a family)? Recommended:
   yes.
4. Should archiving E's member follow the report whatever the outcome? Recommended: yes, per ADR-0011; an archived
   member can return through a later preregistered menu (ADR-0010).
5. V salt only, or V seeded from salt plus a beacon value fixed after SELECT (ADR-0012 design)? Recommended: salt
   only, generated after SELECT is anchored; beacon seeding is not implemented yet.

## Appendix: TBD-PILOT items

| Item | Rule that sets it |
|---|---|
| Budget unit 1x | A0 Quinn mean cost on dev 0-399 (EXP-CZ-002 section 7) |
| Executor rate r | bench and generation speed on the Corsair (EXP-CZ-002 section 7) |
| T3 role tables for F and each F minus m | rule C, section 7.2 |
| A2 fallback routers for F and each F minus m | rule C, section 7.2 |
| Configuration identities and the configuration-identical list | rule C, section 7.2 |
| d_dev | section 11 |
| n_V (2,400, 3,000 or 3,600, else OPEN) | section 11 power rule |
| Selection-phase and evaluation-phase token caps | section 15 |
| Selection-phase and evaluation-phase wall caps | section 15 |
