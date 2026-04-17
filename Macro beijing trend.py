import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD AND PREPARE DATA
# ---------------------------------------------------------
# Ensure file path is correct for your local machine
file_path = r'C:\Users\rohan\OneDrive\Desktop\NUS Y1S2\BT2102\Assignment 3\cleaned_beijing_housing.xlsx'
df = pd.read_excel(file_path)

# District Mapping
district_mapping = {
    1: "Dongcheng District", 2: "Fengtai District", 3: "Tongzhou District", 
    4: "Daxing District", 5: "Fangshan District", 6: "Changping District", 
    7: "Chaoyang District", 8: "Haidian District", 9: "Shijingshan District", 
    10: "Xicheng District", 11: "Pinggu District", 12: "Mentougou District", 
    13: "Shunyi District"
}
df['district_name'] = df['district'].map(district_mapping)

# Calculate Weighted Ensemble Prediction
df['pred_ensemble'] = (df['pred_rf'] * 0.53) + (df['pred_lr'] * 0.47)

# Define Pareto Order
pareto_order = ["Chaoyang District", "Changping District", "Fengtai District", 
                "Haidian District", "Daxing District", "Pinggu District"]

pareto_colors = {
    "Chaoyang District": "#E15759", "Changping District": "#F17B79", 
    "Fengtai District": "#F9A655", "Haidian District": "#F1CE63", 
    "Daxing District": "#D4E157", "Pinggu District": "#72B966"
}

# 2. PLOT CONFIGURATION
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 10), dpi=300)
sns.set_style("whitegrid", {'axes.grid': True, 'grid.color': '.95'})

# Layer 1: Others (Light grey)
others_df = df[~df['district_name'].isin(pareto_order)]
ax.scatter(others_df['pred_ensemble'], others_df['price'], 
            color='#C0C0C0', alpha=0.12, s=25, label='Other Districts', 
            zorder=1, edgecolor='none')

# Layer 2: Pareto Districts
for district in pareto_order:
    district_data = df[df['district_name'] == district]
    ax.scatter(district_data['pred_ensemble'], district_data['price'],
               color=pareto_colors[district], alpha=0.65, s=60, 
               label=district, zorder=2, edgecolor='white', linewidth=0.3)

# 3. REFERENCE LINES AND ZONE SHADING
# ---------------------------------------------------------
max_vis = df['price'].quantile(0.995)
min_vis = 0

# Fair Value Line (y = x)
ax.plot([min_vis, max_vis], [min_vis, max_vis], color='black', lw=2.2, 
        label='Fair Value Line', zorder=3)

# -10% Undervaluation Line (y = 0.9x) 
# FIXED: The previous logic used a fixed horizontal point; this creates a proper slope.
ax.plot([min_vis, max_vis], [min_vis, max_vis * 0.9], color='#1B5E20', 
        ls='--', lw=2.0, label='-10% Undervaluation Line', zorder=3)

# Shading the Green "Underpriced Zone" 
ax.fill_between([min_vis, max_vis], [min_vis, max_vis * 0.9], [min_vis, min_vis], 
                 color='#C8E6C9', alpha=0.25, zorder=0, 
                 label='Underpriced Zone (Buy Signal)')

# Annotation
ax.text(max_vis * 0.55, max_vis * 0.3, 'VALUE ZONE\n(Properties selling below fair value)', 
        fontsize=11, fontweight='bold', color='#1B5E20', alpha=0.7,
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#C8E6C9', alpha=0.4, edgecolor='#1B5E20', linewidth=2),
        ha='center', va='center', zorder=2)

# 4. FORMATTING
# ---------------------------------------------------------
ax.set_title("Beijing Housing Market: Weighted Ensemble Model\nActual Price vs. Predicted Fair Value", 
             fontsize=14, fontweight='bold', pad=25)
ax.set_xlabel("Predicted Fair Value (Weighted Ensemble)", fontsize=11, fontweight='bold')
ax.set_ylabel("Actual Market Price", fontsize=11, fontweight='bold')

ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'¥{int(x/1000)}k'))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'¥{int(x/1000)}k'))

# 5. LEGEND POSITIONING (Fixed Slicing)
# ---------------------------------------------------------
plt.tight_layout()
fig.subplots_adjust(right=0.80)

handles, labels = ax.get_legend_handles_labels()
# Legend 1: Scatter plots (Indices 0 to 6: Others + 6 Pareto Districts)
legend1 = ax.legend(handles[:7], labels[:7], bbox_to_anchor=(1.02, 1), 
                    loc='upper left', fontsize=9.5, title="Priority Districts", 
                    title_fontsize=10, frameon=True, fancybox=True, shadow=True)
ax.add_artist(legend1)

# Legend 2: Lines/Zones (Indices 7 to 9: Fair Value, -10% Line, Zone Shading)
legend2 = ax.legend(handles[7:], labels[7:], bbox_to_anchor=(1.02, 0.55), 
                    loc='upper left', fontsize=9.5, title="Valuation Reference", 
                    title_fontsize=10, frameon=True, fancybox=True, shadow=True)

# 7. ZOOM OUT / EXPAND VIEW
# ---------------------------------------------------------
# Increase figure size further
fig.set_size_inches(16, 12)

# Reduce font sizes slightly to fit better
ax.set_title("Beijing Housing Market: Weighted Ensemble Model\nActual Price vs. Predicted Fair Value", 
             fontsize=12, fontweight='bold', pad=25)
ax.set_xlabel("Predicted Fair Value (Weighted Ensemble)", fontsize=10, fontweight='bold')
ax.set_ylabel("Actual Market Price", fontsize=10, fontweight='bold')

# Adjust legend font sizes
for legend in [legend1, legend2]:
    for text in legend.get_texts():
        text.set_fontsize(8.5)
    legend.get_title().set_fontsize(9)

# Increase margins
fig.subplots_adjust(right=0.78, left=0.08, top=0.95, bottom=0.08)

plt.savefig('beijing_ensemble_mispricing_enhanced.png', dpi=300, bbox_inches='tight')
plt.show()