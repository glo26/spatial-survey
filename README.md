# Agentic AI for Spatial Intelligence: A Comprehensive Survey

[![Conference](https://img.shields.io/badge/Conference-IEEE%20AIVR%202026-blue)](https://ieeevr.org/2026/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![arXiv](https://img.shields.io/badge/arXiv-2601.12345-b31b1b.svg)](https://arxiv.org/abs/2601.12345) <!-- Replace with actual arXiv ID -->

This repository contains the official LaTeX source and supplementary materials for our comprehensive survey, **"Agentic AI for Spatial Intelligence: A Comprehensive Survey"**, accepted at the 2026 IEEE International Conference on Artificial Intelligence and Virtual Reality (AIVR).

---

### Key Contributions

This survey provides a unified framework for understanding the intersection of two critical AI domains: **Agentic AI** and **Spatial Intelligence**. Our work aims to bridge the gap between autonomous agent architectures and the capabilities required for complex spatial reasoning and interaction.

1.  **A Novel, Unified Taxonomy:** We introduce a taxonomy that connects agentic architectures (e.g., memory, planning, tool use) with a spectrum of spatial intelligence tasks (e.g., navigation, scene understanding, geospatial analysis).

2.  **Comprehensive Review of SOTA Methods:** We systematically review state-of-the-art approaches, from embodied agents and multimodal LLMs to Graph Neural Networks, providing a structured overview of the current research landscape.

3.  **Analysis of Evaluation Frameworks:** We analyze existing benchmarks for both agentic AI and spatial reasoning, highlighting a critical need for integrated evaluation frameworks that can assess performance on complex, multi-step spatial tasks.

4.  **Applications in Critical Infrastructure:** We explore high-impact applications in areas such as urban planning, autonomous logistics, environmental monitoring, and industrial automation.

5.  **A Forward-Looking Research Roadmap:** We identify key open challenges and propose a detailed research roadmap to guide future work in developing more capable, robust, and safe spatially-aware agentic systems.

### Survey Scope and Taxonomy

Our survey is structured to provide a clear and comprehensive overview of the field. The core of our contribution is a taxonomy that organizes the research landscape into two main axes: **Agentic Capabilities** and **Spatial Task Domains**.

| | **Navigation & Path Planning** | **Scene Understanding** | **Manipulation & Interaction** | **Geospatial Analysis** |
| :--- | :--- | :--- | :--- | :--- |
| **Memory & World Models** | State representation, map building | Object permanence, relational memory | Affordance learning, state tracking | Spatiotemporal data storage |
| **Planning & Reasoning** | Goal decomposition, pathfinding | Causal inference, logical reasoning | Task and motion planning (TAMP) | Predictive modeling, anomaly detection |
| **Tool Use & Action** | API calls to navigation services | Visual question answering (VQA) | Robotic control primitives | GIS APIs, remote sensing data |

### Accessing the Paper

The full paper is available on arXiv and will be published in the IEEE AIVR 2026 conference proceedings.

*   **[Read the paper on arXiv](https://arxiv.org/abs/2601.12345)** (link will be active upon publication)

### Repository Structure

This repository is organized as follows:

```
spatial-survey/
├── latex/                # LaTeX source code for the paper
│   ├── main.tex
│   ├── references.bib
│   └── ...
├── figures/              # Source files for figures and diagrams
├── notes/                # Supplementary research notes and summaries
└── README.md             # This file
```

### How to Compile the Paper

To compile the LaTeX source code and generate a PDF of the paper, you will need a standard TeX distribution (e.g., TeX Live, MiKTeX). The following commands can be used:

```bash
cd latex/
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

This will generate a `main.pdf` file in the `latex/` directory.

### Citation

If you find our work useful in your research, please consider citing our paper:

```bibtex
@inproceedings{YourName2026AgenticSpatial,
    title={Agentic AI for Spatial Intelligence: A Comprehensive Survey},
    author={Author One and Author Two and Author Three},
    booktitle={2026 IEEE International Conference on Artificial Intelligence and Virtual Reality (AIVR)},
    year={2026},
    pages={1-12}, % Replace with actual page numbers
    doi={10.1109/AIVR.2026.XXXXXXX} % Replace with actual DOI
}
```

### Acknowledgments

This work was supported in part by the **MOVE Fellowship**. We also thank the anonymous reviewers for their insightful feedback.

### License

This work is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
