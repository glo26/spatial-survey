# From Perception to Action: Spatial AI Agents and World Models

[![arXiv](https://img.shields.io/badge/arXiv-2601.XXXXX-b31b1b.svg)](https://arxiv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/glo26/spatial-survey?style=social)](https://github.com/glo26/spatial-survey)

A comprehensive survey bridging **Agentic AI**, **Spatial Intelligence**, and **World Models** for physical world understanding. This paper introduces a unified three-axis taxonomy connecting agentic capabilities with spatial tasks across scales.

## Authors

**Gloria Felicia, Nolan Bryant, Handi Putra, Ayaan Gazali, Eliel Lobo, Esteban Rojas**

AtlasPro AI

## Abstract

While large language models have become the dominant paradigm for agentic reasoning and planning, their success in symbolic domains does not readily translate to the physical world. Spatial intelligence—the ability to perceive 3D structure, reason about object relationships, and act under physical constraints—is an orthogonal, not incremental, capability that is critical for embodied agents. This paper bridges that gap through a systematic review of over 800 peer-reviewed papers from top-tier venues, introducing a unified three-axis taxonomy connecting agentic capabilities with spatial tasks across scales.

## Key Contributions

1. **Unified Three-Axis Taxonomy**: A novel framework mapping agentic AI components (memory, planning, tool use) to spatial intelligence domains (navigation, scene understanding, manipulation, geospatial analysis) across spatial scales (micro, meso, macro).

2. **Comprehensive Analysis**: Review of 800+ papers identifying key architectural patterns including GNN-LLM integration, vision-language-action models, and world model-based planning.

3. **SpatialAgentBench**: A conceptual evaluation framework for standardizing cross-domain assessment of spatial AI agents.

4. **Industry Design Patterns**: Analysis of real-world deployments from Waymo, Tesla, Palantir, ESRI, and other industry leaders, abstracted into reusable design patterns.

## Repository Structure

```
spatial-survey/
├── conference/                    # Main conference paper (58 pages)
│   ├── main.tex                   # LaTeX source
│   ├── main.pdf                   # Compiled PDF
│   └── references.bib             # Bibliography (847 unique citations)
│
├── technical-report/              # Extended technical report
│   ├── main.tex                   # LaTeX source
│   ├── main.pdf                   # Compiled PDF
│   └── references.bib             # Bibliography
│
├── versions/                      # Previous versions archive
├── latex/                         # Original working directory
└── README.md                      # This file
```

## Paper Statistics

| Metric | Value |
|--------|-------|
| Pages | 58 |
| Unique Citations | 847 |
| Sections | 11 |
| Tables | 5 |
| Equations | 9 |

## Topics Covered

- **Agentic AI Architectures**: ReAct, Reflexion, Tree of Thoughts, Multi-Agent Systems
- **Embodied AI & VLA Models**: RT-2, PaLM-E, Octo, OpenVLA, Voyager, SayCan
- **Spatial Reasoning & Navigation**: VLN, Habitat, ZSON, VLMaps, VoxPoser
- **Graph Neural Networks**: DCRNN, STGCN, Graph WaveNet, GNN-LLM Integration
- **3D Scene Understanding**: ScanNet, Matterport3D, NeRF, 3D Gaussian Splatting
- **World Models**: Dreamer, DreamerV2, DreamerV3, Genie, GAIA-1, Sora
- **Geospatial AI**: Prithvi, SatMAE, GeoAI, Remote Sensing Foundation Models
- **Industry Applications**: Autonomous Vehicles, Robot Learning, Geospatial Intelligence

## Compilation

To compile the LaTeX paper:

```bash
cd conference/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Citation

If you find our work useful in your research, please consider citing:

```bibtex
@article{felicia2026perception,
    title={From Perception to Action: Spatial AI Agents and World Models},
    author={Felicia, Gloria and Bryant, Nolan and Putra, Handi and Gazali, Ayaan and Lobo, Eliel and Rojas, Esteban},
    journal={arXiv preprint arXiv:2601.XXXXX},
    year={2026}
}
```

## License

MIT License

## Contact

For questions or collaboration inquiries, please contact the authors at AtlasPro AI.
