# Spatial AI Research Repository

[![arXiv](https://img.shields.io/badge/arXiv-Pending-b31b1b.svg)](https://arxiv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This repository contains two complementary research documents on spatial AI, agentic systems, and graph neural networks for infrastructure intelligence.

## Authors

Gloria Felicia, Nolan Bryant, Handi Putra, Ayaan Gazali, Eliel Lobo, Esteban Rojas

AtlasPro AI

---

## Document 1: Survey Paper

**Title:** From Perception to Action: Spatial AI Agents and World Models

**Pages:** 58 | **Citations:** 751 | **Status:** Conference submission ready

### Overview

This survey bridges the gap between agentic AI systems and spatial intelligence. Through a systematic review of over 800 papers from top venues (NeurIPS, ICML, CVPR, ICLR, IROS), we introduce a three-axis taxonomy connecting agentic capabilities with spatial task domains across different scales.

### Key Contributions

1. **Three-Axis Taxonomy**: A framework organizing the intersection of agentic AI and spatial intelligence across Task (navigation, scene understanding, manipulation, geospatial analysis), Capability (memory, planning, tool use), and Scale (micro, meso, macro).

2. **Comprehensive Literature Analysis**: Systematic review of 800+ papers identifying architectural patterns, GNN-LLM integration approaches, and the role of world models in spatial planning.

3. **Industry Design Patterns**: Lessons from deployments at Waymo, Tesla, Palantir, Esri, and others, abstracted into reusable patterns.

4. **Six Grand Challenges**: Research directions including unified spatial representation, grounded long-horizon planning, safe deployment under uncertainty, sim-to-real transfer, scalable multi-agent coordination, and efficient edge deployment.

### Topics Covered

- Agentic AI (ReAct, Reflexion, Tree of Thoughts, Multi-Agent Systems)
- Embodied AI (RT-2, PaLM-E, Octo, OpenVLA, Voyager, SayCan)
- Navigation (VLN, Habitat, ZSON, VLMaps, VoxPoser)
- Graph Neural Networks (DCRNN, STGCN, Graph WaveNet, GNN-LLM Integration)
- 3D Understanding (ScanNet, Matterport3D, NeRF, 3D Gaussian Splatting)
- World Models (Dreamer, DreamerV3, Genie, GAIA-1, Cosmos)
- Geospatial AI (Prithvi, SatMAE, GeoAI, Remote Sensing Foundation Models)

---

## Document 2: Technical Report

**Title:** AtlasPro AI Technical Report: Building Agentic Geospatial Systems

**Version:** 1.0 | **Pages:** 106 | **Status:** Internal research document

### Overview

This technical report details AtlasPro AI's approach to building agentic geospatial systems for infrastructure network intelligence. It extends the survey paper with company-specific architectural decisions, competitive analysis, validated use cases, and a detailed research roadmap.

### Key Sections

1. **Competitive Landscape**: Analysis of legacy GIS platforms (Esri, Hexagon, CARTO), niche infrastructure monitoring solutions (LiveEO, Planet, IQGeo), and emerging GNN players (Ericsson, academic research). Includes a 4-quadrant positioning diagram.

2. **Technical Foundations**: Deep dive into graph neural networks for network topology, spatio-temporal modeling, and the Model Context Protocol (MCP) for tool integration.

3. **AtlasPro AI Architecture**: Six architectural principles, memory systems hierarchy, and agentic orchestration design.

4. **World Models for Spatial Intelligence**: Analysis of applicability for synthetic data generation, scenario planning, digital twins, and agent training.

5. **Validated Use Cases**: Three detailed use cases across Electric/Gas Utilities (grid resilience), Telecommunications (fiber network optimization), and Smart Cities (urban digital twins).

6. **Limitations and Dependencies**: Comprehensive analysis of data dependencies, GNN limitations, agentic system failure modes, and critical success factors.

7. **Future Predictions**: Research-backed market predictions with confidence levels (geospatial AI market growth, digital twin adoption, agentic AI paradigm shift).

8. **Research Roadmap**: Three-phase development plan (Foundation, Capability Expansion, Scale and Productization) with deliverables and success metrics.

### Figures

- Three-Axis Taxonomy Cube
- Competitive Landscape Quadrant
- System Architecture Diagram
- GNN Network Visualization
- Research Roadmap Timeline

---

## Repository Structure

```
spatial-survey/
├── conference/                    # Survey Paper (58 pages)
│   ├── main.tex                   # LaTeX source
│   ├── main.pdf                   # Compiled PDF
│   └── references.bib             # Bibliography (751 citations)
│
├── technical-report/              # Technical Report (106 pages)
│   ├── main.tex                   # LaTeX source
│   ├── main.pdf                   # Compiled PDF
│   ├── references.bib             # Bibliography
│   ├── figures/                   # Generated figures
│   │   ├── taxonomy_cube.pdf
│   │   ├── competitive_quadrant.pdf
│   │   ├── system_architecture.pdf
│   │   ├── gnn_network.pdf
│   │   └── research_roadmap.pdf
│   ├── competitive_landscape.tex  # Competitive analysis section
│   ├── future_predictions.tex     # Market predictions section
│   ├── expanded_future_work.tex   # Research roadmap section
│   └── use_cases.tex              # Industry use cases section
│
├── versions/                      # Archive of previous versions
└── README.md
```

## Compilation

### Survey Paper

```bash
cd conference/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Technical Report

```bash
cd technical-report/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Citation

```bibtex
@article{felicia2026perception,
    title={From Perception to Action: Spatial AI Agents and World Models},
    author={Felicia, Gloria and Bryant, Nolan and Putra, Handi and 
            Gazali, Ayaan and Lobo, Eliel and Rojas, Esteban},
    journal={arXiv preprint arXiv:Pending},
    year={2026}
}

@techreport{atlaspro2026technical,
    title={AtlasPro AI Technical Report: Building Agentic Geospatial Systems},
    author={Felicia, Gloria and Bryant, Nolan and Putra, Handi and 
            Gazali, Ayaan and Lobo, Eliel and Rojas, Esteban},
    institution={AtlasPro AI},
    year={2026},
    type={Technical Report},
    number={v1.0}
}
```

## License

MIT License

## Contact

For questions or collaboration inquiries, contact the authors at AtlasPro AI.
