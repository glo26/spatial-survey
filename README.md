# Autonomous Spatial Intelligence: A Survey of Agentic AI Methods and Evaluation

[![arXiv](https://img.shields.io/badge/arXiv-2601.XXXXX-b31b1b.svg)](https://arxiv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This repository contains the research materials for a comprehensive survey on Autonomous Spatial Intelligence, exploring the intersection of Agentic AI architectures and spatial intelligence tasks.

## Authors

**Gloria Felicia, Nolan Bryant, Handi Putra, Ayaan Gazali, Eliel Lobo, Esteban Rojas**

AtlasPro AI

## Repository Structure

```
spatial-survey/
├── conference/                    # Conference paper version (IEEE, NeurIPS, ICLR)
│   ├── main.tex                   # LaTeX source (21 pages)
│   ├── main.pdf                   # Compiled PDF
│   └── references.bib             # Bibliography (1,165 references)
│
├── technical-report/              # Technical report version (arXiv)
│   ├── main.tex                   # LaTeX source (16 pages)
│   ├── main.pdf                   # Compiled PDF
│   └── references.bib             # Bibliography (1,165 references)
│
├── versions/                      # Previous versions archive
│   ├── main-v1.tex                # Version 1 LaTeX source
│   └── main-v1.pdf                # Version 1 PDF
│
├── latex/                         # Original LaTeX working directory
│   ├── conference_paper.tex       # Conference paper source
│   ├── conference_paper.pdf       # Conference paper PDF
│   ├── technical_report.tex       # Technical report source
│   ├── technical_report.pdf       # Technical report PDF
│   └── references.bib             # Master bibliography
│
├── Comprehensive_Spatial_AI_Survey.md   # Full survey in Markdown format
├── paper_insights.md              # Research notes and insights
├── survey_framework.md            # A+ framework for survey writing
├── top_survey_analysis.md         # Analysis of top survey papers
└── README.md                      # This file
```

## Paper Versions

### Conference Paper (21 pages)

**Title:** Autonomous Spatial Intelligence: A Survey of Agentic AI Methods and Evaluation

**Target Venues:** IEEE, NeurIPS, ICLR, ICML

This version follows the "Attention Is All You Need" formatting style with 208 carefully curated citations. It provides comprehensive coverage of agentic architectures, embodied AI, spatial reasoning, and industry applications in a format suitable for top-tier conference submission.

### Technical Report (16 pages)

**Title:** Autonomous Spatial Intelligence: A Comprehensive Technical Report

**Target Venue:** arXiv preprint

This version provides more exhaustive coverage with an expanded bibliography, suitable for technical documentation and reference purposes.

## Key Contributions

This survey provides a unified framework for understanding the intersection of two critical AI domains: Agentic AI and Spatial Intelligence.

1. **Unified Taxonomy:** A novel taxonomy connecting agentic AI architectures (memory, planning, tool use) with spatial intelligence tasks (navigation, scene understanding, manipulation, geospatial analysis).

2. **Comprehensive Review:** Analysis of over 250 papers covering state-of-the-art methods, evaluation benchmarks, and real-world industry applications from Palantir, ESRI, Foursquare, Google, Waymo, and other industry leaders.

3. **Forward-Looking Analysis:** Identification of open challenges and a research roadmap for autonomous spatial intelligence.

## Bibliography

The repository contains 1,165 unique references covering:

- Agentic AI Architectures (ReAct, Reflexion, Tree of Thoughts, Multi-Agent Systems)
- Embodied AI and VLA Models (RT-2, PaLM-E, Octo, OpenVLA, Voyager, SayCan)
- Spatial Reasoning and Navigation (VLN, Habitat, ZSON, VLMaps)
- GNN and Spatio-Temporal Networks (DCRNN, STGCN, Graph WaveNet)
- 3D Scene Understanding (ScanNet, Matterport3D, NeRF, 3D Gaussian Splatting)
- Geospatial AI and Remote Sensing (GeoFM, SatCLIP, SSL4EO)
- World Models (Dreamer, Genie, Sora, WorldDreamer)
- Foundation Models (CLIP, SAM, DINOv2, Grounding DINO)

## Compilation

To compile the LaTeX papers:

```bash
cd conference/  # or technical-report/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Citation

If you find our work useful in your research, please consider citing our paper:

```bibtex
@article{felicia2026autonomous,
    title={Autonomous Spatial Intelligence: A Survey of Agentic AI Methods and Evaluation},
    author={Felicia, Gloria and Bryant, Nolan and Putra, Handi and Gazali, Ayaan and Lobo, Eliel and Rojas, Esteban},
    journal={arXiv preprint arXiv:2601.XXXXX},
    year={2026}
}
```

## License

MIT License

## Contact

For questions or collaboration inquiries, please contact the authors at AtlasPro AI.
