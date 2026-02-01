#!/usr/bin/env python3
"""
Three-Axis Taxonomy Cube for AtlasPro AI Technical Report
Visualizes Task × Capability × Scale taxonomy with representative methods
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Set up the figure with high DPI for publication quality
fig = plt.figure(figsize=(12, 10), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# Define color palette - navy blue monochromatic with accent colors
navy_dark = '#003366'
navy_medium = '#005599'
navy_light = '#0077CC'
accent_red = '#E63946'
accent_gold = '#F4A261'
accent_teal = '#2A9D8F'
light_gray = '#E8E8E8'

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
    
    # Draw faces with different colors for each axis plane
    face_colors = [
        (0, 0.3, 0.6, 0.08),  # front - blue tint
        (0, 0.3, 0.6, 0.08),  # back
        (0.1, 0.5, 0.4, 0.08),  # left - teal tint
        (0.1, 0.5, 0.4, 0.08),  # right
        (0.9, 0.6, 0.3, 0.08),  # bottom - gold tint
        (0.9, 0.6, 0.3, 0.08)   # top
    ]
    
    for face, color in zip(faces, face_colors):
        poly = Poly3DCollection([face], alpha=color[3])
        poly.set_facecolor(color[:3])
        poly.set_edgecolor(navy_dark)
        poly.set_linewidth(1.5)
        ax.add_collection3d(poly)

draw_cube_faces(ax)

# Draw grid lines inside the cube
for i in range(1, 4):
    # Vertical lines along Task axis
    ax.plot([i, i], [0, 0], [0, 3], color=navy_dark, alpha=0.3, linewidth=0.5, linestyle='--')
    ax.plot([i, i], [3, 3], [0, 3], color=navy_dark, alpha=0.3, linewidth=0.5, linestyle='--')

for i in range(1, 3):
    # Vertical lines along Capability axis
    ax.plot([0, 0], [i, i], [0, 3], color=navy_dark, alpha=0.3, linewidth=0.5, linestyle='--')
    ax.plot([4, 4], [i, i], [0, 3], color=navy_dark, alpha=0.3, linewidth=0.5, linestyle='--')

for i in range(1, 3):
    # Horizontal lines along Scale axis
    ax.plot([0, 4], [0, 0], [i, i], color=navy_dark, alpha=0.3, linewidth=0.5, linestyle='--')
    ax.plot([0, 4], [3, 3], [i, i], color=navy_dark, alpha=0.3, linewidth=0.5, linestyle='--')

# Plot representative methods as colored spheres
methods = [
    # (x, y, z, name, color, size)
    # x: Task (0-4), y: Capability (0-3), z: Scale (0-3)
    (0.5, 0.5, 1.5, 'VLMaps', navy_light, 200),           # Navigation, Memory, Meso
    (2.5, 1.5, 0.5, 'SayCan', accent_teal, 200),          # Manipulation, Planning, Micro
    (2.5, 2.5, 0.5, 'RT-2', accent_gold, 200),            # Manipulation, Tool Use, Micro
    (1.5, 1.5, 1.5, 'DreamerV3', navy_medium, 250),       # Scene Understanding, Planning, Meso
    (3.5, 0.5, 2.5, 'Prithvi', accent_teal, 200),         # Geospatial, Memory, Macro
    (3.5, 0.5, 2.5, 'DCRNN', navy_light, 180),            # Geospatial, Memory, Macro (offset)
    (3.5, 1.5, 2.5, 'AtlasPro AI', accent_red, 350),      # Geospatial, Planning, Macro - HIGHLIGHTED
]

# Offset DCRNN slightly to avoid overlap
methods[5] = (3.2, 0.8, 2.3, 'DCRNN', navy_light, 180)

for x, y, z, name, color, size in methods:
    if name == 'AtlasPro AI':
        # Special styling for AtlasPro AI - star marker
        ax.scatter([x], [y], [z], c=color, s=size, marker='*', edgecolors='white', linewidths=2, zorder=10)
        ax.text(x+0.15, y+0.15, z+0.25, name, fontsize=10, fontweight='bold', color=accent_red,
                ha='left', va='bottom')
    else:
        ax.scatter([x], [y], [z], c=color, s=size, marker='o', edgecolors='white', linewidths=1.5, zorder=5)
        ax.text(x+0.1, y+0.1, z+0.15, name, fontsize=8, color=navy_dark, ha='left', va='bottom')

# Set axis labels with proper positioning
ax.set_xlabel('Spatial Task', fontsize=12, fontweight='bold', labelpad=15, color=navy_dark)
ax.set_ylabel('Agentic Capability', fontsize=12, fontweight='bold', labelpad=15, color=navy_dark)
ax.set_zlabel('Spatial Scale', fontsize=12, fontweight='bold', labelpad=15, color=navy_dark)

# Set tick labels
ax.set_xticks([0.5, 1.5, 2.5, 3.5])
ax.set_xticklabels(task_labels, fontsize=8, ha='center')
ax.set_yticks([0.5, 1.5, 2.5])
ax.set_yticklabels(capability_labels, fontsize=9)
ax.set_zticks([0.5, 1.5, 2.5])
ax.set_zticklabels(scale_labels, fontsize=9)

# Set axis limits
ax.set_xlim(0, 4)
ax.set_ylim(0, 3)
ax.set_zlim(0, 3)

# Set viewing angle for best visibility
ax.view_init(elev=20, azim=45)

# Add title
plt.title('Three-Axis Taxonomy: Task × Capability × Scale\nfor Spatial Intelligence Systems', 
          fontsize=14, fontweight='bold', color=navy_dark, pad=20)

# Create legend
legend_elements = [
    mpatches.Patch(facecolor=navy_light, edgecolor='white', label='Navigation/Memory Methods'),
    mpatches.Patch(facecolor=accent_teal, edgecolor='white', label='Manipulation/Geospatial Methods'),
    mpatches.Patch(facecolor=accent_gold, edgecolor='white', label='Vision-Language-Action Models'),
    mpatches.Patch(facecolor=accent_red, edgecolor='white', label='AtlasPro AI (Target Position)'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=9, framealpha=0.9)

# Remove background panes for cleaner look
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('lightgray')
ax.yaxis.pane.set_edgecolor('lightgray')
ax.zaxis.pane.set_edgecolor('lightgray')

plt.tight_layout()

# Save in multiple formats
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/taxonomy_cube.png', 
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/taxonomy_cube.pdf', 
            bbox_inches='tight', facecolor='white', edgecolor='none')

print("Taxonomy cube figure saved successfully!")
