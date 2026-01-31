# From Perception to Action: Spatial AI Agents and World Models

[![arXiv](https://img.shields.io/badge/arXiv-Pending-b31b1b.svg)](https://arxiv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/glo26/spatial-survey?style=social)](https://github.com/glo26/spatial-survey)

This survey bridges the gap between agentic AI systems and spatial intelligence. We review over 800 papers to understand how AI agents can perceive, reason about, and act within the physical world.

## Authors

**Gloria Felicia, Nolan Bryant, Handi Putra, Ayaan Gazali, Eliel Lobo, Esteban Rojas**

AtlasPro AI

## What This Paper Is About

Large language models are remarkably good at reasoning and planning in symbolic domains, but they struggle when it comes to the physical world. Navigation agents hallucinate paths that don't exist. Manipulation planners propose grasps that are physically impossible. Embodied systems misjudge distances by orders of magnitude.

Why? Because spatial intelligence requires something fundamentally different: the ability to perceive 3D structure, reason about object relationships, and act under physical constraints. This is not just an incremental improvement over language understanding; it's an orthogonal capability.

We wrote this survey to bridge that gap. Through a systematic review of over 800 papers from top venues, we introduce a three-axis taxonomy that connects agentic capabilities (memory, planning, tool use) with spatial task domains (navigation, scene understanding, manipulation, geospatial analysis) across different spatial scales (micro, meso, macro).

## What We Contribute

1. **A Three-Axis Taxonomy**: A framework for organizing the intersection of agentic AI and spatial intelligence across scales.

2. **Analysis of 800+ Papers**: We identify key architectural patterns, including how GNNs are being integrated with LLMs, the rise of vision-language-action models, and the role of world models in planning.

3. **Comparison with Existing Surveys**: A quantitative look at what other surveys cover and where they leave gaps.

4. **Six Grand Challenges**: Research directions for the field, including the need for unified evaluation frameworks.

5. **Industry Design Patterns**: Lessons from real-world deployments at Waymo, Tesla, Palantir, ESRI, and others, abstracted into reusable patterns.

## Repository Structure

```
spatial-survey/
├── conference/                    # Main paper (58 pages)
│   ├── main.tex                   # LaTeX source
│   ├── main.pdf                   # Compiled PDF
│   └── references.bib             # Bibliography
│
├── technical-report/              # Extended version
│   ├── main.tex
│   ├── main.pdf
│   └── references.bib
│
├── versions/                      # Archive of previous versions
└── README.md
```

## Paper Statistics

| Metric | Value |
|--------|-------|
| Pages | 58 |
| Unique Citations | 751 |
| Sections | 11 |
| Tables | 5 |
| Equations | 9 |

## Topics Covered

- **Agentic AI**: ReAct, Reflexion, Tree of Thoughts, Multi-Agent Systems
- **Embodied AI**: RT-2, PaLM-E, Octo, OpenVLA, Voyager, SayCan
- **Navigation**: VLN, Habitat, ZSON, VLMaps, VoxPoser
- **Graph Neural Networks**: DCRNN, STGCN, Graph WaveNet, GNN-LLM Integration
- **3D Understanding**: ScanNet, Matterport3D, NeRF, 3D Gaussian Splatting
- **World Models**: Dreamer, DreamerV2, DreamerV3, Genie, GAIA-1, Sora
- **Geospatial AI**: Prithvi, SatMAE, GeoAI, Remote Sensing Foundation Models
- **Industry**: Autonomous Vehicles, Robot Learning, Geospatial Intelligence

## Compilation

```bash
cd conference/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Citation

```bibtex
@article{felicia2026perception,
    title={From Perception to Action: Spatial AI Agents and World Models},
    author={Felicia, Gloria and Bryant, Nolan and Putra, Handi and Gazali, Ayaan and Lobo, Eliel and Rojas, Esteban},
    journal={arXiv preprint arXiv:Pending},
    year={2026}
}
```

## License

MIT License

## Contact

For questions or collaboration, reach out to the authors at AtlasPro AI.
