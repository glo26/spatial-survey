#!/usr/bin/env python3
"""
AtlasPro AI System Architecture Diagram
Visualizes the complete system architecture with GNN backend, MCP layer, and Agent orchestration
B&W-friendly version with high contrast and distinct patterns
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
import matplotlib.lines as mlines
import numpy as np

# Set up the figure with high DPI for publication quality
fig, ax = plt.subplots(figsize=(14, 10), dpi=300)

# Define B&W-friendly color palette - high contrast grayscale
black = '#000000'
dark_gray = '#333333'
medium_gray = '#666666'
light_gray = '#CCCCCC'
very_light_gray = '#E8E8E8'
white = '#FFFFFF'

# Layer background colors (distinct grayscale shades)
layer1_bg = '#F5F5F5'  # Lightest - User Interface
layer2_bg = '#E0E0E0'  # Light - Orchestration
layer3_bg = '#D0D0D0'  # Medium - MCP
layer4_bg = '#C0C0C0'  # Darker - Backend
layer5_bg = '#B0B0B0'  # Darkest - Data

def draw_rounded_box(ax, x, y, width, height, color, edge_color, label, fontsize=10, bold=False, edge_width=2):
    """Draw a rounded rectangle with label"""
    box = FancyBboxPatch((x, y), width, height, 
                          boxstyle="round,pad=0.02,rounding_size=0.03",
                          facecolor=color, edgecolor=edge_color, linewidth=edge_width)
    ax.add_patch(box)
    weight = 'bold' if bold else 'normal'
    ax.text(x + width/2, y + height/2, label, ha='center', va='center', 
            fontsize=fontsize, fontweight=weight, color=black, wrap=True)
    return box

def draw_arrow(ax, start, end, color=black, style='->'):
    """Draw an arrow between two points"""
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color, lw=2))

# Set axis limits and remove axes
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(7, 9.6, 'AtlasPro AI System Architecture', ha='center', va='center',
        fontsize=16, fontweight='bold', color=black)

# ============ Layer 1: User Interface (Top) ============
draw_rounded_box(ax, 5.5, 8.5, 3, 0.8, layer1_bg, black, 'User Interface\n(Natural Language Queries)', fontsize=9, edge_width=2.5)

# ============ Layer 2: Agent Orchestration ============
orchestration_box = FancyBboxPatch((1, 6.5), 12, 1.6, 
                                    boxstyle="round,pad=0.02,rounding_size=0.05",
                                    facecolor=layer2_bg, edgecolor=black, linewidth=2.5)
ax.add_patch(orchestration_box)
ax.text(7, 7.9, 'Agentic Orchestration Layer', ha='center', va='center',
        fontsize=11, fontweight='bold', color=black)

# Sub-components of orchestration
draw_rounded_box(ax, 1.3, 6.7, 2.2, 0.9, white, dark_gray, 'ReAct\nReasoning', fontsize=8)
draw_rounded_box(ax, 3.7, 6.7, 2.2, 0.9, white, dark_gray, 'Memory\nManager', fontsize=8)
draw_rounded_box(ax, 6.1, 6.7, 2.2, 0.9, white, dark_gray, 'Task\nPlanner', fontsize=8)
draw_rounded_box(ax, 8.5, 6.7, 2.2, 0.9, white, dark_gray, 'Tool\nSelector', fontsize=8)
draw_rounded_box(ax, 10.9, 6.7, 2, 0.9, white, dark_gray, 'Safety\nGuard', fontsize=8)

# ============ Layer 3: MCP Protocol Layer ============
mcp_box = FancyBboxPatch((1, 4.8), 12, 1.3, 
                          boxstyle="round,pad=0.02,rounding_size=0.05",
                          facecolor=layer3_bg, edgecolor=black, linewidth=2.5)
ax.add_patch(mcp_box)
ax.text(7, 5.8, 'Model Context Protocol (MCP) Layer', ha='center', va='center',
        fontsize=11, fontweight='bold', color=black)

# MCP Tools
draw_rounded_box(ax, 1.5, 5.0, 2.5, 0.6, white, dark_gray, 'GNN Query Tools', fontsize=8)
draw_rounded_box(ax, 4.3, 5.0, 2.5, 0.6, white, dark_gray, 'Spatial Analysis', fontsize=8)
draw_rounded_box(ax, 7.1, 5.0, 2.5, 0.6, white, dark_gray, 'Network Ops', fontsize=8)
draw_rounded_box(ax, 9.9, 5.0, 2.5, 0.6, white, dark_gray, 'External APIs', fontsize=8)

# ============ Layer 4: Core AI Backend ============
backend_box = FancyBboxPatch((1, 2.5), 12, 2, 
                              boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor=layer4_bg, edgecolor=black, linewidth=2.5)
ax.add_patch(backend_box)
ax.text(7, 4.2, 'Core AI Backend', ha='center', va='center',
        fontsize=11, fontweight='bold', color=black)

# Backend components
draw_rounded_box(ax, 1.3, 2.7, 2.8, 1.2, white, dark_gray, 'Graph Neural\nNetwork Engine\n(GCN, GAT, GraphSAGE)', fontsize=8)
draw_rounded_box(ax, 4.4, 2.7, 2.5, 1.2, white, dark_gray, 'Spatio-Temporal\nGNN\n(DCRNN, STGCN)', fontsize=8)
draw_rounded_box(ax, 7.2, 2.7, 2.5, 1.2, white, dark_gray, 'World Model\n(Simulation &\nPrediction)', fontsize=8)
draw_rounded_box(ax, 10, 2.7, 2.8, 1.2, white, dark_gray, 'LLM Integration\n(GPT-4, Claude,\nGemini)', fontsize=8)

# ============ Layer 5: Data Layer ============
data_box = FancyBboxPatch((1, 0.5), 12, 1.7, 
                           boxstyle="round,pad=0.02,rounding_size=0.05",
                           facecolor=layer5_bg, edgecolor=black, linewidth=2.5)
ax.add_patch(data_box)
ax.text(7, 1.9, 'Data Platform', ha='center', va='center',
        fontsize=11, fontweight='bold', color=black)

# Data sources
draw_rounded_box(ax, 1.3, 0.7, 2.2, 0.9, white, dark_gray, 'Graph\nDatabase\n(Neo4j)', fontsize=7)
draw_rounded_box(ax, 3.7, 0.7, 2.2, 0.9, white, dark_gray, 'Vector\nStore\n(Embeddings)', fontsize=7)
draw_rounded_box(ax, 6.1, 0.7, 2.2, 0.9, white, dark_gray, 'Geospatial\nData\n(PostGIS)', fontsize=7)
draw_rounded_box(ax, 8.5, 0.7, 2.2, 0.9, white, dark_gray, 'Time Series\nDB\n(InfluxDB)', fontsize=7)
draw_rounded_box(ax, 10.9, 0.7, 2, 0.9, white, dark_gray, 'Document\nStore', fontsize=7)

# ============ Draw Arrows ============
# User to Orchestration
draw_arrow(ax, (7, 8.5), (7, 8.1))

# Orchestration to MCP
draw_arrow(ax, (7, 6.5), (7, 6.1))

# MCP to Backend
draw_arrow(ax, (7, 4.8), (7, 4.5))

# Backend to Data
draw_arrow(ax, (7, 2.5), (7, 2.2))

# Feedback arrows (right side)
ax.annotate('', xy=(13.3, 7.3), xytext=(13.3, 3.5),
            arrowprops=dict(arrowstyle='->', color=dark_gray, lw=1.5, 
                          connectionstyle='arc3,rad=0'))
ax.text(13.6, 5.4, 'Feedback\nLoop', ha='left', va='center', fontsize=8, 
        color=dark_gray, rotation=90)

# ============ External Data Sources (Left Side) ============
ax.text(0.3, 1.3, 'External\nData\nSources', ha='center', va='center', fontsize=8, 
        color=black, fontweight='bold')
draw_arrow(ax, (0.7, 1.3), (1, 1.3), color=dark_gray)

# ============ Legend ============
legend_elements = [
    mpatches.Patch(facecolor=layer1_bg, edgecolor=black, linewidth=2, label='User Interface'),
    mpatches.Patch(facecolor=layer2_bg, edgecolor=black, linewidth=2, label='Agent Orchestration'),
    mpatches.Patch(facecolor=layer3_bg, edgecolor=black, linewidth=2, label='MCP Protocol'),
    mpatches.Patch(facecolor=layer4_bg, edgecolor=black, linewidth=2, label='Core AI Backend'),
    mpatches.Patch(facecolor=layer5_bg, edgecolor=black, linewidth=2, label='Data Platform'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=9, framealpha=0.95,
          bbox_to_anchor=(0.99, 0.99))

plt.tight_layout()

# Save in multiple formats
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/system_architecture.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/system_architecture.pdf', 
            bbox_inches='tight', facecolor='white', edgecolor='none')

print("System architecture diagram saved successfully!")
