import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Page config
st.set_page_config(page_title="Smart Expense Tracker", layout="wide")

# Title
st.title("💰 Smart Expense Tracker Pro")

# Load data
df = pd.read_csv("data/expenses.csv")

# Sidebar
st.sidebar.title("⚙ Settings")
budget = st.sidebar.slider("Set Monthly Budget", 1000, 20000, 5000)

# =========================
# Add Expense Form (NEW)
# =========================
st.sidebar.subheader("➕ Add New Expense")

date = st.sidebar.date_input("Date")
category = st.sidebar.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
amount = st.sidebar.number_input("Amount", min_value=0)
desc = st.sidebar.text_input("Description")

if st.sidebar.button("Add Expense"):
    new_data = pd.DataFrame({
        "Date":[date],
        "Category":[category],
        "Amount":[amount],
        "Description":[desc]
    })
    
    new_data.to_csv("data/expenses.csv", mode="a", header=False, index=False)
    
    st.sidebar.success("Expense Added Successfully!")

    # 🔥 Reload updated data
    df = pd.read_csv("data/expenses.csv")

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# =========================
# Machine Learning
# =========================
X = np.arange(len(df)).reshape(-1,1)
y = df["Amount"]

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[len(df)]])[0]

# =========================
# Metrics
# =========================
total = df["Amount"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("💸 Total Expense", total)
col2.metric("📈 Predicted Expense", round(prediction,2))
col3.metric("📊 Average Expense", round(df["Amount"].mean(),2))

# =========================
# Charts
# =========================
col4, col5 = st.columns(2)

with col4:
    st.subheader("📊 Category Distribution")
    category_total = df.groupby("Category")["Amount"].sum()
    fig1, ax1 = plt.subplots()
    category_total.plot(kind="pie", autopct='%1.1f%%', ax=ax1)
    st.pyplot(fig1)

with col5:
    st.subheader("📈 Expense Trend")
    fig2, ax2 = plt.subplots()
    ax2.plot(df["Date"], df["Amount"], marker='o')
    st.pyplot(fig2)

# =========================
# Smart Insights
# =========================
st.subheader("🧠 Insights")

highest = df.groupby("Category")["Amount"].sum().idxmax()
st.write(f"👉 You spend most on **{highest}**")

if total > budget:
    st.error("⚠ Budget exceeded!")
else:
    st.success("✅ Budget under control")

# =========================
# Download Report (NEW)
# =========================
st.subheader("📥 Download Report")

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Expense Data",
    data=csv,
    file_name='expenses_report.csv',
    mime='text/csv',
)

# Footer
st.markdown("---")
st.caption("🚀 Built by Aishwarya | Data Science Project")