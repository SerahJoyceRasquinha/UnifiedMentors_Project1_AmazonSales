import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('DataSet/CSV_SortedOnBasisOf_Region,Country,TotRevenue(L-S),TotCost(L-S),TotProfit(L-S).csv')

# Convert 'Order Date' to datetime format
data['Order Date'] = pd.to_datetime(data['Order Date'])

# Extract month and year from 'Order Date'
data['Month'] = data['Order Date'].dt.month
data['Year'] = data['Order Date'].dt.year

# 1) Bar graph for month-wise analysis of units sold
print("\n\n")
print("This graph shows the relationship between Units Sold on a Monthly-Wise Count")
print("\n")
monthly_units_sold = data.groupby('Month')['Units Sold'].sum()
plt.figure(figsize=(10, 6))
monthly_units_sold.plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.title('Month-wise Analysis of Units Sold')
plt.xticks(rotation=45)
plt.show()

# 2) Bar graph for year-wise analysis of units sold
print("\n\n")
print("This graph shows the relationship between Units Sold on a Yearly-Wise Count")
print("\n")
yearly_units_sold = data.groupby('Year')['Units Sold'].sum()
plt.figure(figsize=(10, 6))
yearly_units_sold.plot(kind='bar')
plt.xlabel('Year')
plt.ylabel('Units Sold')
plt.title('Year-wise Analysis of Units Sold')
plt.xticks(rotation=45)
plt.show()

# 3) Line and clustered column chart for month-wise analysis of units sold and profit
print("\n\n")
print("This graph shows the relationship between Units Sold on a Monthly-Wise Count and the Total Profits Earned off of it")
print("\n")
monthly_units_profit = data.groupby('Month')[['Units Sold', 'Total Profit']].sum()
plt.figure(figsize=(10, 6))
ax = monthly_units_profit['Units Sold'].plot(kind='bar', color='blue')
ax2 = ax.twinx()
monthly_units_profit['Total Profit'].plot(kind='line', marker='o', color='red', ax=ax2)
ax.set_ylabel('Units Sold', color='blue')
ax2.set_ylabel('Total Profit', color='red')
plt.title('Month-wise Analysis of Units Sold and Profit')
plt.xticks(rotation=45)
plt.show()

# 4) Line and clustered column chart for year-wise analysis of units sold and profit
print("\n\n")
print("This graph shows the relationship between Units Sold on a Yearly-Wise Count and the Total Profits Earned off of it")
print("\n")
yearly_units_sold = data.groupby('Year')['Units Sold'].sum()
yearly_profit = data.groupby('Year')['Total Profit'].sum()

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('Units Sold', color=color)
ax1.bar(yearly_units_sold.index, yearly_units_sold, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Total Profit', color=color)
ax2.plot(yearly_profit.index, yearly_profit, color=color, marker='o', linestyle='-', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Year-wise Analysis of Units Sold with Profit')
plt.xticks(rotation=45)
plt.show()

# 5) Pie chart showing the relationship between Total Profit and Item Type
print("\n\n")
print("This graph shows the relationship between the Total Profits earned off of Each Item type Sold")
print("\n")
profit_by_item_type = data.groupby('Item Type')['Total Profit'].sum()
plt.figure(figsize=(10, 6))
plt.pie(profit_by_item_type, labels=profit_by_item_type.index, autopct='%1.1f%%')
plt.title('Total Profit by Item Type')
plt.show()

# 6) Clustered column chart for month-wise analysis of revenue, cost, and profit
print("\n\n")
print("This graph shows the relationship between the Total Revenue, Total Cost and Total Profit on a Monthly-Wise Count")
print("\n")
monthly_financials = data.groupby('Month')[['Total Revenue', 'Total Cost', 'Total Profit']].sum()
plt.figure(figsize=(10, 6))
monthly_financials.plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Monthly Financial Analysis')
plt.xticks(rotation=45)
plt.show()

# 7) Clustered column chart for year-wise analysis of revenue, cost, and profit
print("\n\n")
print("This graph shows the relationship between the Total Revenue, Total Cost and Total Profit on a Yearly-Wise Count")
print("\n")
yearly_financials = data.groupby('Year')[['Total Revenue', 'Total Cost', 'Total Profit']].sum()
plt.figure(figsize=(10, 6))
yearly_financials.plot(kind='bar')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Yearly Financial Analysis')
plt.xticks(rotation=45)
plt.show()
