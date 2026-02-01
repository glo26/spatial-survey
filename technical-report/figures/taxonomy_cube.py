#!/usr/bin/env python3
"""
Three-Axis Taxonomy Cube for AtlasPro AI Technical Report
Visualizes Task × Capability × Scale taxonomy with representative methods
Dark army green version with distinct markers and high contrast for B&W printing
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Set up the figure with high DPI for publication quality
fig = plt.figure(figsize=(12, 10), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# Define dark army green color palette (monochromatic with contrast)
# Following same contrast theory as B&W version
army_dark = '#2D4A22'       # Dark army green (primary - replaces black)
army_medium = '#4A7C3F'     # Medium army green (replaces dark gray)
army_light = '#6B9B5A'      # Light army green (replaces medium gray)
army_pale = '#8FBC7A'       # Pale army green (replaces light gray)
army_lightest = '#B8D4A8'   # Lightest green for backgrounds
black = '#000000'
white = '#FFFFFF'

# Axis labels and positions
task_labels = ['Navigation', 'Scene\nUnderstanding', 'Manipulation', 'Geospatial\nAnalysis']
capability_labels = ['Memory', 'Planning', 'Tool Use']
scale_labels = ['Micro\n(<1m)', 'Meso\n(1-100m)', 'Macro\n(>100m)']

# Draw semi-transparent cube faces
def draw_cube_faces(ax):
    # Define vertices of the cube
    vertices = [
        [0, 0, 0], [4, 0, 0], [4, 3, 0], [0, 3, 0],  # bottom
        [0, 0, 3], [4, 0, 3], [4, 3, 3], [0, 3, 3]   # top
    ]
    
    # Define faces
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # front
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # back
        [vertices[0], vertices[3], vertices[7], vertices[4]],  # left
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # right
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # bottom
        [vertices[4], vertices[5], vertices[6], vertices[7]]   # top
    ]
    
    # Draw faces with subtle army green shading
    for face in faces:
        poly = Poly3DCollection([face], alpha=0.05)
        poly.set_facecolor(army_light)
        poly.set_edgecolor(army_dark)
        poly.set_linewidth(1.5)
        ax.add_collection3d(poly)

draw_cube_faces(ax)

# Draw grid lines inside the cube
for i in range(1, 4):
    ax.plot([i, i], [0, 0], [0, 3], color=army_medium, alpha=0.3, linewidth=0.5, linestyle='--')
    ax.plot([i, i], [3, 3], [0, 3], color=army_medium, alpha=0.3, linewidth=0.5, linestyle='--')

for i in range(1, 3):
    ax.plot([0, 0], [i, i], [0, 3], color=army_medium, alpha=0.3, linewidth=0.5, linestyle='--')
    ax.plot([4, 4], [i, i], [0, 3], color=army_medium, alpha=0.3, linewidth=0.5, linestyle='--')

for i in range(1, 3):
    ax.plot([0, 4], [0, 0], [i, i], color=army_medium, alpha=0.3, linewidth=0.5, linestyle='--')
    ax.plot([0, 4], [3, 3], [i, i], color=army_medium, alpha=0.3, linewidth=0.5, linestyle='--')

# Plot representative methods with distinct markers for B&W readability
# Axis mapping:
#   x: Task axis - 0.5=Navigation, 1.5=Scene Understanding, 2.5=Manipulation, 3.5=Geospatial Analysis
#   y: Capability axis - 0.5=Memory, 1.5=Planning, 2.5=Tool Use
#   z: Scale axis - 0.5=Micro (<1m), 1.5=Meso (1-100m), 2.5=Macro (>100m)

# Different markers for different method categories - using army green shades
methods = [
    # (x, y, z, name, marker, facecolor, edgecolor, size)
    (0.5, 0.5, 1.5, 'VLMaps', 'o', army_pale, army_dark, 200),           # Navigation, Memory, Meso
    (2.5, 1.5, 0.5, 'SayCan', 's', army_light, army_dark, 200),          # Manipulation, Planning, Micro
    (2.5, 2.5, 0.5, 'RT-2', '^', army_medium, army_dark, 200),           # Manipulation, Tool Use, Micro
    (2.0, 1.5, 1.5, 'DreamerV3', 'D', army_light, army_dark, 250),       # All tasks (center), Planning, All scales
    (3.5, 0.5, 2.5, 'Prithvi', 'p', army_pale, army_dark, 250),          # Geospatial, Memory, Macro
    (3.2, 0.8, 2.3, 'DCRNN', 'h', army_light, army_dark, 200),           # Geospatial, Memory, Macro (offset)
    (3.5, 1.5, 2.5, 'AtlasPro AI', '*', army_dark, 'white', 450),        # Geospatial, Planning, Macro - HIGHLIGHTED
]

for x, y, z, name, marker, facecolor, edgecolor, size in methods:
    if name == 'AtlasPro AI':
        # Special styling for AtlasPro AI - large dark army green star with white edge
        ax.scatter([x], [y], [z], c=facecolor, s=size, marker=marker, edgecolors=edgecolor, linewidths=2, zorder=10)
        ax.text(x+0.15, y+0.15, z+0.25, name, fontsize=10, fontweight='bold', color=army_dark,
                ha='left', va='bottom',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=army_dark, alpha=0.9))
    else:
        ax.scatter([x], [y], [z], c=facecolor, s=size, marker=marker, edgecolors=edgecolor, linewidths=1.5, zorder=5)
        ax.text(x+0.1, y+0.1, z+0.15, name, fontsize=8, color=army_dark, ha='left', va='bottom')

# Set axis labels with proper positioning
ax.set_xlabel('Spatial Task', fontsize=12, fontweight='bold', labelpad=15, color=army_dark)
ax.set_ylabel('Agentic Capability', fontsize=12, fontweight='bold', labelpad=15, color=army_dark)
ax.set_zlabel('Spatial Scale', fontsize=12, fontweight='bold', labelpad=15, color=army_dark)

# Set tick labels
ax.set_xticks([0.5, 1.5, 2.5, 3.5])
ax.set_xticklabels(task_labels, fontsize=8, ha='center', color=army_dark)
ax.set_yticks([0.5, 1.5, 2.5])
ax.set_yticklabels(capability_labels, fontsize=9, color=army_dark)
ax.set_zticks([0.5, 1.5, 2.5])
ax.set_zticklabels(scale_labels, fontsize=9, color=army_dark)

# Set axis limits
ax.set_xlim(0, 4)
ax.set_ylim(0, 3)
ax.set_zlim(0, 3)

# Set viewing angle for best visibility
ax.view_init(elev=20, azim=45)

# Add title
plt.title('Three-Axis Taxonomy: Task × Capability × Scale\nfor Spatial Intelligence Systems', 
          fontsize=14, fontweight='bold', color=army_dark, pad=20)

# Create legend with distinct markers (army green palette)
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=army_pale, markeredgecolor=army_dark, 
               markersize=10, label='Navigation/Memory'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=army_light, markeredgecolor=army_dark, 
               markersize=10, label='Planning Methods'),
    plt.Line2D([0], [0], marker='^', color='w', markerfacecolor=army_medium, markeredgecolor=army_dark, 
               markersize=10, label='Tool Use Methods'),
    plt.Line2D([0], [0], marker='D', color='w', markerfacecolor=army_light, markeredgecolor=army_dark, 
               markersize=10, label='World Models'),
    plt.Line2D([0], [0], marker='*', color='w', markerfacecolor=army_dark, markeredgecolor='white', 
               markersize=15, label='AtlasPro AI'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=9, framealpha=0.95)

# Remove background panes for cleaner look
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor(army_lightest)
ax.yaxis.pane.set_edgecolor(army_lightest)
ax.zaxis.pane.set_edgecolor(army_lightest)

plt.tight_layout()

# Save in multiple formats
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/taxonomy_cube.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/taxonomy_cube.pdf', 
            bbox_inches='tight', facecolor='white', edgecolor='none')

print("Taxonomy cube figure saved successfully!")
