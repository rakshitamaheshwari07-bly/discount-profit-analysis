# 📊 Discount vs Profit Insight Report

A data analytics mini-project analyzing how discounting strategy impacts profitability across the Superstore retail dataset, with a linear regression model to quantify the relationship.

## 🎯 Objective
Retailers often use discounts to drive sales, but excessive discounting can silently erode profit margins. This project investigates the Superstore dataset (9,994 transactions) to answer:
**Does higher discounting actually hurt profitability, and where does it hurt most?**

## 📁 Dataset
Superstore Sales Dataset — 9,994 rows, 21 columns including Sales, Quantity, Discount, Profit, Category, Region, and Sub-Category.

## 🔍 Key Findings
| Insight | Detail |
|---|---|
| Discount → Profit | Negative relationship — regression coefficient: **-241.97** |
| Category | Furniture: highest avg. discount (17.4%), lowest avg. profit (₹8.7). Technology: lowest discount (13.2%), highest profit (₹78.75) |
| Region | Central: highest discount (24%), lowest profit (₹17). West: lowest discount (11%), highest profit (₹33.8) |
| Sub-Category losses | Tables (-₹55.5 avg) and Bookcases (-₹15.2 avg) run at a loss |
| Best performer | Copiers — ₹817.9 average profit |

## 📈 Regression Model Results
| Model | R² Score | RMSE |
|---|---|---|
| Discount → Profit | 0.064 | 213.06 |
| Discount + Quantity → Profit | 0.069 | 212.46 |

The low R² confirms discount alone doesn't explain all profit variation — category and region matter just as much, which is itself a useful finding for targeted (not blanket) discount policies.

## 💡 Business Recommendations
- Cap discounts on **Furniture, Tables, and Bookcases** (e.g. max 15%) to prevent losses
- Re-evaluate **Central region's** discount strategy — high discounting isn't paying off there
- Push high-margin categories like **Technology and Copiers** with minimal discounts instead of relying on blanket promotions

## 📊 Visualizations
- `discount_vs_profit.png` — Scatter plot of Discount vs Profit
- `category_profit.png` — Average profit by category
- `region_profit.png` — Average profit by region
- `subcategory_profit.png` — Average profit by sub-category
- `regression_line.png` — Regression fit line over the data

## 🛠️ Tools & Libraries
Python · pandas · matplotlib · seaborn · scikit-learn

## 📂 Files
- `discount_profit_analysis.py` — full analysis and modeling script
- `README.md` — this file
- PNG chart outputs

---
*Built as an extension of my Data Analytics internship at Thiranex, applying regression modeling to a real business question.*
