import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Updated Coefficients
coefficients = {
    'square': -434.8,
    'buildingType': -384.4,
    'floor_num': -69.36,
    'constructionTime': -72.05,
    'buildingStructure': -525,
    'fiveYearsProperty': -1610,
    'DOM': 16.93,
    'followers': 22.16,
    'drawingRoom': 284.1,
    'kitchen': 1470,
    'bathRoom': 1540,
    'renovationCondition': 1084,
    'elevator': 758.6,
    'subway': 229.7,
    'Lat': 3341,
    'Lng': -1451,
    'district': 17.20,
    'communityAverage': 0.2709
}

# 2. Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

features = ['square', 'buildingType', 'floor_num', 'constructionTime', 'buildingStructure', 
            'fiveYearsProperty', 'DOM', 'followers', 'drawingRoom']
coefs = [coefficients[f] for f in features]

# Red color for counterintuitive features
problematic = ['square', 'buildingType', 'floor_num']
colors = ['#d62728' if f in problematic else '#2ca02c' for f in features]

ax1.barh(features, coefs, color=colors, alpha=0.8, edgecolor='black')
ax1.axvline(x=0, color='black', linestyle='-', linewidth=1)
ax1.set_xlabel('Coefficient Value', fontsize=12, fontweight='bold')
ax1.set_title('Paradoxial Coefficients of Linear Regression', fontsize=14, fontweight='bold')
ax1.grid(axis='x', alpha=0.3)

# Improved number labels formatting
for i, f in enumerate(features):
    v = coefs[i]
    label = f' {v:,.1f} '
    
    # Handle the specific overlap cases
    if f == 'fiveYearsProperty':
        # Push this long negative bar's label to the right of the 0 line
        ax1.text(20, i, label, va='center', ha='left', fontweight='bold', fontsize=10, color='black')
    elif f == 'drawingRoom':
        # Shift drawingRoom label further right so it's clearly inside the bar/not on axis
        ax1.text(v - 20, i, label, va='center', ha='right', fontweight='bold', fontsize=10, color='black')
    elif f in ['DOM', 'followers']:
        # For very small positive bars, put label to the right of the bar
        ax1.text(v + 10, i, label, va='center', ha='left', fontweight='bold', fontsize=10)
    else:
        # Standard alignment based on sign
        ha = 'right' if v < 0 else 'left'
        ax1.text(v, i, label, va='center', ha=ha, fontweight='bold', fontsize=10)

# Plot 2: Paradox Table
ax2.axis('tight')
ax2.axis('off')
table_data = [
    ['Feature', 'Coeff', 'Expected', 'Actual', 'Result'],
    ['square', '-434.8', 'Positive', 'Negative', 'Paradox'],
    ['floor_num', '-69.3', 'Positive', 'Negative', 'Inverted'],
    ['renovation', '+1084', 'Positive', 'Positive', 'Expected']
]

table = ax2.table(cellText=table_data, cellLoc='center', loc='center', colWidths=[0.18, 0.15, 0.18, 0.18, 0.18])
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 3)

for j in range(5):
    table[(0, j)].set_facecolor('#404040')
    table[(0, j)].set_text_props(color='white', weight='bold')

plt.tight_layout()
plt.show()