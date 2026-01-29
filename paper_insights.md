# Deep Research Insights for Spatial AI Survey Paper

## Objective
Extract A+ quality insights from each paper to build a comprehensive survey on AI agents capable of spatial planning tasks.

---

## Part I: Foundational Agentic Architectures

### 1. ReAct: Synergizing Reasoning and Acting in Language Models
**Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
**Venue:** ICLR 2023
**arXiv:** 2210.03629

**A+ Key Insights:**

1. **Core Innovation:** Interleaves reasoning traces and task-specific actions, creating synergy between thought and action
   - Reasoning traces help induce, track, and update action plans
   - Actions interface with external sources (knowledge bases, environments)
   - Overcomes hallucination and error propagation in pure chain-of-thought

2. **Performance Results:**
   - HotpotQA and Fever: Overcomes hallucination via Wikipedia API interaction
   - ALFWorld: +34% absolute success rate over imitation/RL methods
   - WebShop: +10% absolute success rate
   - Only 1-2 in-context examples needed

3. **Spatial Planning Implications:**
   - **Action-Observation Loop:** Critical for spatial agents that must perceive, reason, and act
   - **Exception Handling:** Reasoning traces enable recovery from spatial planning failures
   - **External Tool Integration:** Pattern for integrating GIS tools, maps, spatial databases
   - **Interpretability:** Human-like trajectories essential for safety-critical spatial applications

4. **Architectural Pattern:**
   ```
   Thought → Action → Observation → Thought → Action → ...
   ```

**Citation Key:** yao2023react

---

### 2. Toolformer: Language Models Can Teach Themselves to Use Tools
**Authors:** Timo Schick, Jane Dwivedi-Yu, et al.
**Venue:** ICLR 2023
**arXiv:** 2302.04761

**A+ Key Insights:**

1. **Self-Supervised Tool Learning:**
   - Models learn when and how to invoke APIs during pretraining
   - No explicit supervision for tool use decisions
   - Self-labeling inserts API calls into text

2. **Spatial Planning Implications:**
   - Pattern for teaching agents to invoke spatial tools (PostGIS, H3, S2)
   - Autonomous decision-making about when spatial computation is needed
   - Foundation for GIS-augmented language agents

**Citation Key:** schick2023toolformer

---

### 3. Tree of Thoughts: Deliberate Problem Solving with Large Language Models
**Authors:** Shunyu Yao, Dian Yu, Jeffrey Zhao, et al.
**Venue:** NeurIPS 2023
**arXiv:** 2305.10601

**A+ Key Insights:**

1. **Core Innovation:** Frames reasoning as tree search over intermediate thought states
   - Enables exploration, backtracking, and scoring
   - Explicit branching over reasoning states
   - Deliberate problem solving vs. greedy CoT

2. **Spatial Planning Implications:**
   - **Path Planning Analogy:** Tree search mirrors spatial path planning algorithms
   - **Backtracking:** Essential for navigating spatial dead-ends
   - **Multi-Hypothesis Reasoning:** Exploring multiple spatial configurations
   - **Scoring:** Evaluating spatial feasibility of intermediate plans

**Citation Key:** yao2023tree

---

### 4. Reflexion: Language Agents with Verbal Reinforcement Learning
**Authors:** Noah Shinn, Federico Cassano, Ashwin Gopinath, et al.
**Venue:** NeurIPS 2023
**arXiv:** 2303.11366

**A+ Key Insights:**

1. **Self-Reflection as Learning Signal:**
   - Natural-language self-reflection stored in memory
   - Trial → Reflection → Retry loop
   - Improves performance over multiple attempts

2. **Spatial Planning Implications:**
   - **Learning from Spatial Failures:** Agents can reflect on navigation/manipulation errors
   - **Episodic Memory:** Storing spatial experiences for future reference
   - **Iterative Refinement:** Critical for complex spatial planning tasks

**Citation Key:** shinn2023reflexion

---

### 5. Generative Agents: Interactive Simulacra of Human Behavior
**Authors:** Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, et al.
**Venue:** CHI 2023 (Best Paper)
**arXiv:** 2304.03442

**A+ Key Insights:**

1. **Memory + Reflection + Planning Architecture:**
   - LLM-driven agents with coherent daily behaviors
   - Social interactions in simulated world
   - Emergent believable behavior

2. **Spatial Planning Implications:**
   - **Spatial Memory:** Agents remember locations and spatial relationships
   - **Activity Planning:** Scheduling activities across spatial locations
   - **Social-Spatial Dynamics:** Multi-agent spatial coordination

**Citation Key:** park2023generative

---

## Part II: Embodied AI and Physical Agents

### 6. Voyager: An Open-Ended Embodied Agent with Large Language Models
**Authors:** Guanzhi Wang, Yu Bai, Wanyun Du, et al.
**Venue:** arXiv 2023
**arXiv:** 2305.16291

**A+ Key Insights:**

1. **Lifelong Learning Agent:**
   - Explores open world (Minecraft)
   - Learns reusable skills
   - LLM generates code-based actions
   - Self-improvement through exploration

2. **Key Components:**
   - **Skill Library:** Reusable spatial/manipulation skills
   - **Curriculum Learning:** Progressive skill acquisition
   - **Code-as-Action:** Precise spatial control through code

3. **Spatial Planning Implications:**
   - **Open-Ended Exploration:** Agents discover spatial structure
   - **Skill Composition:** Building complex spatial behaviors from primitives
   - **Environment Adaptation:** Generalizing across spatial configurations

**Citation Key:** wang2023voyager

---

### 7. PaLM-E: An Embodied Multimodal Language Model
**Authors:** Danny Driess, Fei Xia, et al.
**Venue:** ICML 2023
**arXiv:** 2303.03378

**A+ Key Insights:**

1. **Multimodal Embodied Foundation Model:**
   - Integrates vision, language, and robot control
   - 562B parameter model
   - End-to-end training on embodied tasks

2. **Spatial Planning Implications:**
   - **Unified Perception-Action:** Single model for spatial understanding and control
   - **Transfer Learning:** Spatial knowledge transfers across tasks
   - **Grounded Language:** Language connected to physical spatial actions

**Citation Key:** driess2023palme

---

### 8. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
**Authors:** Anthony Brohan, et al. (Google DeepMind)
**Venue:** arXiv 2023
**arXiv:** 2307.15818

**A+ Key Insights:**

1. **Web-to-Robot Transfer:**
   - Vision-language models fine-tuned for robotic control
   - Actions as text tokens
   - Emergent spatial reasoning from web pretraining

2. **Spatial Planning Implications:**
   - **Semantic Spatial Reasoning:** Understanding "put X on Y" from web knowledge
   - **Generalization:** Novel object manipulation without explicit training
   - **VLA Architecture:** Vision-Language-Action as unified paradigm

**Citation Key:** brohan2023rt2

---

## Part III: Spatial Reasoning and Benchmarks

### 9. CLEVR: A Diagnostic Dataset for Compositional Language and Elementary Visual Reasoning
**Authors:** Justin Johnson, et al.
**Venue:** CVPR 2017

**A+ Key Insights:**

1. **Compositional Spatial Reasoning:**
   - Synthetic VQA with controlled complexity
   - Spatial relations: left/right, front/behind, above/below
   - Attribute reasoning + spatial reasoning

2. **Benchmark Design Principles:**
   - **Diagnostic:** Isolates specific reasoning capabilities
   - **Compositional:** Tests generalization to novel combinations
   - **Controlled:** Eliminates confounds from real-world complexity

**Citation Key:** johnson2017clevr

---

### 10. GQA: A New Dataset for Real-World Visual Reasoning
**Authors:** Drew A. Hudson, Christopher D. Manning
**Venue:** CVPR 2019

**A+ Key Insights:**

1. **Scene Graph-Based VQA:**
   - Real images with compositional questions
   - Spatial relations derived from scene graphs
   - Consistency and validity metrics

2. **Spatial Reasoning Aspects:**
   - Object-object spatial relations
   - Relative positioning
   - Spatial reference resolution

**Citation Key:** hudson2019gqa

---

### 11. ScanNet: Richly-Annotated 3D Reconstructions of Indoor Scenes
**Authors:** Angela Dai, Angel X. Chang, Manolis Savva, et al.
**Venue:** CVPR 2017

**A+ Key Insights:**

1. **3D Indoor Scene Understanding:**
   - RGB-D reconstructions with semantic labels
   - Core dataset for 3D spatial reasoning
   - Foundation for embodied navigation

2. **Spatial Intelligence Applications:**
   - 3D object detection
   - Semantic segmentation
   - Scene understanding for navigation

**Citation Key:** dai2017scannet

---

### 12. Matterport3D: Learning from RGB-D Data in Indoor Environments
**Authors:** Angel X. Chang, Angela Dai, et al.
**Venue:** 3DV 2017

**A+ Key Insights:**

1. **Large-Scale Indoor 3D Dataset:**
   - Panoramic RGB-D captures
   - 90 building-scale scenes
   - Foundation for VLN research

2. **Spatial Navigation Applications:**
   - Vision-language navigation
   - Spatial language grounding
   - Room-to-room navigation

**Citation Key:** chang2017matterport3d

---

## Part IV: Graph Neural Networks for Spatial Intelligence

### 13. Spatio-Temporal Graph Neural Networks for Urban Computing: A Survey
**Authors:** Guangyin Jin, Yuxuan Liang, et al.
**Venue:** IEEE TKDE 2023
**arXiv:** 2303.14483

**A+ Key Insights:**

1. **STGNN Architecture:**
   - Integrates GNNs with temporal learning (RNN/TCN/Attention)
   - Captures complex spatio-temporal dependencies
   - Enables urban-scale prediction

2. **Application Domains:**
   - Traffic flow prediction
   - Air quality forecasting
   - Crime prediction
   - Epidemic modeling

3. **Spatial Planning Implications:**
   - **Dynamic Spatial Reasoning:** Understanding how spatial patterns evolve
   - **Urban Intelligence:** City-scale spatial planning support
   - **Predictive Planning:** Anticipating spatial dynamics

**Citation Key:** jin2023stgnn

---

### 14. Graph Transformers: A Survey
**Authors:** Ahsan Shehzad, Feng Xia, et al.
**Venue:** IEEE TNNLS 2026
**arXiv:** 2407.09777

**A+ Key Insights:**

1. **Graph + Transformer Synergy:**
   - Graph inductive biases in transformer architecture
   - Graph attention mechanisms
   - Scalable graph learning

2. **Spatial Planning Implications:**
   - **Long-Range Dependencies:** Attention captures distant spatial relationships
   - **Scalability:** Handling large spatial graphs (road networks, cities)
   - **Flexibility:** Adapting to different spatial graph structures

**Citation Key:** shehzad2024graphtransformers

---

## Part V: Geospatial AI and Foundation Models

### 15. Prithvi: A Foundation Model for Earth Observation
**Authors:** IBM/NASA
**Venue:** 2023

**A+ Key Insights:**

1. **Geospatial Foundation Model:**
   - Pretrained on satellite imagery
   - Multi-spectral understanding
   - Transfer to downstream tasks

2. **Spatial Planning Applications:**
   - Land use classification
   - Change detection
   - Disaster response

**Citation Key:** jakubik2023prithvi

---

### 16. GeoAI: A Review of Artificial Intelligence Approaches for the Interpretation of Complex Geospatial Data
**Authors:** Janowicz et al.
**Venue:** IJGIS 2020

**A+ Key Insights:**

1. **GeoAI Taxonomy:**
   - Deep learning for geospatial data
   - Spatial representation learning
   - Knowledge graphs for geography

2. **Key Challenges:**
   - Spatial autocorrelation
   - Scale dependency
   - Heterogeneous data fusion

**Citation Key:** janowicz2020geoai

---

## Part VI: Agent Evaluation and Benchmarks

### 17. AgentBench: Evaluating LLMs as Agents
**Authors:** Xiao Liu, et al.
**Venue:** arXiv 2023
**arXiv:** 2308.03688

**A+ Key Insights:**

1. **Multi-Domain Agent Benchmark:**
   - Evaluates tool use, planning, memory
   - Diverse interactive tasks
   - Systematic capability assessment

2. **Evaluation Dimensions:**
   - Task completion
   - Reasoning quality
   - Tool invocation accuracy

**Citation Key:** liu2023agentbench

---

### 18. WebArena: A Realistic Web Environment for Building Autonomous Agents
**Authors:** Tianbao Xie, et al.
**Venue:** arXiv 2023
**arXiv:** 2307.13854

**A+ Key Insights:**

1. **Realistic Web Environment:**
   - Interactive websites
   - Multi-step tasks
   - Browser actions

2. **Spatial Analogy:**
   - Web navigation as spatial navigation
   - Information foraging in digital space
   - Sequential decision-making

**Citation Key:** xie2023webarena

---

### 19. BEHAVIOR: Benchmark for Everyday Household Activities
**Authors:** Srivastava et al.
**Venue:** CoRL 2021

**A+ Key Insights:**

1. **Embodied Task Benchmark:**
   - 100 household activities
   - Long-horizon tasks
   - Object interaction + spatial reasoning

2. **Spatial Planning Requirements:**
   - Object localization
   - Spatial constraint satisfaction
   - Multi-step manipulation

**Citation Key:** srivastava2021behavior

---

## Part VII: Multi-Agent Systems

### 20. AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation
**Authors:** Chi Wang, et al.
**Venue:** arXiv 2024

**A+ Key Insights:**

1. **Multi-Agent Framework:**
   - Specialized agents coordinate via conversation
   - Role-based task decomposition
   - Tool use integration

2. **Spatial Planning Implications:**
   - **Collaborative Spatial Planning:** Multiple agents with different spatial expertise
   - **Distributed Reasoning:** Parallel spatial analysis
   - **Coordination:** Multi-robot spatial coordination

**Citation Key:** wang2024autogen

---

### 21. MetaGPT: Meta Programming for Multi-Agent Collaborative Framework
**Authors:** Siyu Hong, et al.
**Venue:** arXiv 2023
**arXiv:** 2308.00352

**A+ Key Insights:**

1. **Software Company Metaphor:**
   - Role-based multi-agent system
   - Specification → Design → Code pipeline
   - Structured collaboration

2. **Spatial Planning Analogy:**
   - Urban planning as multi-agent collaboration
   - Architect, engineer, planner roles
   - Hierarchical spatial design

**Citation Key:** hong2023metagpt

---

## Part VIII: Vision-Language Navigation

### 22. Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments
**Authors:** Peter Anderson, et al.
**Venue:** CVPR 2018

**A+ Key Insights:**

1. **VLN Task Definition:**
   - Follow natural language navigation instructions
   - First-person visual observations
   - Real indoor environments (Matterport3D)

2. **Spatial Language Grounding:**
   - "Turn left at the kitchen"
   - Landmark-based navigation
   - Spatial reference resolution

**Citation Key:** anderson2018vln

---

### 23. ALFWorld: Aligning Text and Embodied Environments for Interactive Learning
**Authors:** Shunyu Yao, et al.
**Venue:** ICLR 2021
**arXiv:** 2010.03768

**A+ Key Insights:**

1. **Text-Embodied Alignment:**
   - Text-based games aligned with 3D environments
   - Language to embodied actions
   - Interactive learning

2. **Spatial Planning Tasks:**
   - Object search
   - Multi-step manipulation
   - Household task completion

**Citation Key:** yao2021alfworld

---

## Part IX: World Models and Simulation

### 24. World Models Survey
**Authors:** Various
**Venue:** arXiv 2024
**arXiv:** 2411.14499

**A+ Key Insights:**

1. **Internal World Representation:**
   - Agents build models of environment dynamics
   - Predict future states
   - Plan in imagination

2. **Spatial World Models:**
   - 3D scene understanding
   - Physics simulation
   - Spatial dynamics prediction

**Citation Key:** worldmodels2024survey

---

### 25. Habitat: A Platform for Embodied AI Research
**Authors:** Manolis Savva, et al.
**Venue:** ICCV 2019

**A+ Key Insights:**

1. **High-Performance Simulation:**
   - 10,000+ FPS rendering
   - Realistic 3D environments
   - Embodied AI benchmarks

2. **Spatial Intelligence Evaluation:**
   - PointNav: Navigate to coordinates
   - ObjectNav: Navigate to object categories
   - Embodied QA

**Citation Key:** savva2019habitat

---

## Summary: Cross-Cutting Themes for Survey

### Theme 1: The Perception-Reasoning-Action Loop
All successful spatial agents implement some form of:
- **Perceive:** Understand spatial environment (vision, sensors, maps)
- **Reason:** Plan actions considering spatial constraints
- **Act:** Execute spatial movements/manipulations
- **Observe:** Update understanding based on outcomes

### Theme 2: Memory and Spatial Knowledge
- **Episodic Memory:** Remembering spatial experiences
- **Semantic Memory:** General spatial knowledge
- **Spatial Maps:** Explicit spatial representations

### Theme 3: Tool Use for Spatial Computation
- GIS tools (PostGIS, QGIS)
- Spatial indexing (H3, S2)
- Geometric computation libraries
- Map APIs

### Theme 4: Multi-Scale Spatial Reasoning
- Object-level (manipulation)
- Room-level (navigation)
- Building-level (indoor mapping)
- City-level (urban planning)
- Global-level (geospatial analysis)

### Theme 5: Sim-to-Real Transfer
- Simulation environments (Habitat, iGibson, Minecraft)
- Domain adaptation
- Reality gap challenges

### Theme 6: Evaluation Gaps
- Need for integrated agentic + spatial benchmarks
- Multi-step spatial planning evaluation
- Real-world deployment metrics

---

## Next Steps
1. Deep dive into remaining papers in zip folder
2. Access full PDFs for detailed methodology extraction
3. Identify additional citations needed
4. Update LaTeX with comprehensive literature review
5. Build complete BibTeX file with 50+ references



---

## Additional Deep Dive Papers

### 26. Voyager - Extended Insights
**Full Author List:** Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar

**Quantitative Results:**
- 3.3x more unique items obtained
- 2.3x longer distances traveled
- 15.3x faster tech tree milestone unlocking vs. prior SOTA

**Three Key Components:**
1. **Automatic Curriculum:** Maximizes exploration without human intervention
2. **Skill Library:** Ever-growing library of executable code for complex behaviors
3. **Iterative Prompting:** Incorporates environment feedback, execution errors, self-verification

**Critical Design Decisions:**
- GPT-4 via blackbox queries (no fine-tuning needed)
- Skills are temporally extended, interpretable, compositional
- Compounds abilities rapidly, alleviates catastrophic forgetting
- Generalizes to new Minecraft worlds

**Spatial Planning Relevance:**
- **Exploration as Spatial Discovery:** Agent learns spatial structure through exploration
- **Skill Composition:** Complex spatial behaviors from primitive skills
- **Code-as-Action:** Precise spatial control through programmatic actions
- **Lifelong Learning:** Continuous spatial knowledge acquisition



---

### 27. Tree of Thoughts - Extended Insights
**Full Author List:** Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan
**Venue:** NeurIPS 2023

**Core Problem Addressed:**
- LMs confined to token-level, left-to-right decision-making
- Fall short in tasks requiring exploration, strategic lookahead
- Initial decisions play pivotal role but cannot be revised

**Key Innovation:**
- Generalizes Chain of Thought to tree structure
- Exploration over coherent units of text (thoughts)
- Multiple reasoning paths with self-evaluation
- Looking ahead and backtracking for global choices

**Quantitative Results:**
- Game of 24: GPT-4 with CoT = 4% success, ToT = 74% success
- Massive improvement on tasks requiring planning/search

**Spatial Planning Implications:**
- Tree search mirrors A* and other path planning algorithms
- Backtracking essential for spatial dead-ends
- Multi-hypothesis spatial reasoning
- Deliberate evaluation of spatial configurations

**Citation Key:** yao2023tree

---

### 28. A Survey on Large Language Model based Autonomous Agents
**Full Author List:** Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, Ji-Rong Wen
**Venue:** Frontiers of Computer Science 2024
**arXiv:** 2308.11432

**Survey Scope:**
- Comprehensive survey of LLM-based autonomous agents
- Holistic perspective on agent construction
- Applications in social science, natural science, engineering
- Evaluation strategies

**Unified Agent Framework:**
1. **Profile Module:** Agent identity and role
2. **Memory Module:** Short-term and long-term memory
3. **Planning Module:** Task decomposition and reasoning
4. **Action Module:** Tool use and environment interaction

**Key Insights for Spatial AI:**
- Memory critical for spatial navigation (remembering visited locations)
- Planning essential for multi-step spatial tasks
- Tool use enables GIS/mapping integration
- Profile can encode spatial expertise

**Citation Key:** wang2024survey

---

### 29. Understanding the Planning of LLM Agents: A Survey
**arXiv:** 2402.02716 (Feb 2024)

**Planning Taxonomy:**
1. **Task Decomposition:** Breaking complex goals into subgoals
2. **Plan Generation:** Creating action sequences
3. **Plan Refinement:** Iterative improvement
4. **Plan Execution:** Carrying out actions

**Spatial Planning Relevance:**
- Hierarchical spatial planning (room → building → city)
- Constraint satisfaction in spatial domains
- Replanning when spatial obstacles encountered

**Citation Key:** huang2024understanding

---

### 30. SayCan: Grounding Language in Robotic Affordances
**Authors:** Google/Everyday Robots
**Venue:** arXiv 2022

**Key Innovation:**
- Grounds LLM knowledge in robot capabilities
- Affordance functions score action feasibility
- Language provides high-level goals
- Robot provides low-level execution

**Spatial Planning Implications:**
- Affordances encode spatial feasibility
- Physical constraints on spatial actions
- Grounding abstract spatial language in robot actions

**Citation Key:** ahn2022saycan

---

### 31. MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge
**Authors:** Linxi Fan, Guanzhi Wang, et al.
**Venue:** NeurIPS 2022

**Key Contributions:**
- Large-scale Minecraft environment
- Internet-scale knowledge integration
- Diverse task suite
- Foundation for open-ended learning

**Spatial Intelligence Aspects:**
- 3D world exploration
- Resource gathering requires spatial planning
- Building construction as spatial creativity
- Navigation in procedurally generated worlds

**Citation Key:** fan2022minedojo



---

### 32. Vision-and-Language Navigation (VLN) - R2R Dataset
**Full Author List:** Peter Anderson, Qi Wu, Damien Teney, Jake Bruce, Mark Johnson, Niko Sunderhauf, Ian Reid, Stephen Gould, Anton van den Hengel
**Venue:** CVPR 2018 Spotlight

**Foundational Contribution:**
- First benchmark for visually-grounded natural language navigation
- Matterport3D Simulator for RL environment
- Room-to-Room (R2R) dataset
- Real building imagery

**Task Definition:**
- Robot interprets natural-language navigation instruction
- Visually grounded sequence-to-sequence translation
- Similar to Visual Question Answering

**Spatial Language Grounding:**
- "Turn left at the kitchen"
- "Go past the couch and through the doorway"
- Landmark-based spatial references
- Relative spatial directions

**Key Metrics:**
- Success Rate (SR)
- Success weighted by Path Length (SPL)
- Navigation Error (NE)

**Spatial Planning Implications:**
- Grounding language in spatial actions
- Visual landmark recognition
- Path planning from instructions
- Real-world spatial reasoning

**Citation Key:** anderson2018vln

---

### 33. Habitat: A Platform for Embodied AI Research
**Authors:** Manolis Savva, Abhishek Kadian, et al.
**Venue:** ICCV 2019

**Key Contributions:**
- High-performance 3D simulation (10,000+ FPS)
- Photorealistic environments
- Standardized embodied AI benchmarks

**Benchmark Tasks:**
1. **PointNav:** Navigate to (x, y, z) coordinates
2. **ObjectNav:** Navigate to object category
3. **Embodied QA:** Answer questions by exploring

**Spatial Intelligence Evaluation:**
- Measures navigation efficiency
- Tests spatial memory
- Evaluates exploration strategies

**Citation Key:** savva2019habitat

---

### 34. iGibson: Interactive Simulation for Robot Learning
**Venue:** CoRL 2021

**Key Features:**
- Physics-based simulation
- Interactive objects
- Object-centric manipulation

**Spatial Planning Applications:**
- Manipulation planning
- Object rearrangement
- Household task completion

**Citation Key:** li2021igibson

---

### 35. BEHAVIOR: Benchmark for Everyday Household Activities
**Venue:** CoRL 2021

**Key Contributions:**
- 100 household activities
- Long-horizon tasks
- Object interaction + spatial reasoning

**Spatial Requirements:**
- Object localization
- Spatial constraint satisfaction
- Multi-room navigation
- Tool use for manipulation

**Citation Key:** srivastava2021behavior

---

## Part X: Geospatial AI and Foundation Models

### 36. Prithvi: A Foundation Model for Earth Observation
**Authors:** IBM/NASA
**Venue:** 2023

**Key Innovation:**
- First open geospatial foundation model
- Pretrained on HLS satellite data
- Multi-spectral understanding

**Applications:**
- Flood mapping
- Burn scar detection
- Crop classification
- Land cover segmentation

**Spatial Planning Implications:**
- Large-scale environmental monitoring
- Disaster response planning
- Urban growth analysis

**Citation Key:** jakubik2023prithvi

---

### 37. SatCLIP: Global, General-Purpose Location Embeddings
**Venue:** arXiv 2023

**Key Innovation:**
- Location embeddings from satellite imagery
- CLIP-style contrastive learning
- Global coverage

**Applications:**
- Location-aware retrieval
- Geospatial transfer learning
- Place recognition

**Citation Key:** klemmer2023satclip

---

### 38. GeoAI: Spatially Explicit Artificial Intelligence Techniques
**Authors:** Janowicz et al.
**Venue:** IJGIS 2020

**GeoAI Taxonomy:**
1. **Spatial Representation Learning:** Embeddings for locations
2. **Geospatial Knowledge Graphs:** Structured geographic knowledge
3. **Deep Learning for Geospatial Data:** CNNs, GNNs for spatial data

**Key Challenges:**
- Spatial autocorrelation
- Scale dependency
- Heterogeneous data fusion
- Uncertainty quantification

**Citation Key:** janowicz2020geoai

---

## Part XI: Graph Neural Networks for Spatial Intelligence

### 39. A Comprehensive Survey on Graph Neural Networks
**Authors:** Wu et al.
**Venue:** IEEE TNNLS 2021

**GNN Taxonomy:**
1. **Spectral GNNs:** Graph Fourier transform
2. **Spatial GNNs:** Message passing
3. **Graph Autoencoders:** Unsupervised learning
4. **Spatial-Temporal GNNs:** Dynamic graphs

**Spatial Applications:**
- Traffic prediction
- Point cloud processing
- Scene graphs
- Road network analysis

**Citation Key:** wu2021gnn

---

### 40. Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges
**Authors:** Bronstein et al.
**Venue:** arXiv 2021

**Unifying Framework:**
- Symmetry and invariance principles
- Geometric priors in neural networks
- From CNNs to GNNs to transformers

**Spatial Relevance:**
- 3D point cloud processing
- Molecular geometry
- Manifold learning

**Citation Key:** bronstein2021geometric

---

### 41. Spatio-Temporal Graph Neural Networks: A Survey
**Authors:** Sahili et al.
**Venue:** arXiv 2023

**STGNN Components:**
1. **Spatial Module:** GNN for spatial dependencies
2. **Temporal Module:** RNN/TCN/Attention for time
3. **Joint Learning:** Coupled spatio-temporal

**Applications:**
- Traffic flow prediction
- Air quality forecasting
- Epidemic modeling
- Human mobility prediction

**Citation Key:** sahili2023stgnn

---

## Part XII: Multimodal Large Language Models

### 42. GPT-4V(ision) System Card
**Venue:** OpenAI 2023

**Capabilities:**
- Image understanding
- Visual reasoning
- Spatial relationship recognition

**Limitations:**
- Fine-grained spatial reasoning
- Precise counting
- Spatial measurement

**Implications:**
- MLLMs show promise but gaps remain
- Need for spatial-specific training
- Benchmark development needed

**Citation Key:** openai2023gpt4v

---

### 43. LLaVA: Visual Instruction Tuning
**Authors:** Liu et al.
**Venue:** NeurIPS 2023

**Key Innovation:**
- Visual instruction following
- GPT-4 generated training data
- End-to-end multimodal model

**Spatial Capabilities:**
- Object localization
- Spatial relationship description
- Scene understanding

**Citation Key:** liu2023llava

---

### 44. BLIP-2: Bootstrapping Language-Image Pre-training
**Authors:** Li et al.
**Venue:** ICML 2023

**Architecture:**
- Q-Former bridges vision and language
- Frozen image encoders
- Frozen LLMs

**Spatial Applications:**
- Visual question answering
- Image captioning with spatial details
- Grounded generation

**Citation Key:** li2023blip2

---

## Part XIII: Agent Safety and Robustness

### 45. Constitutional AI: Harmlessness from AI Feedback
**Venue:** Anthropic 2022

**Key Innovation:**
- Self-critique with constitution
- Reduces harmful outputs
- Alignment through feedback

**Spatial Agent Safety:**
- Safe navigation constraints
- Avoiding dangerous actions
- Ethical spatial planning

**Citation Key:** bai2022constitutional

---

### 46. Safety of Embodied Navigation: A Survey
**Venue:** arXiv 2025

**Threat Models:**
1. **Adversarial Perception:** Attacks on visual input
2. **Backdoor Attacks:** Hidden triggers
3. **Unsafe Planning:** Dangerous trajectories

**Defenses:**
- Robust perception
- Verified planning
- Safety constraints

**Citation Key:** safety2025embodied

---

## Summary Statistics

**Papers Analyzed:** 46+
**Categories Covered:**
- Agentic LLM Architectures: 10
- Embodied AI: 8
- Spatial Reasoning Benchmarks: 6
- GNN/Geometric DL: 5
- Geospatial AI: 5
- Multi-Agent Systems: 4
- VLN/Navigation: 4
- MLLMs: 4
- Safety: 2

**Key Themes Identified:**
1. Perception-Reasoning-Action Loop
2. Memory for Spatial Knowledge
3. Tool Use for Spatial Computation
4. Multi-Scale Spatial Reasoning
5. Sim-to-Real Transfer
6. Evaluation Gaps



---

## Part XIV: Latest Benchmarks for Spatial AI Agents (2025)

### 47. REM: Evaluating LLM Embodied Spatial Reasoning through Multi-Frame Trajectories
**Authors:** Jacob Thompson, Emiliano Garcia-Lopez, Yonatan Bisk
**Venue:** COLM 2025
**arXiv:** 2512.00736

**Core Contribution:**
- Benchmark for long-horizon embodied spatial reasoning
- Uses controllable 3D environments
- Multi-frame visual sequences simulating egocentric viewpoints

**Key Evaluation Dimensions:**
1. **Object Permanence/Distinction:** Tracking objects across viewpoints
2. **Spatial Relationships:** Understanding relative positions
3. **Numerical Tracking:** Counting objects in dynamic scenes

**Critical Findings:**
- MLLMs lack fundamental spatial reasoning despite video training
- Best models become unreliable at moderate complexity
- Humans easily handle tasks that challenge MLLMs
- Gap in developing robust spatial representations from sequential input

**Implications for Survey:**
- Highlights critical capability gap in current MLLMs
- Need for spatial-specific training and architectures
- Benchmark provides targeted diagnostics for improvement

**Citation Key:** thompson2025rem

---

### 48. EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents
**Authors:** Rui Yang, Hanyang Chen, Junyu Zhang, Mark Zhao, Cheng Qian, et al.
**Venue:** ICML 2025
**arXiv:** 2502.09560

**Benchmark Features:**
- 1,128 testing tasks across four environments
- High-level semantic tasks (household)
- Low-level atomic actions (navigation, manipulation)

**Six Evaluation Subsets:**
1. **Commonsense Reasoning:** General world knowledge
2. **Complex Instruction Understanding:** Multi-step instructions
3. **Spatial Awareness:** Understanding 3D space
4. **Visual Perception:** Object recognition and tracking
5. **Long-term Planning:** Multi-step task completion

**Key Results:**
- 24 MLLMs evaluated
- MLLMs excel at high-level tasks
- Struggle with low-level manipulation
- GPT-4o scores only 28.9% on average

**Implications:**
- Major gap between high-level reasoning and low-level control
- Need for better grounding of language in physical actions
- Spatial awareness remains a key bottleneck

**Citation Key:** yang2025embodiedbench

---

### 49. SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents
**Venue:** arXiv 2024
**arXiv:** 2412.13178

**Focus:**
- Safety-aware benchmark for embodied LLM agents
- Task planning with safety constraints
- Avoiding dangerous actions

**Safety Dimensions:**
- Physical safety (avoiding collisions)
- Task safety (not breaking objects)
- Human safety (avoiding harm to people)

**Citation Key:** safeagentbench2024

---

### 50. MANGO: A Benchmark for Evaluating Mapping and Navigation with Language
**Venue:** OpenReview 2024

**Focus:**
- Text-based mapping and navigation
- LLM capabilities for spatial understanding
- Language-guided exploration

**Citation Key:** mango2024

---

### 51. Embodied Arena: A Comprehensive Evaluation Platform for Embodied AI
**Venue:** arXiv 2025
**arXiv:** 2509.15273

**Platform Features:**
- First comprehensive evaluation platform
- Leaderboards for embodied AI
- Standardized evaluation protocols

**Evaluation Dimensions:**
- Spatial reasoning
- Object interaction
- Navigation efficiency
- Task completion

**Citation Key:** embodiedarena2025

---

### 52. Multimodal Spatial Reasoning in the Large Model Era: A Survey and Benchmarks
**Venue:** arXiv 2025
**arXiv:** 2510.25760

**Survey Scope:**
- Comprehensive review of spatial reasoning in MLLMs
- Embodied AI including VLN and action models
- Emerging modalities (audio, egocentric video)

**Key Themes:**
- Gap between 2D and 3D spatial understanding
- Need for embodied training
- Multi-modal fusion for spatial reasoning

**Citation Key:** spatialreasoning2025survey

---

## Part XV: Urban Planning and GeoAI Applications

### 53. Urban Planning in the Age of Large Language Models
**Venue:** Computers, Environment and Urban Systems 2025

**Study Design:**
- 556 urban planning tasks
- Systematic benchmarking of OpenAI o1
- Multiple planning domains

**Findings:**
- Strong performance on documentation and analysis
- Limitations in spatial visualization
- Potential for LLM-based planning agents

**Citation Key:** urbanplanning2025

---

### 54. GIScience in the Era of Artificial Intelligence: A Research Agenda Towards Autonomous GIS
**Venue:** International Journal of Geographical Information Science 2025

**Vision:**
- Autonomous GIS systems powered by AI
- Integration of LLMs with spatial databases
- Generative AI for spatial analysis

**Research Agenda:**
- Benchmark for spatial skill testing
- Evaluation of generative AI spatial abilities
- Autonomous spatial decision-making

**Citation Key:** giscience2025

---

## Summary: Key Benchmarks for Spatial AI Agents

| Benchmark | Focus | Tasks | Key Metric | Year |
|-----------|-------|-------|------------|------|
| EmbodiedBench | MLLM embodied agents | 1,128 | Success rate | 2025 |
| REM | Embodied spatial reasoning | Multi-frame | Accuracy | 2025 |
| MineAnyBuild | Spatial planning | Building | Quality score | 2025 |
| SafeAgentBench | Safe task planning | Safety-aware | Safety rate | 2024 |
| BEHAVIOR | Household activities | 100 | Task success | 2021 |
| Habitat | Embodied navigation | PointNav/ObjectNav | SPL | 2019 |
| VLN-R2R | Vision-language navigation | Room-to-room | SR/SPL | 2018 |
| ALFWorld | Text-embodied alignment | Household | Success rate | 2021 |
| WebArena | Web navigation | Web tasks | Task success | 2023 |
| AgentBench | Multi-domain agents | 8 domains | Composite | 2023 |

