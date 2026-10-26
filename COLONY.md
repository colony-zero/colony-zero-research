# The colony

Every member has a name, so the colony can be followed season after season. A name belongs to one model at one revision. An offspring gets its own name and records its parent. A member that is eliminated keeps its name and its row.

## Generation 0, founding members

| Name | Model (Hugging Face repo) | Lab | Architecture | Parameters | Licence | Joined | Status |
|---|---|---|---|---|---|---|---|
| Quinn | Qwen/Qwen3.5-0.8B | Alibaba Qwen | Hybrid: Gated DeltaNet and attention | about 0.8B | Apache-2.0 | Season 0 | Active |
| Quentin | Qwen/Qwen3-0.6B | Alibaba Qwen | Transformer | about 0.6B | Apache-2.0 | Season 0 | Active |
| Grace | ibm-granite/granite-4.0-h-350m | IBM | Hybrid: Mamba-2 and attention | about 340M | Apache-2.0 | Season 0 | Active |
| Sam | HuggingFaceTB/SmolLM2-360M-Instruct | Hugging Face | Transformer | about 362M | Apache-2.0 | Season 0 | Active, floor control |
| Graham | ibm-granite/granite-4.0-350m | IBM | Attention only (Grace's sibling without Mamba layers) | 352M | Apache-2.0 | Season 0, second casting | Active; his adapters failed the parity gate, so he was not in the adapter experiments |
| Rowan | BlinkDL/rwkv7-g1 (G1d 0.4B) | RWKV | Recurrent (RWKV-7), no attention | about 0.4B | Apache-2.0 | Season 0, second casting | Active |
| Erin | baidu/ERNIE-4.5-0.3B-PT | Baidu | Transformer | 361M | Apache-2.0 | Season 0, second casting | Active |
| Bastien | PleIAs/baguettotron-600m | PleIAs | Transformer trained on synthetic data | 608M | Apache-2.0 | Season 0, second casting | Active |
| Mina | openbmb/MiniCPM4-0.5B | OpenBMB | Transformer | 434M | Apache-2.0 | Season 0, second casting | Active |

Architecture, size and licence come from each model's Hugging Face card and repository metadata at the revision we pin; exact revisions and file hashes are recorded with each experiment.

Quinn and Quentin come from one lab. Grace and Graham are IBM siblings of almost the same size, one with Mamba layers and one without, which makes them a useful architecture comparison. The second casting (EXP-CZ-009) ran the same procedure as the first: template choice on the dev split, then a sealed test on a fresh, newly committed sealed set. Its design was frozen on 2026-10-25 before any member saw that set.

## Season 0 standings (first casting)

| Name | Sealed solve rate | Answer format valid | Note |
|---|---|---|---|
| Quinn | 44.8% | 86.4% | Only member clearly above guessing on graph questions; nearly all the arithmetic solves |
| Quentin | 28.6% | 58.6% | Strong at pulling facts from JSON |
| Grace | 25.1% | 99.8% | Near-perfect format; best on list puzzles |
| Sam | 16.3% | 77.5% | The floor, as expected |

Details: experiments/EXP-CZ-001/RESULTS.md.

## Season 0 standings (second casting, all nine members)

Sealed set 2, 1,200 new tasks, greedy, each member alone and untrained. The first four land inside their first-casting intervals.

| Name | Sealed solve rate | Answer format valid | Note |
|---|---|---|---|
| Quinn | 42.7% | 87.1% | Still the only member clearly above guessing on graph questions |
| Graham | 34.5% | 55.1% | Arithmetic specialist: 257 of 300 arithmetic tasks; fails R1 on format |
| Quentin | 29.5% | 59.3% | Strong at pulling facts from JSON |
| Grace | 23.4% | 99.8% | Best format in the colony; beats Graham on JSON and lists |
| Erin | 19.8% | 68.7% | |
| Mina | 18.2% | 59.8% | |
| Sam | 15.8% | 75.8% | The floor control |
| Rowan | 12.8% | 91.3% | Good format, but at the guessing baseline |
| Bastien | 6.5% | 13.0% | His thinking mode cannot be switched off; most answers hit the 512-token cap |

No member passes R1 untrained. Graham and Grace, siblings from one lab, differ significantly (414 against 281 solved). Details: experiments/EXP-CZ-009/RESULTS.md.

## Targeted adapters (EXP-CZ-010 and EXP-CZ-011)

Each member got two small adapters by one fixed recipe, trained on public practice problems: one on its own checked answers (self-taught), one on checked answers from an outside open-weight teacher, DeepSeek V4.1 Flash 1017 (teacher-taught). Each adapted member then answered the same 1,200 tasks of sealed set 2.

| Name | Untrained | Self-taught | Teacher-taught | R1 passed |
|---|---|---|---|---|
| Quinn | 42.7% | 82.8% | 88.3% | self-taught and teacher-taught |
| Quentin | 29.5% | 64.3% | 63.8% | self-taught and teacher-taught |
| Grace | 23.4% | 48.9% | 58.5% | self-taught and teacher-taught |
| Rowan | 12.8% | 47.1% | 51.8% | self-taught and teacher-taught |
| Mina | 18.2% | 30.8% | 59.4% | teacher-taught |
| Erin | 19.8% | 31.3% | 43.2% | neither (format) |
| Sam | 15.8% | 20.3% | 35.8% | teacher-taught |
| Bastien | 6.5% | 12.3% | 35.3% | teacher-taught |
| Graham | 34.5% | not run | not run | his adapters failed the parity gate (NaN outputs in the inference engine) |

Every tested member gained under both recipes. The teacher-taught adapter beat the self-taught one for 7 of 8 members, but it also had 1.4 to 4.1 times as many training examples, so a better teacher and more data cannot be told apart here. Two format caveats: the self-taught adapters of Erin and Grace raised their malformed answers by more than the preregistered limit (Erin by 169, Grace by 26, against a limit of 24 of 1,200), so both are recorded as harmful on format even though they raise solves; Erin's answers run to the token cap under both recipes, and she fails R1 on format in both. These are in-distribution gains on the same four synthetic task families, from one training seed per adapter (below our five-seed rule), so they are preliminary. The adapted versions are recorded results, not separate members. Details: experiments/EXP-CZ-010/RESULTS.md and experiments/EXP-CZ-011/RESULTS.md.

## Generation 1, children

A child is a smaller model trained by the colony and admitted only if it passes R1 on a sealed set. Each records its parent and its teacher.

| Name | Model | Parent | Teacher | Parameters | Joined | Sealed solve rate (set 3) | Status |
|---|---|---|---|---|---|---|---|
| Theo | SmolLM2-135M-Instruct with a merged adapter, Q8_0 | SmolLM2-135M-Instruct (Hugging Face, Apache-2.0) | DeepSeek V4.1 Flash 1017 (open weights, MIT) | 135M | EXP-CZ-017, 2026-10-26 | 37.0%, format 99.96% | Active; admitted under R1 (seed 0) |
| Hazel | SmolLM2-135M-Instruct with a merged adapter, Q8_0 | SmolLM2-135M-Instruct (Hugging Face, Apache-2.0) | MiMo V2.6 Flash (Xiaomi, open weights, MIT) | 135M | EXP-CZ-017, 2026-10-26 | 37.4%, format 100% | Active; admitted under R1 (seed 0) |

Both children beat their parent, which solves 12.6% and is not a member (H17.1, H17.2), so the rule that an offspring enters only if it beats its parent on a sealed test holds here. The EXP-CZ-017 admission gate itself was R1 only; future offspring specifications will require both R1 and a preregistered win over the parent. A third model, trained on the generator's own correct answers for the same tasks, is a control and not a member; it solves 36.9%, level with both children. Neither teacher beat those plain correct labels. On sealed set 3 the two children rank second in the colony's untrained standings, behind only Quinn, at about a sixth of his size; the trained founders were not run on set 3. Neither child learned arithmetic. These results are within four synthetic task families, and seed 0 of three decides them. File hashes for both children are in the experiment's manifest; weights are not published. Details: experiments/EXP-CZ-017/RESULTS.md.
