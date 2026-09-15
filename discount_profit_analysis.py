import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

sns.set(style="whitegrid")

# ---- LOAD DATA ----
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')  # apna filename daalo
print(df.columns.tolist())
print(df.head())

# ---- BASIC CHECK ----
print(df[['Discount','Profit','Quantity']].describe())
print(df[['Discount','Profit']].isnull().sum())

# ---- SCATTER: Discount vs Profit ----
plt.figure(figsize=(8,5))
sns.scatterplot(x='Discount', y='Profit', data=df, alpha=0.5)
plt.title("Discount vs Profit")
plt.savefig("discount_vs_profit.png")
plt.close()

# ---- CATEGORY-WISE ----
category_profit = df.groupby('Category')[['Discount','Profit']].mean()
print(category_profit)

plt.figure(figsize=(8,5))
sns.barplot(x=category_profit.index, y=category_profit['Profit'])
plt.title("Average Profit by Category")
plt.savefig("category_profit.png")
plt.close()

# ---- REGION-WISE ----
region_profit = df.groupby('Region')[['Discount','Profit']].mean()
print(region_profit)

plt.figure(figsize=(8,5))
sns.barplot(x=region_profit.index, y=region_profit['Profit'])
plt.title("Average Profit by Region")
plt.savefig("region_profit.png")
plt.close()

# ---- SUB-CATEGORY LOSS CHECK (extra insight) ----
subcat_profit = df.groupby('Sub-Category')['Profit'].mean().sort_values()
print(subcat_profit)

plt.figure(figsize=(10,6))
sns.barplot(x=subcat_profit.values, y=subcat_profit.index)
plt.title("Average Profit by Sub-Category")
plt.savefig("subcategory_profit.png")
plt.close()

# ---- LINEAR REGRESSION: Discount -> Profit ----
X = df[['Discount']]
y = df['Profit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("=== Simple Regression (Discount -> Profit) ===")
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("R2 Score:", r2_score(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred) ** 0.5)

plt.figure(figsize=(8,5))
sns.scatterplot(x='Discount', y='Profit', data=df, alpha=0.3)
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.title("Linear Regression: Discount vs Profit")
plt.savefig("regression_line.png")
plt.close()

# ---- MULTI-FEATURE REGRESSION (Discount + Quantity -> Profit) ----
X_multi = df[['Discount','Quantity']]
y_multi = df['Profit']
Xm_train, Xm_test, ym_train, ym_test = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)

model2 = LinearRegression()
model2.fit(Xm_train, ym_train)
ym_pred = model2.predict(Xm_test)

print("=== Multi Regression (Discount+Quantity -> Profit) ===")
print("R2 Score:", r2_score(ym_test, ym_pred))
print("RMSE:", mean_squared_error(ym_test, ym_pred) ** 0.5)

print("\nDONE. Check folder for saved PNG charts.")