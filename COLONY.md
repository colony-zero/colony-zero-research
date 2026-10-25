# The colony

Every member has a name, so the colony can be followed season after season. A name belongs to one model at one revision. An offspring gets its own name and records its parent. A member that is eliminated keeps its name and its row.

## Generation 0, founding members

| Name | Model (Hugging Face repo) | Lab | Architecture | Parameters | Licence | Joined | Status |
|---|---|---|---|---|---|---|---|
| Quinn | Qwen/Qwen3.5-0.8B | Alibaba Qwen | Hybrid: Gated DeltaNet and attention | about 0.8B | Apache-2.0 | Season 0 | Active |
| Quentin | Qwen/Qwen3-0.6B | Alibaba Qwen | Transformer | about 0.6B | Apache-2.0 | Season 0 | Active |
| Grace | ibm-granite/granite-4.0-h-350m | IBM | Hybrid: Mamba-2 and attention | about 340M | Apache-2.0 | Season 0 | Active |
| Sam | HuggingFaceTB/SmolLM2-360M-Instruct | Hugging Face | Transformer | about 362M | Apache-2.0 | Season 0 | Active, floor control |
| Graham | ibm-granite/granite-4.0-350m | IBM | Attention only (Grace's sibling without Mamba layers) | 352M | Apache-2.0 | Season 0, second casting | Not yet tested |
| Rowan | BlinkDL/rwkv7-g1 (G1d 0.4B) | RWKV | Recurrent (RWKV-7), no attention | about 0.4B | Apache-2.0 | Season 0, second casting | Not yet tested |
| Erin | baidu/ERNIE-4.5-0.3B-PT | Baidu | Transformer | 361M | Apache-2.0 | Season 0, second casting | Not yet tested |
| Bastien | PleIAs/baguettotron-600m | PleIAs | Transformer trained on synthetic data | 608M | Apache-2.0 | Season 0, second casting | Not yet tested |
| Mina | openbmb/MiniCPM4-0.5B | OpenBMB | Transformer | 434M | Apache-2.0 | Season 0, second casting | Not yet tested |

Architecture, size and licence come from each model's Hugging Face card and repository metadata at the revision we pin; exact revisions and file hashes are recorded with each experiment.

Quinn and Quentin come from one lab. Grace and Graham are IBM siblings of almost the same size, one with Mamba layers and one without, which makes them a useful architecture comparison. The second casting (EXP-CZ-009) runs the same procedure as the first: template choice on the dev split, then a sealed test on a fresh, newly committed sealed set. Its design was frozen on 2026-10-25 before any member saw that set.

## Season 0 standings (first casting)

| Name | Sealed solve rate | Answer format valid | Note |
|---|---|---|---|
| Quinn | 44.8% | 86.4% | Only member clearly above guessing on graph questions; nearly all the arithmetic solves |
| Quentin | 28.6% | 58.6% | Strong at pulling facts from JSON |
| Grace | 25.1% | 99.8% | Near-perfect format; best on list puzzles |
| Sam | 16.3% | 77.5% | The floor, as expected |

Details: experiments/EXP-CZ-001/RESULTS.md.
