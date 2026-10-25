# The colony

Every member has a name, so the colony can be followed season after season. A name belongs to one model at one revision. An offspring gets its own name and records its parent. A member that is eliminated keeps its name and its row.

## Generation 0, founding members

| Name | Model | Lab | Architecture | Size | Licence | Joined | Status |
|---|---|---|---|---|---|---|---|
| Quinn | Qwen3.5-0.8B | Alibaba Qwen | Hybrid: Gated DeltaNet and attention | 800M | Apache-2.0 | Season 0 | Active |
| Quentin | Qwen3-0.6B | Alibaba Qwen | Transformer | 600M | Apache-2.0 | Season 0 | Active |
| Grace | Granite-4.0-H-350M | IBM | Hybrid: Mamba-2 and attention | 340M | Apache-2.0 | Season 0 | Active |
| Sam | SmolLM2-360M-Instruct | Hugging Face | Transformer | 362M | Apache-2.0 | Season 0 | Active, floor control |
| Graham | Granite-4.0-350M | IBM | Transformer (Grace's twin without Mamba) | 350M | Apache-2.0 | Season 0, second casting | Casting |
| Rowan | RWKV-7 G1 0.4B | RWKV | Recurrent, no attention | 400M | Apache-2.0 | Season 0, second casting | Casting |
| Erin | ERNIE-4.5-0.3B | Baidu | Transformer | 361M | Apache-2.0 | Season 0, second casting | Casting |
| Bastien | Baguettotron | PleIAs | Transformer trained on synthetic data | 608M | Apache-2.0 | Season 0, second casting | Casting |
| Mina | MiniCPM4-0.5B | OpenBMB | Transformer | 434M | Apache-2.0 | Season 0, second casting | Casting |

Quinn and Quentin are siblings from one lab; Grace and Graham are twins that differ only in architecture, which makes them a controlled comparison. The second casting runs the same procedure as the first: template choice on the dev split, then a sealed test on a fresh, newly committed sealed set.

## Season 0 standings (first casting)

| Name | Sealed solve rate | Answer format valid | Note |
|---|---|---|---|
| Quinn | 44.8% | 86.4% | Only member that reasons on graph questions; alone does arithmetic |
| Quentin | 28.6% | 58.6% | Strong at pulling facts from JSON |
| Grace | 25.1% | 99.8% | Near-perfect format; best on list puzzles |
| Sam | 16.3% | 77.5% | The floor, as expected |

Details: experiments/EXP-CZ-001/RESULTS.md.
