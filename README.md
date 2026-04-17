# Beijing Housing Investment Analysis

A data-driven investment strategy for Beijing's residential property market, built on 12,500+ property listings from Lianjia.com (2016–2018). This project combines exploratory data analysis, machine learning, and business storytelling into a 10-minute presentation.

---

## Project Overview

**Central question:** *Where should I invest in Beijing's housing market?*

We answer this through five analytical chapters:

1. **Market Overview & Diagnosis** — Geographic distribution, price distributions, district-level diagnostics
2. **Value Analysis & Identification** — Value scoring methodology, Pareto ranking, geographic heat mapping, bargain concentration
3. **Market Validation** — Days on market, buyer interest signals, price momentum (2016–2018)
4. **Advanced Analytics** — Random Forest mispricing detection, investment opportunity matrix
5. **Recommendations** — Three-tier investment framework with actionable theses

**Key finding:** Tongzhou and Changping offer the strongest combination of current undervaluation and future appreciation potential. Central districts (Chaoyang, Haidian) are overpriced relative to fundamentals.

---

## Repository Structure

```
├── presentation/
│   └── slides.pptx / slides.pdf       #slide presentation deck
│
├── charts/
│   ├── chapter1_market_overview/
│   │   ├── geographic_scatter.twbx     # Tableau: property location map
│   │   ├── price_distribution.py       # Histogram of total prices
│   │   └── properties_by_district.py   # Bar chart: listings per district
│   │
│   ├── chapter2_value_analysis/
│   │   ├── size_price_scatter.twbx     # Tableau: scatter + regression (A1)
│   │   ├── feature_importance.py       # Random Forest importance bar (A2)
│   │   ├── price_stability_boxplot.R   # ggplot2 box plots by district (A3)
│   │   ├── pareto_value_ranking.twbx   # Tableau: Pareto chart (B1) 
│   │   ├── geographic_heatmap.twbx     # Tableau: geo heat map (B2) 
│   │   └── bargain_distribution.py     # Pie + bar: cheap properties (B3)
│   │
│   ├── chapter3_market_validation/
│   │   ├── days_on_market.py           # Category variance + line chart (C1)
│   │   ├── bubble_chart_demand.twbx    # Tableau: followers vs. sales (C2)
│   │   └── price_trends_timeline.py    # Multi-line price momentum (C3)
│   │
│   └── chapter4_advanced_analytics/
│       ├── prediction_residuals.py     # RF mispricing scatter plot
│       └── investment_matrix.twbx      # Tableau: 2×2 quadrant matrix 
│
└── README.md
```

## Tools & Languages

| Tool | Usage |
|------|-------|
| Python (pandas, matplotlib, scikit-learn) | Data processing, histograms, bar charts, ML model |
| R (ggplot2) | Box plots |
| Tableau | Geographic maps, Pareto chart, bubble chart, investment matrix |

---

## Chart Index

| ID | Question | Chart Type 
|----|----------|------------
| A1 | Size–price relationship? | Scatter + regression 
| A2 | What drives price? | Feature importance bar 
| A3 | Price stability by district? | Box plot 
| B1 | Top value districts? | Pareto chart 
| B2 | Price premium/discount? | Geographic heat map 
| B3 | Where are bargains? | Pie + bar 
| C1 | Market velocity? | Category variance + line 
| C2 | Interest → sales? | Bubble chart 
| C3 | Market momentum? | Multi-line chart 
| — | Mispricing detection | Prediction residuals
| — | Investment recommendation | 2×2 quadrant matrix 

---

## Data

**Source:** Lianjia.com (链家)
**Period:** 2016–2018
**Size:** ~12,500 property listings
**Key fields:** `totalPrice`, `price` (per sqm), `square`, `district`, `tradeTime`, `DOM`, `followers`, `elevator`, `subway`, `renovationCondition`, `livingRoom`, `age`, `lng`, `lat`


