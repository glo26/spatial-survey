#!/usr/bin/env python3
"""
GNN Network Visualization for AtlasPro AI Technical Report
Shows a fiber network graph with GNN message passing illustration
Dark army green version with high contrast and distinct patterns
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle
import matplotlib.lines as mlines
import numpy as np
import networkx as nx

# Set up the figure with high DPI for publication quality
fig, axes = plt.subplots(1, 2, figsize=(14, 7), dpi=300)

# Define dark army green color palette (monochromatic with contrast)
army_dark = '#2D4A22'       # Dark army green (primary)
army_medium = '#4A7C3F'     # Medium army green
army_light = '#6B9B5A'      # Light army green
army_pale = '#8FBC7A'       # Pale army green
army_lightest = '#B8D4A8'   # Lightest green
army_very_light = '#D4E8C8' # Very light green
white = '#FFFFFF'
black = '#000000'

# ============ Left Panel: Fiber Network Graph ============
ax1 = axes[0]
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title('Fiber Optic Network as Graph', fontsize=12, fontweight='bold', color=army_dark, pad=15)

# Create a sample fiber network graph
G = nx.Graph()

# Define node positions (representing network infrastructure)
node_positions = {
    'CO': (0, 0),           # Central Office
    'FDH1': (-0.8, 0.6),    # Fiber Distribution Hub 1
    'FDH2': (0.8, 0.6),     # Fiber Distribution Hub 2
    'FDH3': (-0.8, -0.6),   # Fiber Distribution Hub 3
    'FDH4': (0.8, -0.6),    # Fiber Distribution Hub 4
    'SP1': (-1.2, 1.0),     # Splice Point 1
    'SP2': (-0.4, 1.0),     # Splice Point 2
    'SP3': (0.4, 1.0),      # Splice Point 3
    'SP4': (1.2, 1.0),      # Splice Point 4
    'SP5': (-1.2, -1.0),    # Splice Point 5
    'SP6': (1.2, -1.0),     # Splice Point 6
}

# Define node types with distinct markers and army green colors
# (label, color, size, marker)
node_types = {
    'CO': ('Central\nOffice', army_dark, 400, 's'),           # Dark green square
    'FDH1': ('FDH', army_medium, 250, 'o'),                   # Medium green circle
    'FDH2': ('FDH', army_medium, 250, 'o'),
    'FDH3': ('FDH', army_medium, 250, 'o'),
    'FDH4': ('FDH', army_medium, 250, 'o'),
    'SP1': ('SP', army_light, 150, '^'),                      # Light green triangle
    'SP2': ('SP', army_light, 150, '^'),
    'SP3': ('SP', army_light, 150, '^'),
    'SP4': ('SP', army_light, 150, '^'),
    'SP5': ('SP', army_light, 150, '^'),
    'SP6': ('SP', army_light, 150, '^'),
}

# Add edges (fiber connections)
edges = [
    ('CO', 'FDH1', 2.5), ('CO', 'FDH2', 2.5), ('CO', 'FDH3', 2.5), ('CO', 'FDH4', 2.5),
    ('FDH1', 'SP1', 1.5), ('FDH1', 'SP2', 1.5),
    ('FDH2', 'SP3', 1.5), ('FDH2', 'SP4', 1.5),
    ('FDH3', 'SP5', 1.5),
    ('FDH4', 'SP6', 1.5),
    ('FDH1', 'FDH2', 1.0),  # Redundant connection
]

# Draw edges with varying widths (representing capacity)
for n1, n2, width in edges:
    x1, y1 = node_positions[n1]
    x2, y2 = node_positions[n2]
    ax1.plot([x1, x2], [y1, y2], color=army_pale, linewidth=width, alpha=0.8, zorder=1)

# Draw nodes with distinct markers
for node, (label, color, size, marker) in node_types.items():
    x, y = node_positions[node]
    ax1.scatter([x], [y], c=color, s=size, marker=marker, edgecolors='white', linewidths=2, zorder=5)
    if node == 'CO':
        ax1.text(x, y-0.2, label, ha='center', va='top', fontsize=8, color=army_dark, fontweight='bold')
    else:
        ax1.text(x, y+0.15, label, ha='center', va='bottom', fontsize=7, color=army_dark)

# Add legend for node types
legend_elements = [
    mlines.Line2D([], [], color=army_dark, marker='s', linestyle='None', markersize=12, 
                  markeredgecolor='white', label='Central Office'),
    mlines.Line2D([], [], color=army_medium, marker='o', linestyle='None', markersize=10, 
                  markeredgecolor='white', label='Fiber Distribution Hub'),
    mlines.Line2D([], [], color=army_light, marker='^', linestyle='None', markersize=8, 
                  markeredgecolor='white', label='Splice Point'),
    mlines.Line2D([], [], color=army_pale, linewidth=2, label='Fiber Connection'),
]
ax1.legend(handles=legend_elements, loc='lower left', fontsize=8, framealpha=0.95)

# ============ Right Panel: GNN Message Passing ============
ax2 = axes[1]
ax2.set_xlim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_title('GNN Message Passing Mechanism', fontsize=12, fontweight='bold', color=army_dark, pad=15)

# Draw a simplified 3-node example
center_pos = (0, 0)
neighbor_positions = [(-0.8, 0.6), (0.8, 0.6), (0, -0.8)]

# Draw edges first
for nx_pos, ny_pos in neighbor_positions:
    ax2.plot([0, nx_pos], [0, ny_pos], color=army_pale, linewidth=2, alpha=0.7, zorder=1)

# Draw message arrows (showing aggregation)
for i, (nx_pos, ny_pos) in enumerate(neighbor_positions):
    # Arrow from neighbor to center (message passing)
    ax2.annotate('', xy=(0, 0), xytext=(nx_pos*0.6, ny_pos*0.6),
                arrowprops=dict(arrowstyle='->', color=army_medium, lw=2.5, 
                              connectionstyle='arc3,rad=0.1'))

# Draw center node (target node) - dark army green filled
ax2.scatter([0], [0], c=army_dark, s=600, edgecolors='white', linewidths=3, zorder=10)
ax2.text(0, 0, '$h_i^{(l+1)}$', ha='center', va='center', fontsize=11, color='white', fontweight='bold')

# Draw neighbor nodes - medium army green
for i, (nx_pos, ny_pos) in enumerate(neighbor_positions):
    ax2.scatter([nx_pos], [ny_pos], c=army_light, s=400, edgecolors='white', linewidths=2, zorder=5)
    ax2.text(nx_pos, ny_pos, f'$h_{{j_{i+1}}}^{{(l)}}$', ha='center', va='center', 
             fontsize=9, color='white', fontweight='bold')

# Add attention weight labels
attention_labels = ['$\\alpha_{i,j_1}$', '$\\alpha_{i,j_2}$', '$\\alpha_{i,j_3}$']
label_positions = [(-0.55, 0.45), (0.55, 0.45), (0.15, -0.5)]
for label, (lx, ly) in zip(attention_labels, label_positions):
    ax2.text(lx, ly, label, ha='center', va='center', fontsize=9, color=army_medium, fontweight='bold')

# Add equation box
equation_box = FancyBboxPatch((-1.3, -1.4), 2.6, 0.35, 
                               boxstyle="round,pad=0.02,rounding_size=0.05",
                               facecolor=army_very_light, edgecolor=army_medium, linewidth=1.5)
ax2.add_patch(equation_box)
ax2.text(0, -1.22, r'$h_i^{(l+1)} = \sigma\left(\sum_{j \in \mathcal{N}(i)} \alpha_{ij} W h_j^{(l)}\right)$', 
         ha='center', va='center', fontsize=10, color=army_dark)

# Add step labels
ax2.text(-0.8, 1.2, '1. Collect neighbor\n    features', ha='left', va='center', 
         fontsize=9, color=army_dark, fontweight='bold')
ax2.text(0.3, 1.2, '2. Compute attention\n    weights', ha='left', va='center', 
         fontsize=9, color=army_medium, fontweight='bold')
ax2.text(-0.8, -0.2, '3. Aggregate with\n    weighted sum', ha='left', va='center', 
         fontsize=9, color=army_dark, fontweight='bold')

# Add annotation for the aggregation
ax2.annotate('Aggregated\nRepresentation', xy=(0.15, 0.15), xytext=(0.6, -0.3),
            fontsize=8, color=army_dark,
            arrowprops=dict(arrowstyle='->', color=army_dark, lw=1.5))

plt.tight_layout()

# Save in multiple formats
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/gnn_network.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/gnn_network.pdf', 
            bbox_inches='tight', facecolor='white', edgecolor='none')

print("GNN network visualization saved successfully!")
