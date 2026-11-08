# EXP-CZ-002 results

Status: REPORTED.

## Primary result

H2.1 was supported. T3 coverage at 4x was 81.625%. The pooled tool reference coverage at 4x was 74.042%. The paired gain was 7.583 points. The exact McNemar p-value was 1.86e-14. The 95% paired bootstrap interval for the gain was 5.667 to 9.542 points. The observed power for a 3-point gain was 0.847.

T3 realizable accuracy was 79.500%. It is reported only and is not the primary endpoint.

## Secondary and outline results

H2.2 was supported. The frozen team arm beat the selected non-oracle comparator by 28.417 points in the decomposable regime and 26.917 points in the sequential regime. Both Holm-adjusted tests rejected, and neither regime was worse.

H2.3 was not supported. T3 and P had the same reported novel-solve count.

H2.4 was supported. T3 beat T2 at 4x by 13.667 points. The Holm-adjusted p-value was 6.32e-95.

H2.5 was supported as a separately reported tool-effect comparison. T2 beat the pooled text reference at 4x by 10.000 points. The Holm-adjusted p-value was 1.41e-15. This result cannot satisfy the H2.2 outline gate.

## Reported-only metrics

These descriptive values do not change the confirmatory result. Coverage is the fraction of all scored tasks reached within the stated cut. Realizable accuracy uses only tasks reached within the cut. `U` and `U_tool` are non-realizable pooled references, so their realizable-accuracy values are not meaningful at every cut and must not be cited.

| Arm | 1x coverage | 1x realizable accuracy | 2x coverage | 2x realizable accuracy | 4x coverage | 4x realizable accuracy |
|---|---:|---:|---:|---:|---:|---:|
| A0 | 24.583% | 24.583% | 42.875% | 42.875% | 42.875% | 42.875% |
| A1 | 13.708% | 13.708% | 28.667% | 25.125% | 44.792% | 34.750% |
| A2 | 23.583% | 21.917% | 44.375% | 37.625% | 57.958% | 51.833% |
| A3 | 1.125% | 0.000% | 31.917% | 5.458% | 63.375% | 42.667% |
| A4a | 0.000% | 0.000% | 13.750% | 13.750% | 61.417% | 54.583% |
| A4b | 10.042% | 10.042% | 54.625% | 54.625% | 85.292% | 79.708% |
| CK | 10.042% | 10.042% | 43.125% | 43.125% | 71.583% | 71.583% |
| P | 10.042% | 10.042% | 54.625% | 54.625% | 81.583% | 79.500% |
| T1 | 10.042% | 10.042% | 43.125% | 43.125% | 67.958% | 67.958% |
| T2 | 10.042% | 10.042% | 43.125% | 43.125% | 67.958% | 67.958% |
| T3 | 10.042% | 10.042% | 54.625% | 54.625% | 81.625% | 79.500% |
| U | 12.833% | not meaningful | 33.208% | not meaningful | 57.958% | not meaningful |
| U_tool | 7.208% | not meaningful | 42.625% | not meaningful | 74.042% | not meaningful |

## Amendments and operations

Six disclosed, hash-only amendments preceded scoring. A1 accepted an already-recorded identity binding in specific text-ledger headers. A2 and A3 corrected authentication and release verification. A4 corrected scorer-output staging. A5 replaced one scorer acceptance rule without changing scoring math, thresholds, task bytes, or ledger bytes. A6 aligned the live source-hash check with the authenticated A5 scorer. No score existed before any amendment. The commitment chain and Bitcoin anchors are in [public commitments](../../public-commitments/EXP-CZ-002.md).

Operational disclosures, including attempted-run recovery and publication transport changes, are in [OPERATIONS.md](OPERATIONS.md). They do not disclose salts, sealed locations, task content, or per-task outcomes.

The raw evidence files keep the runtime paths they were recorded with.

## What this does not show

T1 `difficulty` beat `family` by +50 to +71 dev solves per member. `family` remains frozen. T3 and P have identical dev per-cell accuracy, 0.7925, and 66 novel solves each. H2.3 has little dev support. T1 and T2 tie at every repair cap for Quinn because repair fired on only two episodes. R=1 comes from a flat curve. `ck-quinn`, `ck-quentin`, `team-a3`, and `team-a4b` have budget-stop truncation notes. Uncapped descriptive values remain truncated.

This result is limited to executable shortcuts in the founders pool and this instrument. It makes no storage claim. It does not establish a result outside this task family, for larger members, or for general intelligence.
