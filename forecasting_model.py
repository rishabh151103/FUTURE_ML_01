import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from prophet import Prophet

# === Step 1: Load the dataset ===
file_path = Path("Data/superstore_sales.csv")
df = pd.read_csv(file_path, encoding='ISO-8859-1')
print("✅ Data loaded successfully.")
print(df.head())

# === Step 2: Convert 'Order Date' column to datetime ===
df['Order Date'] = pd.to_datetime(df['Order Date'])

# === Step 3: Group sales by month ===
monthly_sales = df.resample('M', on='Order Date')['Sales'].sum()
print("\n📊 Monthly Sales Summary:")
print(monthly_sales.head())

# === Create Images folder if not exists ===
Path("Images").mkdir(exist_ok=True)

# === Step 4: Plot monthly sales trend ===
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linestyle='-')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig("Images/monthly_sales_trend.png")
plt.show()

# === Step 5: Prepare data for Prophet ===
prophet_df = monthly_sales.reset_index()
prophet_df.columns = ['ds', 'y']
print("\n📄 Prophet-ready data:")
print(prophet_df.head())

# === Step 6: Train the Prophet model ===
model = Prophet()
model.fit(prophet_df)

# === Step 7: Create future dates (next 6 months) ===
future = model.make_future_dataframe(periods=6, freq='M')
print("\n📅 Future months to forecast:")
print(future.tail())

# === Step 8: Make predictions ===
forecast = model.predict(future)

# === Step 9: Plot forecast ===
fig1 = model.plot(forecast)
plt.title('Sales Forecast for Next 6 Months')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.tight_layout()
fig1.savefig("Images/forecast_plot.png")

# === Step 10: Plot trend and seasonality ===
fig2 = model.plot_components(forecast)
fig2.savefig("Images/forecast_trend_seasonality.png")

print("✅ Forecast plots saved.")

# === Step 11: Extra Visualizations (Dashboard Style) ===

# 11A: Sales by Category (horizontal bar chart)
plt.figure(figsize=(8, 5))
category_sales = df.groupby('Category')['Sales'].sum().sort_values()
sns.barplot(x=category_sales.values, y=category_sales.index, palette='viridis')
plt.title('💼 Sales by Category', fontsize=14)
plt.xlabel('Total Sales')
plt.tight_layout()
plt.savefig('Images/sales_by_category.png')
plt.show()

# 11B: Sales by Segment (pie chart)
plt.figure(figsize=(6, 6))
segment_sales = df.groupby('Segment')['Sales'].sum()
colors = sns.color_palette('pastel')[0:5]
plt.pie(segment_sales, labels=segment_sales.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('👥 Sales by Segment')
plt.ylabel('')
plt.tight_layout()
plt.savefig('Images/sales_by_segment.png')
plt.show()

# 11C: Top 10 States by Sales (bar chart)
plt.figure(figsize=(10, 6))
state_sales = df.groupby('State')['Sales'].sum().nlargest(10)
sns.barplot(x=state_sales.values, y=state_sales.index, palette='crest')
plt.title('📍 Top 10 States by Sales', fontsize=14)
plt.xlabel('Total Sales')
plt.tight_layout()
plt.savefig('Images/top_10_states.png')
plt.show()

print("✅ All visualizations completed and saved.")

