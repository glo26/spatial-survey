import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Set up the figure with a professional style
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(12, 10))

# Define dark army green color palette (monochromatic with contrast)
# Following same contrast theory as B&W version
army_dark = '#2D4A22'       # Dark army green (primary - replaces black)
army_medium = '#4A7C3F'     # Medium army green (replaces dark gray)
army_light = '#6B9B5A'      # Light army green (replaces medium gray)
army_pale = '#8FBC7A'       # Pale army green (replaces light gray)
army_lightest = '#B8D4A8'   # Lightest green for backgrounds
black = '#000000'
white = '#FFFFFF'
dark_gray = '#333333'

# Define the quadrant boundaries
ax.axhline(y=0, color=army_dark, linewidth=1.5, linestyle='-')
ax.axvline(x=0, color=army_dark, linewidth=1.5, linestyle='-')

# Set axis limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Define companies with their positions
# X-axis: Domain Specificity (Generic -> Infrastructure-Specific)
# Y-axis: AI Sophistication (Traditional/Rule-Based -> Agentic AI)
# Using distinct markers and army green palette with high contrast for B&W printing

companies = {
    # Quadrant 1: High AI, High Domain Specificity (Top Right) - AtlasPro AI's target
    'AtlasPro AI': (7.5, 8.5, army_dark, '*', 500),  # Dark army green filled star
    
    # Quadrant 2: High AI, Low Domain Specificity (Top Left) - Horizontal AI platforms
    'OpenAI': (-7, 7.5, army_medium, 'o', 200),
    'Anthropic': (-6, 6.5, army_medium, 'o', 180),
    'Google DeepMind': (-5, 8, army_medium, 'o', 220),
    'World Labs': (-3, 7, army_medium, 'o', 150),
    
    # Quadrant 3: Low AI, Low Domain Specificity (Bottom Left) - Generic tools
    'AWS': (-6, -3, army_light, 's', 180),
    'Microsoft Azure': (-5, -2, army_light, 's', 180),
    'Google Cloud': (-4, -4, army_light, 's', 180),
    
    # Quadrant 4: Low AI, High Domain Specificity (Bottom Right) - Legacy GIS/Infrastructure
    'Esri': (6, -5, army_pale, '^', 200),
    'Hexagon': (5, -6, army_pale, '^', 180),
    'CARTO': (3, -3, army_pale, '^', 150),
    'Mapbox': (2, -2, army_pale, '^', 150),
    'IQGeo': (7, -4, army_pale, '^', 140),
    'Planet': (4, -1, army_pale, '^', 140),
    'LiveEO': (5, -2, army_pale, '^', 130),
    
    # Emerging players in between
    'Ericsson (GNN)': (4, 3, army_medium, 'D', 120),
    'Academic Research': (3, 4, army_medium, 'D', 100),
}

# Plot each company
for company, (x, y, color, marker, size) in companies.items():
    if company == 'AtlasPro AI':
        # AtlasPro AI: Large dark army green filled star with white edge for visibility
        ax.scatter(x, y, c=army_dark, marker=marker, s=size, edgecolors='white', linewidths=2, zorder=10)
        ax.annotate(company, (x, y), xytext=(10, 10), textcoords='offset points',
                   fontsize=12, fontweight='bold', color=army_dark,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=army_dark, alpha=0.95))
    else:
        ax.scatter(x, y, c=color, marker=marker, s=size, alpha=0.9, zorder=5, edgecolors='white', linewidths=0.5)
        ax.annotate(company, (x, y), xytext=(5, 5), textcoords='offset points',
                   fontsize=9, color=dark_gray)

# Add quadrant labels with high contrast
quadrant_style = dict(fontsize=11, fontweight='bold', color=army_dark, 
                      bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=army_dark, alpha=0.95))

ax.text(5, 9.2, 'Agentic Infrastructure\nIntelligence', ha='center', va='top', **quadrant_style)
ax.text(-5, 9.2, 'Horizontal AI\nPlatforms', ha='center', va='top', **quadrant_style)
ax.text(-5, -9.2, 'Generic Cloud\nServices', ha='center', va='bottom', **quadrant_style)
ax.text(5, -9.2, 'Legacy GIS &\nInfrastructure Tools', ha='center', va='bottom', **quadrant_style)

# Add axis labels
ax.set_xlabel('Domain Specificity', fontsize=14, fontweight='bold', labelpad=15, color=army_dark)
ax.set_ylabel('AI Sophistication', fontsize=14, fontweight='bold', labelpad=15, color=army_dark)

# Add axis endpoint labels
ax.text(-9.5, 0, 'Generic', fontsize=10, ha='left', va='center', style='italic', color=army_medium)
ax.text(9.5, 0, 'Infrastructure-\nSpecific', fontsize=10, ha='right', va='center', style='italic', color=army_medium)
ax.text(0, -9.5, 'Traditional/\nRule-Based', fontsize=10, ha='center', va='bottom', style='italic', color=army_medium)
ax.text(0, 9.5, 'Agentic AI', fontsize=10, ha='center', va='top', style='italic', color=army_medium)

# Add title
ax.set_title('Competitive Landscape: Geospatial AI Market Positioning', 
             fontsize=16, fontweight='bold', pad=20, color=army_dark)

# Create legend with distinct markers (B&W friendly with army green colors)
legend_elements = [
    plt.Line2D([0], [0], marker='*', color='w', markerfacecolor=army_dark, markersize=15, 
               markeredgecolor='white', markeredgewidth=1, label='AtlasPro AI (Target Position)'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=army_medium, markersize=10, 
               label='Horizontal AI Platforms'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=army_light, markersize=10, 
               label='Cloud Providers'),
    plt.Line2D([0], [0], marker='^', color='w', markerfacecolor=army_pale, markersize=10, 
               label='Legacy GIS/Infrastructure'),
    plt.Line2D([0], [0], marker='D', color='w', markerfacecolor=army_medium, markersize=10, 
               label='Emerging GNN Players'),
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=9, framealpha=0.95)

# Remove tick labels but keep grid
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.tick_params(axis='both', which='both', length=0)

# Add subtle background shading for quadrants (army green palette)
ax.fill_between([0, 10], [0, 0], [10, 10], alpha=0.15, color=army_dark)  # Top right - target (darkest)
ax.fill_between([-10, 0], [0, 0], [10, 10], alpha=0.08, color=army_medium)  # Top left
ax.fill_between([-10, 0], [-10, -10], [0, 0], alpha=0.05, color=army_light)  # Bottom left
ax.fill_between([0, 10], [-10, -10], [0, 0], alpha=0.08, color=army_pale)  # Bottom right

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/competitive_quadrant.pdf', 
            format='pdf', dpi=300, bbox_inches='tight')
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/competitive_quadrant.png', 
            format='png', dpi=300, bbox_inches='tight')

print("Competitive quadrant diagram saved successfully!")
