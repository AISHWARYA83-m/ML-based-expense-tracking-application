import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data\expenses.csv")

category_total = df.groupby("Category")["Amount"].sum()

# Pie Chart
category_total.plot(kind="pie", autopct='%1.1f%%')
plt.title("Expense Distribution")
plt.show()

# Bar Chart 
category_total.plot(kind="bar")
plt.title("Category-wise Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()

# Line Chart
df["Date"] = pd.to_datetime(df["Date"])

plt.plot(df["Date"], df["Amount"], marker='o')
plt.title("Expense Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.show()

import pandas as pd

df = pd.read_csv("data/expenses.csv")

# Total Expense
total = df["Amount"].sum()
print("Total Expense:", total)

# Budget Alert
budget = 3000

if total > budget:
    print("⚠ Budget exceeded!")
else:
    print("✅ You are within budget")

print()

# Category Analysis
category_total = df.groupby("Category")["Amount"].sum()
print("Category Spending")
print(category_total)

highest_category = category_total.idxmax()
print("You spend most on:", highest_category)

print()

# Daily Spending
df["Date"] = pd.to_datetime(df["Date"])
daily_spending = df.groupby("Date")["Amount"].sum()

print("Daily Spending")
print(daily_spending)

print()

# Savings Suggestion
avg_spending = df["Amount"].mean()

print("Average spending:", avg_spending)

if avg_spending > 500:
    print("Suggestion: Try reducing daily expenses")
else:
    print("Good job! Your spending is controlled")