import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Set up the figure with a professional style
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(12, 10))

# Define the quadrant boundaries
ax.axhline(y=0, color='#333333', linewidth=1.5, linestyle='-')
ax.axvline(x=0, color='#333333', linewidth=1.5, linestyle='-')

# Set axis limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Define companies with their positions
# X-axis: Domain Specificity (Generic -> Infrastructure-Specific)
# Y-axis: AI Sophistication (Traditional/Rule-Based -> Agentic AI)

companies = {
    # Quadrant 1: High AI, High Domain Specificity (Top Right) - AtlasPro AI's target
    'AtlasPro AI': (7.5, 8.5, '#003366', '*', 400),
    
    # Quadrant 2: High AI, Low Domain Specificity (Top Left) - Horizontal AI platforms
    'OpenAI': (-7, 7.5, '#74AA9C', 'o', 200),
    'Anthropic': (-6, 6.5, '#D4A574', 'o', 180),
    'Google DeepMind': (-5, 8, '#4285F4', 'o', 220),
    'World Labs': (-3, 7, '#9B59B6', 'o', 150),
    
    # Quadrant 3: Low AI, Low Domain Specificity (Bottom Left) - Generic tools
    'AWS': (-6, -3, '#FF9900', 's', 180),
    'Microsoft Azure': (-5, -2, '#00A4EF', 's', 180),
    'Google Cloud': (-4, -4, '#34A853', 's', 180),
    
    # Quadrant 4: Low AI, High Domain Specificity (Bottom Right) - Legacy GIS/Infrastructure
    'Esri': (6, -5, '#2E7D32', '^', 200),
    'Hexagon': (5, -6, '#1565C0', '^', 180),
    'CARTO': (3, -3, '#E91E63', '^', 150),
    'Mapbox': (2, -2, '#000000', '^', 150),
    'IQGeo': (7, -4, '#795548', '^', 140),
    'Planet': (4, -1, '#3F51B5', '^', 140),
    'LiveEO': (5, -2, '#009688', '^', 130),
    
    # Emerging players in between
    'Ericsson (GNN)': (4, 3, '#0082C9', 'D', 120),
    'Academic Research': (3, 4, '#607D8B', 'D', 100),
}

# Plot each company
for company, (x, y, color, marker, size) in companies.items():
    if company == 'AtlasPro AI':
        ax.scatter(x, y, c=color, marker=marker, s=size, edgecolors='gold', linewidths=3, zorder=10)
        ax.annotate(company, (x, y), xytext=(10, 10), textcoords='offset points',
                   fontsize=12, fontweight='bold', color=color,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=color, alpha=0.9))
    else:
        ax.scatter(x, y, c=color, marker=marker, s=size, alpha=0.8, zorder=5)
        ax.annotate(company, (x, y), xytext=(5, 5), textcoords='offset points',
                   fontsize=9, color='#333333')

# Add quadrant labels
quadrant_style = dict(fontsize=11, fontweight='bold', color='#555555', 
                      bbox=dict(boxstyle='round,pad=0.4', facecolor='#f0f0f0', edgecolor='#cccccc', alpha=0.9))

ax.text(5, 9.2, 'Agentic Infrastructure\nIntelligence', ha='center', va='top', **quadrant_style)
ax.text(-5, 9.2, 'Horizontal AI\nPlatforms', ha='center', va='top', **quadrant_style)
ax.text(-5, -9.2, 'Generic Cloud\nServices', ha='center', va='bottom', **quadrant_style)
ax.text(5, -9.2, 'Legacy GIS &\nInfrastructure Tools', ha='center', va='bottom', **quadrant_style)

# Add axis labels
ax.set_xlabel('Domain Specificity', fontsize=14, fontweight='bold', labelpad=15)
ax.set_ylabel('AI Sophistication', fontsize=14, fontweight='bold', labelpad=15)

# Add axis endpoint labels
ax.text(-9.5, 0, 'Generic', fontsize=10, ha='left', va='center', style='italic', color='#666666')
ax.text(9.5, 0, 'Infrastructure-\nSpecific', fontsize=10, ha='right', va='center', style='italic', color='#666666')
ax.text(0, -9.5, 'Traditional/\nRule-Based', fontsize=10, ha='center', va='bottom', style='italic', color='#666666')
ax.text(0, 9.5, 'Agentic AI', fontsize=10, ha='center', va='top', style='italic', color='#666666')

# Add title
ax.set_title('Competitive Landscape: Geospatial AI Market Positioning', 
             fontsize=16, fontweight='bold', pad=20, color='#003366')

# Create legend
legend_elements = [
    mpatches.Patch(facecolor='#003366', edgecolor='gold', linewidth=2, label='AtlasPro AI (Target Position)'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#74AA9C', markersize=10, label='Horizontal AI Platforms'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='#FF9900', markersize=10, label='Cloud Providers'),
    plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='#2E7D32', markersize=10, label='Legacy GIS/Infrastructure'),
    plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='#0082C9', markersize=10, label='Emerging GNN Players'),
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=9, framealpha=0.95)

# Remove tick labels but keep grid
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.tick_params(axis='both', which='both', length=0)

# Add subtle background shading for quadrants
ax.fill_between([0, 10], [0, 0], [10, 10], alpha=0.08, color='#003366')  # Top right - target
ax.fill_between([-10, 0], [0, 0], [10, 10], alpha=0.05, color='#74AA9C')  # Top left
ax.fill_between([-10, 0], [-10, -10], [0, 0], alpha=0.05, color='#FF9900')  # Bottom left
ax.fill_between([0, 10], [-10, -10], [0, 0], alpha=0.05, color='#2E7D32')  # Bottom right

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/competitive_quadrant.pdf', 
            format='pdf', dpi=300, bbox_inches='tight')
plt.savefig('/home/ubuntu/spatial-survey-new/technical-report/figures/competitive_quadrant.png', 
            format='png', dpi=300, bbox_inches='tight')

print("Competitive quadrant diagram saved successfully!")
