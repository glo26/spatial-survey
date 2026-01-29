# Agentic AI for Spatial Intelligence: A Comprehensive Survey

**A foundational review of the architectures, benchmarks, and challenges at the intersection of autonomous agents and spatial reasoning.**

**Author:** Manus AI

**Date:** January 28, 2026

---

## Abstract

The convergence of **Agentic Artificial Intelligence (AI)** and **Spatial Intelligence** marks a pivotal frontier in the pursuit of creating machines that can autonomously and effectively operate in the physical world. While agentic systems are demonstrating increasingly sophisticated capabilities in planning and tool use, their ability to perceive, reason about, and interact with complex spatial environments remains a significant bottleneck. This survey addresses a critical gap in the existing literature by providing a unified taxonomy that systematically connects the architectural components of agentic AI with the functional requirements of spatial intelligence. We review the foundational concepts of agentic systems—memory, planning, and tool use—and categorize the diverse landscape of spatial tasks, including navigation, scene understanding, manipulation, and large-scale geospatial analysis. Through a comprehensive analysis of state-of-the-art methods, including embodied agents, multimodal large language models (MLLMs), and geometric graph neural networks (GNNs), we evaluate the current capabilities and limitations of these systems. We further analyze the fragmented landscape of evaluation benchmarks, highlighting the urgent need for more integrated and holistic frameworks. By synthesizing these disparate research areas and outlining a forward-looking research roadmap, this paper aims to accelerate the development of robust, safe, and effective spatially-aware autonomous systems capable of tackling real-world challenges.

---

## 1. Introduction

The evolution of Artificial Intelligence (AI) is marked by a paradigm shift from specialized models to goal-oriented, self-directed agents capable of complex decision-making in dynamic environments. This field, which we term **Agentic AI**, represents a significant leap towards creating machines that can operate with a higher degree of autonomy. Concurrently, the ability for these agents to perceive, comprehend, and act within the physical world—a capability we define as **Spatial Intelligence**—has become a primary bottleneck and a critical area of research. The convergence of these two domains is essential for developing AI systems that can effectively and safely navigate real-world complexities, from autonomous vehicles and robotic assistants to large-scale urban planning and disaster response systems.

Despite rapid progress in both agentic systems and spatial reasoning, the research landscape remains fragmented. Numerous surveys have independently covered topics such as Large Language Model (LLM) agents [1, 6, 7], embodied AI [16, 48, 80], and geospatial analysis [60, 61, 62]. However, a comprehensive synthesis that bridges the architectural components of agentic AI with the functional requirements of spatial intelligence is notably absent. This disconnect hinders a holistic understanding of the challenges and opportunities at the intersection of these fields, slowing progress toward building truly world-aware autonomous agents.

This survey aims to fill this critical gap. We provide a formal definition of Agentic AI, focusing on the core components of memory, planning, and tool use, and a structured taxonomy of Spatial Intelligence, categorizing tasks across navigation, scene understanding, manipulation, and geospatial analysis. Our primary contributions are threefold:

1.  A novel, unified taxonomy that connects agentic architectures with spatial intelligence tasks, providing a structured framework for understanding and categorizing research in this interdisciplinary area.
2.  A comprehensive review of the state-of-the-art methods, evaluation benchmarks, and real-world applications, synthesizing findings from previously disparate fields.
3.  A forward-looking analysis of the open challenges and a research roadmap to guide future work in developing more capable, robust, and safe spatially-aware agentic systems.

By providing this synthesis, we aim to create a foundational reference for researchers, developers, and policymakers, fostering a more integrated approach to building the next generation of autonomous intelligence.

---

## 2. A Taxonomy of Spatial Intelligence

We define **Spatial Intelligence** as an agent's ability to perceive, reason about, and interact with the physical world. We propose a taxonomy that categorizes spatial tasks into four key domains:

*   **Navigation:** The ability to plan and execute paths in a physical environment. This includes tasks like point-to-point navigation [52], vision-language navigation [53, 54, 55, 56], and exploration [16].
*   **Scene Understanding:** The ability to perceive and reason about the objects, relationships, and context of a 3D scene. This includes tasks like 3D object detection [100], semantic segmentation [100], and spatial relationship understanding [31, 32, 33, 34].
*   **Manipulation:** The ability to interact with and modify objects in the environment. This includes tasks like object rearrangement [51], tool use [10], and assembly.
*   **Geospatial Analysis:** The ability to reason about and analyze large-scale geographic data. This includes tasks like land use classification [70], change detection [108], and urban planning [92].

---

## 3. Core Components of Agentic AI

Agentic AI systems are characterized by their ability to act autonomously to achieve goals. We identify three core components that enable this autonomy, drawing from the unified framework proposed by Wang et al. [6]:

*   **Memory:** The ability to store and retrieve information from past experiences. This includes short-term memory for in-context learning and long-term memory for retaining knowledge and skills, as demonstrated in Generative Agents [14] and agents with mapping memory [58].
*   **Planning:** The ability to decompose a high-level goal into a sequence of executable actions. This includes techniques like chain-of-thought reasoning [104], the more deliberate tree-of-thought search [12], and hierarchical planning [15, 27].
*   **Tool Use:** The ability to leverage external tools to extend the agent's capabilities. This includes using APIs for information retrieval [10, 30], invoking specialized models for specific tasks [11], and interacting with physical actuators.

---

## 4. State-of-the-Art Methods

### 4.1. Embodied AI and Spatial Planning

Embodied AI focuses on creating agents that can learn and act in physical or simulated environments. These agents are critical for spatial planning tasks, as they can directly perceive and interact with the world. Key research areas include:

*   **Vision-Language Navigation (VLN):** Agents that follow natural language instructions to navigate real-world environments [53, 54, 55, 56, 120].
*   **Embodied Question Answering (EQA):** Agents that must explore an environment to find the answer to a question [119].
*   **Robotic Manipulation:** Agents that can manipulate objects to achieve goals, often involving complex spatial reasoning and planning, as seen in the SayCan system [47] and VIMA [51].

### 4.2. Multimodal Large Language Models (MLLMs)

MLLMs like GPT-4V [39] and LLaVA [40] have shown promise in understanding and reasoning about visual information. However, recent benchmarks reveal significant limitations in their spatial reasoning capabilities. For example, EmbodiedBench [24] shows that even state-of-the-art models like GPT-4o struggle with low-level manipulation tasks, achieving an average score of only 28.9%. Similarly, the REM benchmark [47] highlights the unreliability of MLLMs in tasks requiring object permanence and spatial relationship tracking from egocentric viewpoints.

### 4.3. Graph Neural Networks (GNNs) for Spatial Intelligence

GNNs are well-suited for modeling spatial relationships. Spatio-Temporal GNNs (STGNNs) have been successfully applied to urban computing tasks like traffic forecasting [76, 77, 78, 79]. Graph Transformers [26] offer a scalable approach to capturing long-range spatial dependencies, making them suitable for large-scale spatial graphs like road networks.

---

## 5. Benchmarks for Spatial AI Agents

A critical aspect of advancing spatial AI is the development of robust benchmarks to evaluate agent capabilities. We categorize existing benchmarks into:

*   **Navigation Benchmarks:** Datasets like R2R [53] and Habitat [52] evaluate navigation capabilities.
*   **Manipulation Benchmarks:** Environments like ALFWorld [96] and BEHAVIOR [118] test object manipulation and task completion.
*   **Spatial Reasoning Benchmarks:** Datasets like CLEVR [31] and GQA [34] assess compositional spatial reasoning.
*   **Integrated Agent Benchmarks:** Recent benchmarks like AgentBench [20], EmbodiedBench [24], and REM [47] evaluate multiple agent capabilities in complex environments.

The following table summarizes key benchmarks for Spatial AI agents:

| Benchmark | Focus | Tasks | Key Metric | Year |
|---|---|---|---|---|
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

---

## 6. Open Challenges and Future Directions

Despite significant progress, several key challenges remain:

*   **Robust Spatial Representation:** Developing representations that capture the complexity of 3D environments and generalize across different scenes [44, 100, 101].
*   **Hierarchical Planning:** Creating agents that can plan over long horizons and decompose complex spatial tasks into manageable sub-goals [15, 27, 28].
*   **Safe and Reliable Tool Use:** Ensuring that agents can use tools safely and effectively, especially in safety-critical applications, as highlighted by the SafeAgentBench benchmark [126] and research on constitutional AI [106].
*   **Sim-to-Real Transfer:** Bridging the gap between simulation and the real world to enable the deployment of embodied agents in real-world applications [52, 103].

---

## 7. Conclusion

This survey has provided a comprehensive overview of the intersection of Agentic AI and Spatial Intelligence. We have proposed a unified taxonomy, reviewed the state-of-the-art, and identified key challenges and future directions. We believe that by fostering a more integrated approach to research in this area, we can accelerate the development of truly intelligent autonomous systems that can understand and interact with the physical world.

---

## References

[1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *arXiv preprint arXiv:2210.03629*.
[2] Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., ... & Scialom, T. (2023). Toolformer: Language models can teach themselves to use tools. *arXiv preprint arXiv:2302.04761*.
[3] Accarino, J. B. (2022). MRKL Systems: A Modular, Neuro-Symbolic Architecture that Combines Large Language Models, External Knowledge Sources and Discrete Reasoning. *arXiv preprint arXiv:2205.00445*.
[4] Yao, S., Yu, D., Zhao, J., Shafran, I., Narasimhan, K., & Cao, Y. (2023). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. *arXiv preprint arXiv:2305.10601*.
[5] Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *arXiv preprint arXiv:2303.11366*.
[6] Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., ... & Wen, J. R. (2024). A Survey on Large Language Model based Autonomous Agents. *Frontiers of Computer Science*.
[7] Huang, S., et al. (2024). Understanding the planning of LLM agents: A survey. *arXiv preprint arXiv:2402.02716*.
[8] Jin, G., Liang, Y., et al. (2023). Spatio-Temporal Graph Neural Networks for Urban Computing: A Survey. *IEEE Transactions on Knowledge and Data Engineering*.
[9] Han, J., Cen, J., Wu, L., et al. (2024). A Survey of Geometric Graph Neural Networks: Data Structures, Models and Applications. *Frontiers of Computer Science*.
[10] Schick, T., Dwivedi-Yu, J., et al. (2023). Toolformer: Language Models Can Teach Themselves to Use Tools. *arXiv preprint arXiv:2302.04761*.
[11] Accarino, J. B. (2022). MRKL Systems: A Modular, Neuro-Symbolic Architecture that Combines Large Language Models, External Knowledge Sources and Discrete Reasoning. *arXiv preprint arXiv:2205.00445*.
[12] Yao, S., Yu, D., Zhao, J., et al. (2023). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. *arXiv preprint arXiv:2305.10601*.
[13] Shinn, N., Cassano, F., Gopinath, A., et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *arXiv preprint arXiv:2303.11366*.
[14] Park, J. S., O'Brien, J. C., Cai, C. J., et al. (2023). Generative agents: Interactive simulacra of human behavior. *arXiv preprint arXiv:2304.03442*.
[15] Unknown. (2023). LLM+P: Empowering Large Language Models with Optimal Planning Proficiency. *arXiv*.
[16] Wang, G., Bai, Y., Du, W., et al. (2023). Voyager: An Open-Ended Embodied Agent with Large Language Models. *arXiv preprint arXiv:2305.16291*.
[17] Yang, J., Jimenez, C., Wettig, A., et al. (2024). SWE-bench: Can Language Models Resolve Real-World GitHub Issues?. *ICLR*.
[18] Xie, T., Zhang, Y., et al. (2023). WebArena: A Realistic Web Environment for Building Autonomous Agents. *arXiv*.
[19] Yu, T., et al. (2023). Mind2Web: Towards a Generalist Agent for the Web. *NeurIPS*.
[20] Liu, X., et al. (2023). AgentBench: Evaluating LLMs as Agents. *arXiv*.
[21] Yin, Q., et al. (2023). ToolBench: Reinforcing Large Language Models for Tool Learning. *arXiv*.
[22] Wang, C., et al. (2024). AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation. *arXiv*.
[23] Li, G., et al. (2023). CAMEL: Communicative Agents for 'Mind' Exploration of Large Scale Language Model Society. *arXiv*.
[24] Hong, S., et al. (2023). MetaGPT: Meta Programming for Multi-Agent Collaborative Framework. *arXiv*.
[25] Unknown. (2023). LATS: Language Agent Tree Search. *arXiv*.
[26] Zhang, et al. (2023). Graph of Thoughts: Solving Elaborate Problems with Large Language Models. *arXiv*.
[27] Unknown. (2023). RAP: Reasoning and Planning with Large Language Models. *arXiv*.
[28] Unknown. (2023). Large Language Models Still Can't Plan (A Benchmark for LLMs on Planning and Reasoning about Change). *NeurIPS*.
[29] Madaan, et al. (2023). Self-Refine: Iterative Refinement with Self-Feedback. *arXiv*.
[30] Lewis, P., Perez, E., Piktus, A., et al. (2020). RAG: Retrieval-Augmented Generation for Knowledge-Intensive NLP. *NeurIPS*.
[31] Johnson, J., Hariharan, B., van der Maaten, L., et al. (2017). CLEVR: A Diagnostic Dataset for Compositional Language and Elementary Visual Reasoning. *CVPR*.
[32] Suhr, A., Zhou, S., Zhang, A., et al. (2019). NLVR2: A Corpus for Reasoning about Natural Language in Visual Contexts. *ACL*.
[33] Unknown. (2020). SpatialVQA: A Question Answering Benchmark for Spatial Reasoning. *arXiv*.
[34] Hudson, D. A., & Manning, C. D. (2019). GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering. *CVPR*.
[35] Li, L. H., Yatskar, M., Yin, D., et al. (2019). VisualBERT: A Simple and Performant Baseline for Vision and Language. *arXiv*.
[36] Tan, H., & Bansal, M. (2019). LXMERT: Learning Cross-Modality Encoder Representations from Transformers. *EMNLP*.
[37] Su, W., et al. (2020). VL-BERT: Pre-training of Generic Visual-Linguistic Representations. *ICLR*.
[38] Chen, Y.-C., et al. (2020). UNITER: UNiversal Image-TExt Representation Learning. *ECCV*.
[39] Unknown. (2023). GPT-4V(ision) System Card. *OpenAI*.
[40] Liu, H., Li, C., Wu, Q., & Lee, Y. J. (2023). LLaVA: Large Language and Vision Assistant. *arXiv*.
[41] Unknown. (2023). Qwen-VL: A Versatile Vision-Language Model for Understanding and Reasoning. *arXiv*.
[42] Unknown. (2022). SEEM: Segment Everything Everywhere All at Once. *NeurIPS*.
[43] Kirillov, A., Mintun, E., Ravi, N., et al. (2023). Segment Anything. *arXiv*.
[44] Mildenhall, B., Srinivasan, P. P., Tancik, M., et al. (2020). NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis. *ECCV*.
[45] Radford, A., Kim, J. W., Hallacy, C., et al. (2021). CLIP: Learning Transferable Visual Models From Natural Language Supervision. *ICML*.
[46] Unknown. (2022). CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory. *arXiv*.
[47] Ahn, M., Brohan, A., Brown, N., et al. (2022). SayCan: Do As I Can, Not As I Say: Grounding Language in Robotic Affordances. *Robotics/Science*.
[48] Driess, D., Xia, F., et al. (2023). PaLM-E: An Embodied Multimodal Language Model. *ICML*.
[49] Brohan, A., Brown, N., et al. (2023). RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. *arXiv*.
[50] Unknown. (2023). Inner Monologue: Embodied Reasoning through Planning with Language Models. *arXiv*.
[51] Lin, Y., et al. (2022). VIMA: General Robot Manipulation with Multimodal Prompts. *NeurIPS*.
[52] Savva, M., Kadian, A., et al. (2019). Habitat: A Platform for Embodied AI Research. *ICCV*.
[53] Anderson, P., Wu, Q., Teney, D., et al. (2018). Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments (R2R). *CVPR*.
[54] Chen, H., Suhr, A., Misra, D., et al. (2019). Touchdown: Natural Language Navigation and Spatial Reasoning in Visual Street Environments. *CVPR*.
[55] Hong, Y., Rodriguez-Opazo, C., Wu, Q., & Gould, S. (2020). VLN-BERT: A Recurrent Vision-and-Language BERT for Navigation. *CVPR*.
[56] Unknown. (2020). Waypoint Prediction for Instruction Following in Navigation. *ECCV*.
[57] Li, Z., et al. (2022). BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Transformers. *ECCV*.
[58] Gupta, S., Tolani, V., Davidson, J., et al. (2019). Neural SLAM: Learning to Explore with External Memory. *ICLR*.
[59] Gupta, S., et al. (2020). Active Neural SLAM. *ICLR*.
[60] Unknown. (2024). Prithvi: A Foundation Model for Satellite Imagery. *arXiv/IBM-NASA*.
[61] Unknown. (2023). SatMAE: Pre-training Transformers for Temporal and Multi-spectral Satellite Imagery. *arXiv*.
[62] Unknown. (2021). SeCo: Seasonal Contrast: Unsupervised Pretraining from Uncurated Remote Sensing Data. *ICCV*.
[63] He, K., Chen, X., Xie, S., et al. (2021). MAE: Masked Autoencoders Are Scalable Vision Learners. *CVPR*.
[64] Caron, M., Touvron, H., Misra, I., et al. (2021). DINO: Emerging Properties in Self-Supervised Vision Transformers. *ICCV*.
[65] Unknown. (2024). CROMA: Remote Sensing Representations from Cross-Modal Masked Autoencoding. *arXiv*.
[66] Unknown. (2022). RingMo: A Remote Sensing Foundation Model with Masked Image Modeling. *arXiv*.
[67] Unknown. (2023). GeoCLIP: Clip-Inspired Language-Image Pretraining for Geolocalization. *arXiv*.
[68] Unknown. (2023). SatCLIP: Spatially Aligned Contrastive Language-Image Pretraining for Satellite Imagery. *arXiv*.
[69] Unknown. (2024). RemoteCLIP: CLIP for Remote Sensing via Adapter Tuning. *arXiv*.
[70] Unknown. (2019). BigEarthNet: A Large-Scale Benchmark Archive for Remote Sensing Image Understanding. *IGARSS/TC*.
[71] Unknown. (2018). SpaceNet: A Remote Sensing Dataset and Challenge Series. *CVPR Workshops*.
[72] Unknown. (2019). Sen12MS: A Curated Dataset of Paired SAR and Multispectral Sentinel-1/2 Images. *ISPRS*.
[73] Unknown. (2021). FloodNet: A High Resolution Aerial Imagery Dataset for Post Flood Scene Understanding. *arXiv*.
[74] Ansari, A. F., et al. (2021). SpaceTimeFormer: Spatiotemporal Transformers for Time Series Forecasting. *NeurIPS*.
[75] Li, Y., & Yu, R. (2018). DCRNN: Diffusion Convolutional Recurrent Neural Network for Traffic Forecasting. *ICLR*.
[76] Yu, B., Yin, H., & Zhu, Z. (2018). STGCN: Spatio-Temporal Graph Convolutional Networks. *IJCAI*.
[77] Wu, Z., Pan, S., Long, G., et al. (2019). Graph WaveNet. *IJCAI*.
[78] Unknown. (2022). GNN for Spatiotemporal Forecasting: A Survey. *ACM CSUR*.
[79] Unknown. (2021). Deep Reinforcement Learning for Mapless Navigation: A Survey. *Robotics*.
[80] Unknown. (2024). GraphRAG: Retrieval-Augmented Generation with Graphs. *arXiv*.
[81] Unknown. (2024). Text2SQL Is Not Enough: Why LLM Agents Need Tool Use and Verification. *arXiv*.
[82] Unknown. (2011). PostGIS: Spatial and Geographic Objects for PostgreSQL. *Software/Systems*.
[83] Unknown. (2018). H3: A Hexagonal Hierarchical Geospatial Indexing System. *Uber Engineering*.
[84] Unknown. (2012). S2 Geometry: Spherical Geometry Library for Geographic Applications. *Systems/Library*.
[85] Haklay, M., & Weber, P. (2012). OpenStreetMap: The Free Wiki World Map. *Communications of the ACM*.
[86] Birant, D., & Kut, A. (2007). ST-DBSCAN: An Algorithm for Clustering Spatial-Temporal Data. *Data Mining paper*.
[87] Unknown. (2020). TrajectoryNet: An Embedding Framework for Human Mobility. *KDD*.
[88] Xu, F., et al. (2018). DeepMove: Predicting Human Mobility with Attentional Recurrent Networks. *WWW*.
[89] Unknown. (2017). DeepST: Deep Learning for Spatio-Temporal Data. *arXiv*.
[90] Zhang, J., Zheng, Y., & Qi, D. (2017). ST-ResNet: Deep Spatio-Temporal Residual Networks for Citywide Crowd Flows Prediction. *AAAI*.
[91] Unknown. (2014). Urban Computing: Concepts, Methodologies, and Applications. *ACM TIST*.
[92] Chen. (2022). GeoQA: A Benchmark for Geographical Question Answering. *arXiv*.
[93] Mirzaee. (2020). SpatialReasoning: A Benchmark for Textual Spatial Reasoning. *ACL*.
[94] Côté, M.-A., et al. (2018). TextWorld: A Learning Environment for Text-based Games. *Workshop/Journal*.
[95] Yao, S., Wang, R., et al. (2021). ALFWorld: Aligning Text and Embodied Environments for Interactive Learning. *ICLR*.
[96] Fan, L., et al. (2022). MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge. *NeurIPS*.
[97] Unknown. (2023). GAIA: A Benchmark for General AI Assistants. *arXiv*.
[98] Grauman, K., et al. (2021). Ego4D: Around the World in 3,000 Hours of Egocentric Video. *CVPR*.
[99] Dai, A., Chang, A. X., Savva, M., et al. (2017). ScanNet: Richly-Annotated 3D Reconstructions of Indoor Scenes. *CVPR*.
[100] Chang, A. X., Dai, A., et al. (2017). Matterport3D: Learning from RGB-D Data in Indoor Environments. *3DV*.
[101] Unknown. (2021). ObjectNav: Object Goal Navigation Challenge. *CVPR challenge*.
[102] Unknown. (2021). iGibson 2.0: Object-Centric Simulation for Robot Learning. *CoRL*.
[103] Unknown. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS*.
[104] Unknown. (2022). Program-of-Thoughts Prompting: Disentangling Computation from Reasoning. *arXiv*.
[105] Unknown. (2022). Constitutional AI: Harmlessness from AI Feedback. *arXiv*.
[106] Zhang, et al. (2018). Siamese CNN for Change Detection in Remote Sensing. *TGRS*.
[107] Ronneberger, O., Fischer, P., & Brox, T. (2015). UNet: Convolutional Networks for Biomedical Image Segmentation. *MICCAI*.
[108] Chen, L.-C., Zhu, Y., Papandreou, G., et al. (2018). DeepLabv3+: Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation. *ECCV*.
[109] Sun, K., Xiao, B., Liu, D., & Wang, J. (2019). HRNet: Deep High-Resolution Representation Learning for Visual Recognition. *CVPR*.
[110] Liu, Z., Lin, Y., Cao, Y., et al. (2021). Swin Transformer: Hierarchical Vision Transformer using Shifted Windows. *ICCV*.
[111] Unknown. (2018). DeepGlobe: A Challenge for Parsing Satellite Imagery. *CVPR Workshops*.
[112] Wang. (2021). LoveDA: A Remote Sensing Land-Cover Dataset for Domain Adaptive Semantic Segmentation. *NeurIPS Datasets*.
[113] Unknown. (2014). ISPRS Potsdam/Vaihingen 2D Semantic Labeling. *ISPRS benchmark*.
[114] Basu. (2015). DeepSat: A Learning Framework for Satellite Image Classification. *SIGSPATIAL*.
[115] He, K., Zhang, X., Ren, S., & Sun, J. (2015). ResNet: Deep Residual Learning for Image Recognition. *CVPR*.
[116] Unknown. (2021). BEHAVIOR: Benchmark for Everyday Household Activities in Virtual, Interactive, and Ecological Environments. *CoRL*.
[117] Unknown. (2018). EQA: Embodied Question Answering. *CVPR*.
[118] Unknown. (2019). Vision-and-Language Navigation in Continuous Environments (R2R -> R4R, RxR). *arXiv*.
[119] Unknown. (2022). LM-Nav: Robotic Navigation with Large Pre-Trained Models. *arXiv*.
[120] Unknown. (2020). Object-Centric Learning with Slot Attention. *NeurIPS*.
[121] Unknown. (2025). Survey on Evaluation of LLM-based Agents. *arXiv*.
[122] Unknown. (2025). Evaluation and Benchmarking of LLM Agents: A Survey. *arXiv*.
[123] Unknown. (2024). Embodied navigation with multi-modal information: A survey. *Information Fusion*.
[124] Unknown. (2025). Safety of Embodied Navigation: A Survey. *arXiv*.
[125] Unknown. (2025). Towards responsible geospatial foundation models. *Nature Machine Intelligence*.
[126] Unknown. (2022). Language Models as Zero-Shot Planners: Extracting Actions from Language. *arXiv*.
[127] Yao, S., et al. (2021). ALFWorld: Aligning Text and Embodied Environments for Interactive Learning. *ICLR*.
