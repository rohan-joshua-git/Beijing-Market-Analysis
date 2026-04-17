import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Create the figure
fig, ax = plt.subplots(figsize=(14, 8)) # Slightly smaller figure ratio
ax.set_xlim(0, 10)
ax.set_ylim(1, 10) # Adjusted limits to center the content
ax.axis('off')

# Define professional palette
root_color = '#1976D2'  # Strong Blue (Parent)
child_color = '#90CAF9' # Light Blue (Decision)
leaf_color = '#BBDEFB'  # Soft Green (Prediction)

def draw_node(ax, x, y, text, color, width=2.0, height=0.9):
    """Draw a decision or leaf node with black text"""
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                          boxstyle="round,pad=0.1", 
                          edgecolor='black', facecolor=color, 
                          linewidth=1.5, alpha=0.9)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', 
            fontsize=9, fontweight='bold', color='black') # Forced black text

def draw_arrow(ax, x1, y1, x2, y2, label=''):
    """Draw arrow between nodes with black text label"""
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                            arrowstyle='->', mutation_scale=15, 
                            linewidth=2, color='#333333')
    ax.add_patch(arrow)
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x, mid_y + 0.2, label, fontsize=9, 
                fontweight='bold', style='italic', color='black', # Changed to black
                ha='center', bbox=dict(boxstyle='round,pad=0.1', facecolor='white', alpha=0.8, edgecolor='none'))

# --- 1. TITLE ---
ax.text(5, 9.5, 'Random Forest Decision Tree Visualisation', 
        ha='center', fontsize=16, fontweight='bold', color='black')

# --- 2. ROOT NODE ---
# Smaller width/height for a more compact fit
draw_node(ax, 5, 8.2, 
          'Community Average\n> ¥80k / sqm?', 
          root_color, width=2.2, height=1.0)

# --- 3. LEVEL 2 ---
# Left: Standard Market
draw_arrow(ax, 4.0, 7.8, 2.5, 6.8, 'NO (Suburban)')
draw_node(ax, 2.5, 6.0, 
          'Square Footage\n> 90 sqm?', 
          child_color, width=2.0, height=0.9)

# Right: Premium Market
draw_arrow(ax, 6.0, 7.8, 7.5, 6.8, 'YES (Core District)')
draw_node(ax, 7.5, 6.0, 
          'Building Type:\nLow-rise / Villa?', 
          child_color, width=2.0, height=0.9)

# --- 4. LEVEL 3 (Predictions) ---

# Predictions for Suburban Branch
draw_arrow(ax, 2.0, 5.6, 1.2, 4.8, 'Small')
draw_node(ax, 1.2, 4.2, 'Predict:\n¥2.2M', leaf_color, width=1.6, height=0.8)

draw_arrow(ax, 3.0, 5.6, 3.8, 4.8, 'Large')
draw_node(ax, 3.8, 4.2, 'Predict:\n¥4.5M', leaf_color, width=1.6, height=0.8)

# Predictions for Premium Branch
draw_arrow(ax, 7.0, 5.6, 6.2, 4.8, 'High-Rise')
draw_node(ax, 6.2, 4.2, 'Predict:\n¥8.2M', leaf_color, width=1.6, height=0.8)

draw_arrow(ax, 8.0, 5.6, 8.8, 4.8, 'Villa')
draw_node(ax, 8.8, 4.2, 'Predict:\n¥15.8M', leaf_color, width=1.6, height=0.8)

# --- 5. BOTTOM SUMMARY BOX ---
summary_box = (
    "Random Forest Diagnostics:\n"
    "• R² = 0.9696 (Explains ~97% of Variance)\n"
    "• Corrects 'Negative Square' Bias via Market Segmentation\n"
    "• Captures Non-Linear Cultural Premiums for Low-Rise Housing"
)

ax.text(5, 2.2, summary_box,
        ha='center', fontsize=11, fontweight='bold', color='black', linespacing=1.4,
        bbox=dict(boxstyle='round,pad=0.8', facecolor='#F5F5F5', alpha=1.0, edgecolor='#1976D2', linewidth=1.5))

plt.tight_layout()
plt.savefig('random_forest_compact_diagram.png', dpi=300, bbox_inches='tight')
print("✓ Compact Random Forest diagram saved.")
plt.show()