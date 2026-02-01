#!/usr/bin/env python3
"""
Research Roadmap Timeline for AtlasPro AI Technical Report
Shows the three-phase development plan with milestones
Dark army green version with high contrast - MINIMIZING LIGHT GREEN
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon
import numpy as np

# Set up the figure with high DPI for publication quality
fig, ax = plt.subplots(figsize=(14, 8), dpi=300)

# Define DARK army green color palette - minimizing light green
army_darkest = '#1A3A1A'    # Darkest army green (primary)
army_dark = '#2D4A2D'       # Dark army green (secondary)
army_medium = '#3D5C3D'     # Medium army green (tertiary)
army_olive = '#4A6B4A'      # Olive green (accent)
army_sage = '#5A7A5A'       # Muted sage (minimal use)
off_white = '#F8F8F5'       # Off-white for backgrounds
white = '#FFFFFF'
black = '#000000'

# Set axis limits and remove axes
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis('off')

# Title
ax.text(7, 7.6, 'AtlasPro AI Research Roadmap: 2026-2027', ha='center', va='center',
        fontsize=16, fontweight='bold', color=army_darkest)

# Timeline base
timeline_y = 4.0
ax.plot([1, 13], [timeline_y, timeline_y], color=army_darkest, linewidth=3, zorder=1)

# Phase definitions with DARK army green shades - progressive darkening
phases = [
    {
        'name': 'Phase 1: Foundation',
        'period': 'Q1-Q2 2026',
        'x_start': 1,
        'x_end': 4.5,
        'color': army_sage,           # Lightest of the dark shades
        'edge_color': army_dark,
        'marker_fill': army_olive,
        'text_color': white,
        'deliverables': [
            'Graph database infrastructure',
            'Baseline GNN models',
            'MCP tool definitions',
            'Internal benchmarks'
        ],
        'metrics': [
            '>80% failure prediction',
            '10 agent queries',
            '5 core use cases'
        ]
    },
    {
        'name': 'Phase 2: Capability Expansion',
        'period': 'Q3-Q4 2026',
        'x_start': 4.5,
        'x_end': 8.5,
        'color': army_olive,          # Medium dark
        'edge_color': army_dark,
        'marker_fill': army_dark,
        'text_color': white,
        'deliverables': [
            'Spatio-temporal GNN',
            'World model for simulation',
            'Multi-agent coordination',
            '3-5 customer pilots'
        ],
        'metrics': [
            '>70% 90-day forecast',
            'Accurate simulation',
            '>30% efficiency gain'
        ]
    },
    {
        'name': 'Phase 3: Scale & Productization',
        'period': '2027',
        'x_start': 8.5,
        'x_end': 13,
        'color': army_dark,           # Darkest
        'edge_color': army_darkest,
        'marker_fill': army_darkest,
        'text_color': white,
        'deliverables': [
            'Production platform',
            'Self-improving system',
            'Vertical expansion',
            'Published research'
        ],
        'metrics': [
            '20+ customers',
            '$5M+ ARR',
            '2+ top-tier papers'
        ]
    }
]

# Draw phases
for phase in phases:
    # Phase box (above timeline)
    phase_box = FancyBboxPatch(
        (phase['x_start'], timeline_y + 0.3), 
        phase['x_end'] - phase['x_start'] - 0.1, 
        3.0,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=phase['color'], 
        edgecolor=phase['edge_color'], 
        linewidth=2.5
    )
    ax.add_patch(phase_box)
    
    # Phase name - white text on dark background
    ax.text((phase['x_start'] + phase['x_end']) / 2, timeline_y + 3.0, 
            phase['name'], ha='center', va='center',
            fontsize=11, fontweight='bold', color=phase['text_color'])
    
    # Period
    ax.text((phase['x_start'] + phase['x_end']) / 2, timeline_y + 2.6, 
            phase['period'], ha='center', va='center',
            fontsize=9, color=off_white, style='italic')
    
    # Deliverables - white text on dark background
    deliverable_y = timeline_y + 2.1
    for i, deliverable in enumerate(phase['deliverables']):
        ax.text(phase['x_start'] + 0.2, deliverable_y - i * 0.35, 
                f'• {deliverable}', ha='left', va='center',
                fontsize=8, color=phase['text_color'])
    
    # Timeline markers with distinct fills
    marker_x = (phase['x_start'] + phase['x_end']) / 2
    ax.scatter([marker_x], [timeline_y], c=phase['marker_fill'], s=150, 
               edgecolors='white', linewidths=2.5, zorder=5)
    
    # Metrics box (below timeline) - off-white background
    metrics_box = FancyBboxPatch(
        (phase['x_start'], timeline_y - 2.5), 
        phase['x_end'] - phase['x_start'] - 0.1, 
        2.0,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=off_white, 
        edgecolor=phase['edge_color'], 
        linewidth=1.5,
        linestyle='--'
    )
    ax.add_patch(metrics_box)
    
    # Metrics title
    ax.text((phase['x_start'] + phase['x_end']) / 2, timeline_y - 0.7, 
            'Success Metrics', ha='center', va='center',
            fontsize=9, fontweight='bold', color=army_dark)
    
    # Metrics - dark text on light background
    metric_y = timeline_y - 1.1
    for i, metric in enumerate(phase['metrics']):
        ax.text(phase['x_start'] + 0.2, metric_y - i * 0.35, 
                f'✓ {metric}', ha='left', va='center',
                fontsize=8, color=army_darkest)

# Draw arrows between phases
for i in range(len(phases) - 1):
    arrow_x = phases[i]['x_end'] - 0.05
    ax.annotate('', xy=(arrow_x + 0.1, timeline_y), xytext=(arrow_x - 0.2, timeline_y),
                arrowprops=dict(arrowstyle='->', color=army_darkest, lw=2))

# Add year markers on timeline
year_markers = [
    (1.5, 'Q1'),
    (3.0, 'Q2'),
    (5.5, 'Q3'),
    (7.0, 'Q4'),
    (10.0, '2027')
]
for x, label in year_markers:
    ax.plot([x, x], [timeline_y - 0.15, timeline_y + 0.15], color=army_darkest, linewidth=2)
    ax.text(x, timeline_y - 0.35, label, ha='center', va='top', fontsize=8, color=army_darkest)

# Add legend with distinct patterns - dark shades
legend_elements = [
    mpatches.Patch(facecolor=army_sage, edgecolor=army_dark, linewidth=2, label='Phase 1: Foundation'),
    mpatches.Patch(facecolor=army_olive, edgecolor=army_dark, linewidth=2, label='Phase 2: Capability Expansion'),
    mpatches.Patch(facecolor=army_dark, edgecolor=army_darkest, linewidth=2, label='Phase 3: Scale & Productization'),
]
ax.legend(handles=legend_elements, loc='lower center', fontsize=9, framealpha=0.98,
          ncol=3, bbox_to_anchor=(0.5, -0.02), edgecolor=army_dark, fancybox=False)

# Add "2026" label
ax.text(0.5, timeline_y, '2026', ha='right', va='center', fontsize=10, 
        fontweight='bold', color=army_darkest)

plt.tight_layout()

# Save in multiple formats
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/research_roadmap.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/research_roadmap.pdf', 
            bbox_inches='tight', facecolor='white', edgecolor='none')

print("Research roadmap timeline saved successfully!")
