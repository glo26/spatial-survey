#!/usr/bin/env python3
"""
Research Roadmap Timeline for AtlasPro AI Technical Report
Shows the three-phase development plan with milestones
Dark army green version with high contrast for B&W printing
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon
import numpy as np

# Set up the figure with high DPI for publication quality
fig, ax = plt.subplots(figsize=(14, 8), dpi=300)

# Define dark army green color palette (monochromatic with contrast)
army_dark = '#2D4A22'       # Dark army green (primary)
army_medium = '#4A7C3F'     # Medium army green
army_light = '#6B9B5A'      # Light army green
army_pale = '#8FBC7A'       # Pale army green
army_lightest = '#B8D4A8'   # Lightest green
army_very_light = '#D4E8C8' # Very light green
white = '#FFFFFF'
black = '#000000'

# Set axis limits and remove axes
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis('off')

# Title
ax.text(7, 7.6, 'AtlasPro AI Research Roadmap: 2026-2027', ha='center', va='center',
        fontsize=16, fontweight='bold', color=army_dark)

# Timeline base
timeline_y = 4.0
ax.plot([1, 13], [timeline_y, timeline_y], color=army_dark, linewidth=3, zorder=1)

# Phase definitions with distinct army green shades
phases = [
    {
        'name': 'Phase 1: Foundation',
        'period': 'Q1-Q2 2026',
        'x_start': 1,
        'x_end': 4.5,
        'color': army_very_light,
        'edge_color': army_medium,
        'marker_fill': army_pale,
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
        'color': army_lightest,
        'edge_color': army_light,
        'marker_fill': army_light,
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
        'color': army_pale,
        'edge_color': army_dark,
        'marker_fill': army_dark,
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
    
    # Phase name
    ax.text((phase['x_start'] + phase['x_end']) / 2, timeline_y + 3.0, 
            phase['name'], ha='center', va='center',
            fontsize=11, fontweight='bold', color=army_dark)
    
    # Period
    ax.text((phase['x_start'] + phase['x_end']) / 2, timeline_y + 2.6, 
            phase['period'], ha='center', va='center',
            fontsize=9, color=army_medium, style='italic')
    
    # Deliverables
    deliverable_y = timeline_y + 2.1
    for i, deliverable in enumerate(phase['deliverables']):
        ax.text(phase['x_start'] + 0.2, deliverable_y - i * 0.35, 
                f'• {deliverable}', ha='left', va='center',
                fontsize=8, color=army_dark)
    
    # Timeline markers with distinct fills
    marker_x = (phase['x_start'] + phase['x_end']) / 2
    ax.scatter([marker_x], [timeline_y], c=phase['marker_fill'], s=150, 
               edgecolors='white', linewidths=2, zorder=5)
    
    # Metrics box (below timeline)
    metrics_box = FancyBboxPatch(
        (phase['x_start'], timeline_y - 2.5), 
        phase['x_end'] - phase['x_start'] - 0.1, 
        2.0,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor=white, 
        edgecolor=phase['edge_color'], 
        linewidth=1.5,
        linestyle='--'
    )
    ax.add_patch(metrics_box)
    
    # Metrics title
    ax.text((phase['x_start'] + phase['x_end']) / 2, timeline_y - 0.7, 
            'Success Metrics', ha='center', va='center',
            fontsize=9, fontweight='bold', color=army_medium)
    
    # Metrics
    metric_y = timeline_y - 1.1
    for i, metric in enumerate(phase['metrics']):
        ax.text(phase['x_start'] + 0.2, metric_y - i * 0.35, 
                f'✓ {metric}', ha='left', va='center',
                fontsize=8, color=army_dark)

# Draw arrows between phases
for i in range(len(phases) - 1):
    arrow_x = phases[i]['x_end'] - 0.05
    ax.annotate('', xy=(arrow_x + 0.1, timeline_y), xytext=(arrow_x - 0.2, timeline_y),
                arrowprops=dict(arrowstyle='->', color=army_dark, lw=2))

# Add year markers on timeline
year_markers = [
    (1.5, 'Q1'),
    (3.0, 'Q2'),
    (5.5, 'Q3'),
    (7.0, 'Q4'),
    (10.0, '2027')
]
for x, label in year_markers:
    ax.plot([x, x], [timeline_y - 0.15, timeline_y + 0.15], color=army_dark, linewidth=2)
    ax.text(x, timeline_y - 0.35, label, ha='center', va='top', fontsize=8, color=army_dark)

# Add legend with distinct patterns
legend_elements = [
    mpatches.Patch(facecolor=army_very_light, edgecolor=army_medium, linewidth=2, label='Phase 1: Foundation'),
    mpatches.Patch(facecolor=army_lightest, edgecolor=army_light, linewidth=2, label='Phase 2: Capability Expansion'),
    mpatches.Patch(facecolor=army_pale, edgecolor=army_dark, linewidth=2, label='Phase 3: Scale & Productization'),
]
ax.legend(handles=legend_elements, loc='lower center', fontsize=9, framealpha=0.95,
          ncol=3, bbox_to_anchor=(0.5, -0.02))

# Add "2026" label
ax.text(0.5, timeline_y, '2026', ha='right', va='center', fontsize=10, 
        fontweight='bold', color=army_dark)

plt.tight_layout()

# Save in multiple formats
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/research_roadmap.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/research_roadmap.pdf', 
            bbox_inches='tight', facecolor='white', edgecolor='none')

print("Research roadmap timeline saved successfully!")
