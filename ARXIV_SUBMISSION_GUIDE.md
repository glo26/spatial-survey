# arXiv Submission Guide: From Perception to Action

## Complete A+ Submission Checklist

This guide provides step-by-step instructions for submitting your survey paper to arXiv with all required metadata for maximum visibility and impact.

---

## 📦 Submission Package Contents

Your submission package (`spatial-ai-survey-arxiv.zip`) contains:

| File | Description | Size |
|------|-------------|------|
| `main.tex` | LaTeX source file | 100 KB |
| `main.bbl` | Pre-compiled bibliography (742 citations) | 207 KB |
| `taxonomy.png` | Three-axis taxonomy figure | 137 KB |

**Total package size:** ~228 KB (well under arXiv's 50MB limit)

---

## 🔐 Step 1: Create/Login to arXiv Account

1. Go to https://arxiv.org/user/login
2. If new user: Click "Register" and complete verification
3. Login with your credentials

**Important:** Use an institutional email if possible (higher trust score)

---

## 📤 Step 2: Start New Submission

1. Click **"Submit"** in the top navigation
2. Select **"Start New Submission"**

---

## 📂 Step 3: Select License

**Recommended License:** `arXiv.org perpetual, non-exclusive license to distribute this article`

This allows:
- arXiv to host and distribute
- You retain copyright
- Others can read and cite freely

---

## 🏷️ Step 4: Select Primary Category

### Primary Category (REQUIRED)
```
cs.AI - Artificial Intelligence
```

### Cross-List Categories (RECOMMENDED - Select all that apply)
```
cs.CV - Computer Vision and Pattern Recognition
cs.RO - Robotics
cs.LG - Machine Learning
cs.MA - Multiagent Systems
```

**Rationale:** This survey spans AI agents, computer vision, robotics, and machine learning. Cross-listing maximizes visibility to all relevant communities.

---

## ✍️ Step 5: Enter Metadata

### Title
```
From Perception to Action: Spatial AI Agents and World Models
```

### Authors (in order)
```
Gloria Felicia, Nolan Bryant, Handi Putra, Ayaan Gazali, Eliel Lobo, Esteban Rojas
```

**Author Format Notes:**
- Use full names (First Last)
- Separate with commas
- Order matches paper

### Abstract
```
While large language models have become the prevailing approach for agentic reasoning and planning, their success in symbolic domains does not readily translate to the physical world. Spatial intelligence—the ability to perceive 3D structure, reason about object relationships, and act under physical constraints—is an orthogonal capability that proves important for embodied agents. Existing surveys address either agentic architectures or spatial domains in isolation; none provide a unified framework connecting these complementary capabilities. This paper bridges that gap. Through a thorough review of over 2,000 papers, citing 742 works from top-tier venues, we introduce a unified three-axis taxonomy connecting agentic capabilities with spatial tasks across scales. Crucially, we distinguish spatial grounding (metric understanding of geometry and physics) from symbolic grounding (associating images with text), arguing that perception alone does not confer agency. Our analysis reveals three key findings mapped to these axes: (1) hierarchical memory systems (Capability axis) are important for long-horizon spatial tasks; (2) GNN-LLM integration (Task axis) is a promising approach for structured spatial reasoning; and (3) world models (Scale axis) are essential for safe deployment across micro-to-macro spatial scales. We conclude by identifying six grand challenges and outlining directions for future research, including the need for unified evaluation frameworks to standardize cross-domain assessment. This taxonomy provides a foundation for unifying fragmented research efforts and enabling the next generation of spatially-aware autonomous systems in robotics, autonomous vehicles, and geospatial intelligence.
```

### Comments (Optional but HIGHLY RECOMMENDED)
```
61 pages, 742 citations, 6 figures, 8 tables. Survey paper on spatial AI agents, embodied AI, graph neural networks, and world models. Code and supplementary materials: https://github.com/glo26/spatial-survey
```

**Why this matters:** Comments appear on the abstract page and help readers quickly assess the paper's scope.

### Report Number (Optional)
```
AtlasPro-AI-2026-001
```

### Journal Reference (Leave blank)
Leave empty for initial submission. Update after acceptance.

### DOI (Leave blank)
Leave empty. arXiv will assign one.

### ACM Classification (Optional)
```
I.2.9 Robotics; I.2.10 Vision and Scene Understanding; I.2.11 Distributed Artificial Intelligence
```

### MSC Classification (Optional)
Leave blank (primarily for mathematics papers)

---

## 📎 Step 6: Upload Files

1. Click **"Add Files"** or drag-and-drop
2. Upload `spatial-ai-survey-arxiv.zip`
3. arXiv will automatically extract and process

**Alternative:** Upload files individually:
- `main.tex` (main source)
- `main.bbl` (bibliography)
- `taxonomy.png` (figure)

---

## ⚙️ Step 7: Process and Preview

1. Click **"Process"**
2. Wait for arXiv to compile (usually 1-5 minutes)
3. **CRITICAL:** Click **"View"** to preview the PDF
4. Verify:
   - [ ] All 61 pages render correctly
   - [ ] Figure displays properly
   - [ ] All 742 citations resolve
   - [ ] No LaTeX errors or warnings
   - [ ] Tables format correctly

---

## ✅ Step 8: Final Submission

1. Review all metadata one final time
2. Check the box confirming you have rights to submit
3. Click **"Submit"**

---

## 📅 Step 9: Post-Submission Timeline

| Event | Timeline |
|-------|----------|
| Submission received | Immediate confirmation email |
| Moderation review | 1-3 business days |
| Paper goes live | Next announcement (usually 8pm ET) |
| arXiv ID assigned | Upon going live (format: 2602.XXXXX) |

---

## 🎯 Optimization Tips for Maximum Impact

### 1. Timing Your Submission
- **Best days:** Sunday-Tuesday (appears in Monday-Wednesday announcements)
- **Avoid:** Friday submissions (weekend backlog)
- **Time:** Submit before 2pm ET for same-day processing

### 2. Title Optimization
Your title is strong because it:
- ✅ Contains searchable keywords (Spatial AI, Agents, World Models)
- ✅ Indicates scope (Perception to Action)
- ✅ Is concise yet descriptive

### 3. Abstract Optimization
Your abstract is optimized because it:
- ✅ States the problem clearly (first sentence)
- ✅ Quantifies contribution (742 citations, 2,000+ papers reviewed)
- ✅ Lists specific findings (three key findings)
- ✅ Mentions practical applications (robotics, autonomous vehicles)

### 4. Cross-Listing Strategy
Cross-list to ALL relevant categories to maximize visibility:
- `cs.AI` - Primary audience (AI researchers)
- `cs.CV` - Computer vision community
- `cs.RO` - Robotics community
- `cs.LG` - Machine learning community
- `cs.MA` - Multi-agent systems community

---

## 🔄 Post-Publication Actions

### Immediate (Day 1)
1. Share arXiv link on Twitter/X with key findings
2. Post to relevant subreddits (r/MachineLearning, r/robotics)
3. Update GitHub README with arXiv link

### Week 1
1. Submit to arXiv Daily (automated)
2. Add to Google Scholar profile
3. Share on LinkedIn with summary

### Month 1
1. Monitor citations via Google Scholar alerts
2. Respond to any comments or questions
3. Consider submitting to Semantic Scholar

---

## 📧 Correspondence Information

**Corresponding Author:** Gloria Felicia
**Email:** gloria.felicia@atlaspro.ai
**Institution:** AtlasPro AI

---

## 🔗 Associated Resources

| Resource | Link |
|----------|------|
| GitHub Repository | https://github.com/glo26/spatial-survey |
| Paper PDF | Included in package |
| BibTeX Citation | See below |

### BibTeX Citation (for README and sharing)
```bibtex
@article{felicia2026perception,
    title={From Perception to Action: Spatial AI Agents and World Models},
    author={Felicia, Gloria and Bryant, Nolan and Putra, Handi and 
            Gazali, Ayaan and Lobo, Eliel and Rojas, Esteban},
    journal={arXiv preprint arXiv:2602.XXXXX},
    year={2026}
}
```

---

## ⚠️ Common Issues and Solutions

### Issue: "Bibliography not found"
**Solution:** Ensure `main.bbl` is included (not `references.bib`). arXiv prefers pre-compiled `.bbl` files.

### Issue: "Figure not displaying"
**Solution:** Verify `taxonomy.png` is in the same directory as `main.tex` and the `\includegraphics` path is correct.

### Issue: "Compilation timeout"
**Solution:** The paper is large (61 pages). If timeout occurs, try submitting during off-peak hours (early morning ET).

### Issue: "Moderation hold"
**Solution:** This is normal for first-time submitters or papers with many citations. Wait 1-3 days. If longer, contact arXiv support.

---

## 📋 Pre-Submission Checklist

- [ ] All files included in zip (main.tex, main.bbl, taxonomy.png)
- [ ] Abstract copied and ready to paste
- [ ] Author list in correct order
- [ ] Primary category selected (cs.AI)
- [ ] Cross-list categories selected (cs.CV, cs.RO, cs.LG, cs.MA)
- [ ] Comments field prepared (page count, citation count, GitHub link)
- [ ] GitHub repository is public and accessible
- [ ] README updated with "arXiv preprint coming soon"

---

## 🏆 Success Metrics

After submission, track these metrics:

| Metric | Target (Week 1) | Target (Month 1) |
|--------|-----------------|------------------|
| Abstract views | 500+ | 2,000+ |
| PDF downloads | 200+ | 1,000+ |
| Citations | - | 5+ |
| GitHub stars | 50+ | 200+ |

---

**Good luck with your submission! This survey represents significant scholarly contribution to the field of Spatial AI.**
