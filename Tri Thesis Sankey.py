import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Use a standard figure initialization
fig, ax = plt.subplots(figsize=(18, 10), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_axis_off()

# Color scheme
color_liquidity = '#4A7BA7'
color_alpha = '#5C8B9E'
color_defensive = '#7CB342'
color_exit_liquidity = '#1A3A52'
color_exit_alpha = '#2D5A6B'
color_exit_defensive = '#558B2F'

# ============================================================================
# TITLE
# ============================================================================
ax.text(5, 9.6, 'TRI-THESIS BEIJING FUND: CAPITAL DEPLOYMENT TIMELINE & RETURN GENERATION', 
        ha='center', fontsize=16, fontweight='bold')

# ============================================================================
# LEFT BOX: INITIAL INVESTMENT
# ============================================================================
left_box = FancyBboxPatch((0.2, 3.5), 0.8, 3.0, boxstyle="round,pad=0.1",
                          edgecolor='black', facecolor='#1a1a1a', linewidth=2)
ax.add_patch(left_box)
ax.text(0.6, 5.5, 'TOTAL', ha='center', fontsize=11, fontweight='bold', color='white')
ax.text(0.6, 5.0, '¥100M', ha='center', fontsize=14, fontweight='bold', color='white')
ax.text(0.6, 4.5, '(¥100,000,000)', ha='center', fontsize=9, color='white', style='italic')

# ============================================================================
# FLOW BANDS (Rendered behind boxes)
# ============================================================================
# Liquidity flow
liq_flow = plt.Polygon([(1.0, 5.2), (1.8, 6.5), (4.8, 6.2), (7.6, 6.5), (9.0, 6.5),
                        (9.0, 6.3), (7.6, 6.3), (4.8, 6.0), (1.8, 6.3), (1.0, 5.0)],
                       alpha=0.15, facecolor=color_liquidity, edgecolor='none')
ax.add_patch(liq_flow)

# Alpha flow
alpha_flow = plt.Polygon([(1.0, 5.0), (1.8, 5.0), (4.8, 4.8), (7.6, 5.0), (9.0, 5.0),
                          (9.0, 4.8), (7.6, 4.8), (4.8, 4.6), (1.8, 4.8), (1.0, 4.8)],
                         alpha=0.15, facecolor=color_alpha, edgecolor='none')
ax.add_patch(alpha_flow)

# Defensive flow
def_flow = plt.Polygon([(1.0, 4.8), (1.8, 3.5), (4.8, 3.3), (7.6, 3.4), (9.0, 3.4),
                        (9.0, 3.2), (7.6, 3.2), (4.8, 3.1), (1.8, 3.3), (1.0, 4.6)],
                       alpha=0.15, facecolor=color_defensive, edgecolor='none')
ax.add_patch(def_flow)

# ============================================================================
# PHASE HEADERS
# ============================================================================
for x_pos, label in [(2.3, 'YEAR 1-2'), (5.3, 'YEAR 3-5'), (8.1, 'YEAR 6-10')]:
    ax.text(x_pos, 8.8, label, ha='center', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='#2a2a2a', edgecolor='black', linewidth=1, pad=0.5),
            color='white')

# ============================================================================
# BOXES (Liquidity, Alpha, Defensive) - Positioning updated for alignment
# ============================================================================

# Y1-2
ax.add_patch(FancyBboxPatch((1.8, 5.9), 1.0, 1.2, boxstyle="round,pad=0.05", facecolor=color_liquidity, alpha=0.8))
ax.text(2.3, 6.5, 'LIQUIDITY\nENGINE\n(¥25M)', ha='center', va='center', fontsize=9, fontweight='bold', color='white')

ax.add_patch(FancyBboxPatch((1.8, 4.6), 1.0, 0.8, boxstyle="round,pad=0.05", facecolor=color_alpha, alpha=0.8))
ax.text(2.3, 5.0, 'STRUCTURAL\nALPHA\n(¥15M)', ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')

ax.add_patch(FancyBboxPatch((1.8, 3.2), 1.0, 0.6, boxstyle="round,pad=0.05", facecolor=color_defensive, alpha=0.8))
ax.text(2.3, 3.5, 'DEFENSIVE\nVALUE\n(¥10M)', ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')

# Y6-10 EXITS
ax.add_patch(FancyBboxPatch((7.6, 5.8), 1.0, 1.4, boxstyle="round,pad=0.05", facecolor=color_exit_liquidity))
ax.text(8.1, 6.5, 'LIQUIDITY\nENGINE EXIT\n(¥120M)', ha='center', va='center', fontsize=9, fontweight='bold', color='white')

ax.add_patch(FancyBboxPatch((7.6, 4.4), 1.0, 1.2, boxstyle="round,pad=0.05", facecolor=color_exit_alpha))
ax.text(8.1, 5.0, 'STRUCTURAL\nALPHA EXIT\n(¥100M)', ha='center', va='center', fontsize=9, fontweight='bold', color='white')

ax.add_patch(FancyBboxPatch((7.6, 3.2), 1.0, 0.4, boxstyle="round,pad=0.05", facecolor=color_exit_defensive))
ax.text(8.1, 3.4, 'DEFENSIVE\nVALUE EXIT\n(¥30M)', ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')

# ============================================================================
# TOTAL RETURN SUMMARY
# ============================================================================
right_box = FancyBboxPatch((9.0, 3.5), 0.9, 3.0, boxstyle="round,pad=0.1",
                            edgecolor='#FFD700', facecolor='#1a1a1a', linewidth=3)
ax.add_patch(right_box)
ax.text(9.45, 5.8, '2.5x return', ha='center', fontsize=12, fontweight='bold', color='#FFD700')
ax.text(9.45, 5.0, 'TOTAL EXIT\nVALUE:', ha='center', fontsize=9, color='white')
ax.text(9.45, 4.2, '¥250M+', ha='center', fontsize=12, fontweight='bold', color='#FFD700')

# ============================================================================
# BOTTOM INFO BOX
# ============================================================================
info_box = FancyBboxPatch((0.3, 0.2), 9.4, 1.2, boxstyle="round,pad=0.1", facecolor='#f8f9fa', edgecolor='#dee2e6')
ax.add_patch(info_box)
info_text = ("SUMMARIZED PORTFOLIO STRATEGY: Liquidity Engine holdings exit systematically 25-30%/year. "
             "Structural Alpha held through infrastructure maturation for bulk exit post-2026. "
             "Defensive Value maintained for selective allocation and long-term yield (3.5-4%).")
ax.text(5.0, 0.8, info_text, ha='center', va='center', fontsize=9, style='italic', wrap=True)

plt.savefig('tri_thesis_capital_deployment.png', dpi=300, bbox_inches='tight')
plt.show()