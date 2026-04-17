import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np



# 1. EXACT DATA FROM YOUR TABLE

# ---------------------------------------------------------

data = {

    'District': ['Daixing', 'Fengtai', 'Pinggu', 'Chaoyang', 'Changping', 'Haidian'],

    'Number of Listings': [15313, 29338, 13974, 107244, 38634, 38200],

    'Percentage Overpriced': [25.77, 23.02, 23.49, 20.29, 28.34, 19.79],

    'Percentage Underpriced': [23.96, 27.15, 18.38, 27.18, 19.43, 25.76],

    'Percentage Under 10% Alpha': [7.69, 7.05, 6.13, 5.94, 5.34, 4.95]

}



df = pd.DataFrame(data)



# 2. CREATE FIGURE WITH MULTIPLE SUBPLOTS (One per metric)

# ---------------------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(16, 10), dpi=300, 

                          gridspec_kw={'hspace': 0.4, 'wspace': 0.3})

fig.suptitle('Beijing Housing Market: District-Level Mispricing Analysis', 

             fontsize=16, fontweight='bold', y=0.98)



# Flatten axes for easier iteration

axes = axes.flatten()



# 2A. TABLE 1: NUMBER OF LISTINGS (Neutral grey)

# ---------------------------------------------------------

ax1 = axes[0]

ax1.axis('tight')

ax1.axis('off')



listings_data = df[['District', 'Number of Listings']].copy()

listings_data['Number of Listings'] = listings_data['Number of Listings'].astype(str)



table1 = ax1.table(cellText=listings_data.values, 

                   colLabels=listings_data.columns,

                   cellLoc='center', loc='center',

                   colWidths=[0.4, 0.6])

table1.auto_set_font_size(False)

table1.set_fontsize(11)

table1.scale(1, 2.5)



# Header styling

for i in range(len(listings_data.columns)):

    table1[(0, i)].set_facecolor('#404040')

    table1[(0, i)].set_text_props(weight='bold', color='white', fontsize=12)



# Row styling (light grey)

for i in range(1, len(listings_data) + 1):

    for j in range(len(listings_data.columns)):

        table1[(i, j)].set_facecolor('#F5F5F5')

        table1[(i, j)].set_text_props(weight='bold')



ax1.set_title('Number of Listings', fontsize=12, fontweight='bold', pad=15)



# 2B. TABLE 2: PERCENTAGE OVERPRICED (Red gradient)

# ---------------------------------------------------------

ax2 = axes[1]

ax2.axis('tight')

ax2.axis('off')



overpriced_data = df[['District', 'Percentage Overpriced']].copy()

overpriced_data['Percentage Overpriced'] = overpriced_data['Percentage Overpriced'].apply(lambda x: f'{x:.2f}%')



table2 = ax2.table(cellText=overpriced_data.values, 

                   colLabels=overpriced_data.columns,

                   cellLoc='center', loc='center',

                   colWidths=[0.4, 0.6])

table2.auto_set_font_size(False)

table2.set_fontsize(11)

table2.scale(1, 2.5)



# Header styling

for i in range(len(overpriced_data.columns)):

    table2[(0, i)].set_facecolor('#404040')

    table2[(0, i)].set_text_props(weight='bold', color='white', fontsize=12)



# Apply RED gradient to overpriced column

overpriced_vals = df['Percentage Overpriced'].values

norm_overpriced = (overpriced_vals - overpriced_vals.min()) / (overpriced_vals.max() - overpriced_vals.min())



for i in range(1, len(overpriced_data) + 1):

    # District column (grey)

    table2[(i, 0)].set_facecolor('#F5F5F5')

    table2[(i, 0)].set_text_props(weight='bold')

    

    # Percentage column (red gradient)

    intensity = norm_overpriced[i - 1]

    red = int(255)

    green = int(200 * (1 - intensity))

    blue = int(200 * (1 - intensity))

    color = f'#{red:02x}{green:02x}{blue:02x}'

    table2[(i, 1)].set_facecolor(color)

    table2[(i, 1)].set_text_props(weight='bold', color='white' if intensity > 0.5 else 'black')



ax2.set_title('Percentage Overpriced', fontsize=12, fontweight='bold', pad=15, color='#E15759')



# 2C. TABLE 3: PERCENTAGE UNDERPRICED (Green gradient)

# ---------------------------------------------------------

ax3 = axes[2]

ax3.axis('tight')

ax3.axis('off')



underpriced_data = df[['District', 'Percentage Underpriced']].copy()

underpriced_data['Percentage Underpriced'] = underpriced_data['Percentage Underpriced'].apply(lambda x: f'{x:.2f}%')



table3 = ax3.table(cellText=underpriced_data.values, 

                   colLabels=underpriced_data.columns,

                   cellLoc='center', loc='center',

                   colWidths=[0.4, 0.6])

table3.auto_set_font_size(False)

table3.set_fontsize(11)

table3.scale(1, 2.5)



# Header styling

for i in range(len(underpriced_data.columns)):

    table3[(0, i)].set_facecolor('#404040')

    table3[(0, i)].set_text_props(weight='bold', color='white', fontsize=12)



# Apply GREEN gradient to underpriced column

underpriced_vals = df['Percentage Underpriced'].values

norm_underpriced = (underpriced_vals - underpriced_vals.min()) / (underpriced_vals.max() - underpriced_vals.min())



for i in range(1, len(underpriced_data) + 1):

    # District column (grey)

    table3[(i, 0)].set_facecolor('#F5F5F5')

    table3[(i, 0)].set_text_props(weight='bold')

    

    # Percentage column (green gradient)

    intensity = norm_underpriced[i - 1]

    red = int(150 * (1 - intensity))

    green = int(200)

    blue = int(150 * (1 - intensity))

    color = f'#{red:02x}{green:02x}{blue:02x}'

    table3[(i, 1)].set_facecolor(color)

    table3[(i, 1)].set_text_props(weight='bold', color='white' if intensity > 0.5 else 'black')



ax3.set_title('Percentage Underpriced (Value Opportunity)', fontsize=12, fontweight='bold', pad=15, color='#1B5E20')



# 2D. TABLE 4: PERCENTAGE UNDER 10% ALPHA (Teal gradient)

# ---------------------------------------------------------

ax4 = axes[3]

ax4.axis('tight')

ax4.axis('off')



alpha_data = df[['District', 'Percentage Under 10% Alpha']].copy()

alpha_data['Percentage Under 10% Alpha'] = alpha_data['Percentage Under 10% Alpha'].apply(lambda x: f'{x:.2f}%')



table4 = ax4.table(cellText=alpha_data.values, 

                   colLabels=alpha_data.columns,

                   cellLoc='center', loc='center',

                   colWidths=[0.4, 0.6])

table4.auto_set_font_size(False)

table4.set_fontsize(11)

table4.scale(1, 2.5)



# Header styling

for i in range(len(alpha_data.columns)):

    table4[(0, i)].set_facecolor('#404040')

    table4[(0, i)].set_text_props(weight='bold', color='white', fontsize=12)



# Apply TEAL gradient to alpha column

alpha_vals = df['Percentage Under 10% Alpha'].values

norm_alpha = (alpha_vals - alpha_vals.min()) / (alpha_vals.max() - alpha_vals.min())



for i in range(1, len(alpha_data) + 1):

    # District column (grey)

    table4[(i, 0)].set_facecolor('#F5F5F5')

    table4[(i, 0)].set_text_props(weight='bold')

    

    # Percentage column (teal gradient)

    intensity = norm_alpha[i - 1]

    red = int(100 * (1 - intensity))

    green = int(180)

    blue = int(200)

    color = f'#{red:02x}{green:02x}{blue:02x}'

    table4[(i, 1)].set_facecolor(color)

    table4[(i, 1)].set_text_props(weight='bold', color='white' if intensity > 0.5 else 'black')



ax4.set_title('Percentage Under 10% Alpha (Structural Mispricing)', fontsize=12, fontweight='bold', pad=15, color='#1976D2')



# 3. ADD EXPLANATORY NOTE

# ---------------------------------------------------------

fig.text(0.5, 0.02, 

         'Darker shades indicate higher concentration of the metric. Green = More underpriced units (value opportunity). Red = More overpriced units. Teal = Higher structural alpha (systematic mispricing).',

         ha='center', fontsize=10, style='italic', color='#333333',

         bbox=dict(boxstyle='round', facecolor='#F0F0F0', alpha=0.8, pad=1))



# 4. SAVE AND DISPLAY

# ---------------------------------------------------------

plt.savefig('beijing_district_mispricing_heatmap.png', dpi=300, bbox_inches='tight', facecolor='white')

print("✓ District mispricing heatmap table saved: beijing_district_mispricing_heatmap.png")

plt.show()