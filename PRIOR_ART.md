# Prior art

Most Colony Zero mechanisms have close predecessors. This page lists the ones we know, tied to the mechanism each precedes. Every paper below was checked against its arXiv record. Where we list no paper for a mechanism, we have not verified one, and that is not a claim that none exists.

What we think is specific to this project is the combination and the discipline: a population of small open models, elimination by measured contribution with a no-elimination twin, offspring promoted only by a sealed fail-closed test, and a hash-chained record of all of it. We have not shown the combination works.

## Ensembles, voting and repeated sampling (Colony vs best member, EXP-CZ-002)

- 2402.05120, More Agents Is All You Need (2024-02-03). Sampling many answers and voting. Precedes our majority-vote baseline.
- 2407.21787, Large Language Monkeys: Scaling Inference Compute with Repeated Sampling (2024-07-31). Coverage grows with samples. Precedes our coverage@8 endpoint.
- 2408.03314, Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (2024-08-06). Precedes our equal-compute framing.
- 2502.06703, Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling (2025-02-10). Small models with extra test-time compute.
- 2406.04692, Mixture-of-Agents Enhances Large Language Model Capabilities (2024-06-07). Layered teams of models.
- 2502.00674, Rethinking Mixture-of-Agents: Is Mixing Different Large Language Models Beneficial? (2025-02-02). Asks whether mixing different models helps, which is our diversity question.
- 2601.11327, Can Small Agents Collaborate to Beat a Single Large Language Model? (2026-01-16). Closest to our small-team question.
- 2604.02460, Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets (2026-04-02). A warning that equal budgets can erase team gains. It is why we compare at equal compute.
- 2605.01566, Multi-Agent Reasoning Improves Compute Efficiency: Pareto-Optimal Test-Time Scaling (2026-05-02). The opposite finding under other conditions.
- 2512.08296, Towards a Science of Scaling Agent Systems (2025-12-09). Conditions under which agent teams help.
- 2503.13657, Why Do Multi-Agent LLM Systems Fail? (2025-03-17). Failure modes we expect to meet.
- 2310.01798, Large Language Models Cannot Self-Correct Reasoning Yet (2023-10-03). A caution for any judge or debate arm.

## Routing (which member answers, Season 2, EXP-CZ-003)

- 2403.12031, RouterBench: A Benchmark for Multi-LLM Routing System (2024-03-18).
- 2406.18665, RouteLLM: Learning to Route LLMs with Preference Data (2024-06-26).
- 2505.12601, Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers (2025-05-19). Why our routing test includes simple baselines first.
- 2506.16655, Arch-Router: Aligning LLM Routing with Human Preferences (2025-06-19).
- 2606.07587, The Routing Plateau: Understanding the Accuracy Limits of LLM Routers (2026-05-27).
- 2608.06867, LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers (2026-08-07).
- 2606.02488, RASER: Recoverability-Aware Selective Escalation Router for Multi-Hop Question Answering (2026-06-01).

## Model merging (merged offspring, Season 3)

- 2403.13257, Arcee's MergeKit: A Toolkit for Merging Large Language Models (2024-03-20).
- 2403.19522, Model Stock: All we need is just a few fine-tuned models (2024-03-28).

We list no verified paper on evolutionary search over merges. Evolutionary model merging has prior work that is not on this page.

## Self-improvement and evolution of agents and programs (generations, Seasons 3 to 4)

- 2504.15228, A Self-Improving Coding Agent (2025-04-21).
- 2505.22954, Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (2025-05-29).
- 2510.21614, Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine (2025-10-24).
- 2602.04837, Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing (2026-02-04). A population that shares experience.
- 2506.13131, AlphaEvolve: A coding agent for scientific and algorithmic discovery (2025-06-16).
- 2509.19349, ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution (2025-09-17).
- 2604.07725, Squeeze Evolve: Unified Multi-Model Orchestration for Verifier-Free Evolution (2026-04-09). Evolution across several models.
- 2505.03335, Absolute Zero: Reinforced Self-play Reasoning with Zero Data (2025-05-06).
- 2508.05004, R-Zero: Self-Evolving Reasoning LLM from Zero Data (2025-08-07).
- 2506.10943, Self-Adapting Language Models (2025-06-12).
- 2405.15568, OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code (2024-05-24).
- 2603.16910, TerraLingua: Emergence and Analysis of Open-endedness in LLM Ecologies (2026-03-06). LLM populations as ecologies.
- 2411.00114, Project Sid: Many-agent simulations toward AI civilization (2024-10-31).

## Skills that transfer (Season 3, EXP-CZ-004)

- 2305.16291, Voyager: An Open-Ended Embodied Agent with Large Language Models (2023-05-25). A growing skill library.
- 2407.15325, Odyssey: Empowering Minecraft Agents with Open-World Skills (2024-07-22).
- 2603.02766, EvoSkill: Automated Skill Discovery for Multi-Agent Systems (2026-03-03).
- 2604.08377, SkillClaw: Let Skills Evolve Collectively with Agentic Evolver (2026-04-09).
- 2605.09341, SkillMAS: Skill Co-Evolution with LLM-based Multi-Agent System (2026-05-10).

## Distillation and adapters (offspring, EXP-CZ-005 and EXP-CZ-008)

- 2402.01620, MAGDi: Structured Distillation of Multi-Agent Interaction Graphs Improves Reasoning in Smaller Language Models (2024-02-02).
- 2511.05528, SMAGDi: Socratic Multi Agent Interaction Graph Distillation for Efficient High Accuracy Reasoning (2025-10-29).
- 2602.03955, AgentArk: Distilling Multi-Agent Intelligence into a Single LLM Agent (2026-02-03). Precedes the swarm-to-student experiment.
- 2502.12143, Small Models Struggle to Learn from Strong Reasoners (2025-02-17).
- 2405.09673, LoRA Learns Less and Forgets Less (2024-05-15).
- 2311.03285, S-LoRA: Serving Thousands of Concurrent LoRA Adapters (2023-11-06). Many adapters sharing one base model.
- 2308.08747, An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning (2023-08-17). Why promotion has a protected regression suite.

## Small models and evaluation hygiene (EXP-CZ-001)

- 2502.02737, SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model (2025-02-04). One of our founding members.
- 2404.05405, Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws (2024-04-08).
- 2501.04519, rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking (2025-01-08).
- 2510.04871, Less is More: Recursive Reasoning with Tiny Networks (2025-10-06).
- 2606.22189, L20-Edu-135M: An Auditable Single-GPU Study of Data-Efficient Small Language Modeling (2026-06-20). An auditable single-GPU study, close in spirit to ours.
- 2506.12286, The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason (2025-06-14). Why sealed, regenerable tasks matter.
- 2605.26128, The Constraint Tax: Measuring Validity-Correctness Tradeoffs in Structured Outputs for Small Language Models (2026-05-20). Why we report format validity separately from correctness.
- 2211.10435, PAL: Program-aided Language Models (2022-11-18). Why a code reference program shows our tasks are solvable.

## Mechanisms with no verified entry here

Self-consistency voting as a named method, debate between models, elimination by leave-one-out or Shapley contribution, evolutionary search over model merges, and public randomness beacons all have established predecessors. We have not verified citations for them yet, so they are not listed. Until they are, we describe nothing here as a new mechanism. Any contribution of this project is at most a preregistered combination of known parts, tested under sealed evaluation.
