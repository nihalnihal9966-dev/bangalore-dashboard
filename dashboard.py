import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="Bangalore Urban Analytics Dashboard",
    layout="wide"
)

# Load data
df = pd.read_csv("final_30plus_metrics_database.csv")

# Title
st.title("🏙 Bangalore Urban Form Dashboard")

# Sidebar filter
st.sidebar.header("Ward Selection")

ward = st.sidebar.selectbox(
    "Choose Ward",
    ["All"] + sorted(df["WARD_NAME"].dropna().unique())
)

if ward != "All":
    df = df[df["WARD_NAME"] == ward]

# KPIs
c1, c2, c3, c4 = st.columns(4)

c1.metric("Wards", len(df))
c2.metric("Avg WUFI", round(df["WUFI"].mean(), 2))
c3.metric("Max WUFI", round(df["WUFI"].max(), 2))
c4.metric("Avg Density", round(df["POP_DENSITY"].mean(), 2))

# Charts
st.subheader("Top 10 Wards by WUFI")
top = df.sort_values(by="WUFI", ascending=False).head(10)
st.bar_chart(top.set_index("WARD_NAME")["WUFI"])

st.subheader("Top 10 Population Dense Wards")
dense = df.sort_values(by="POP_DENSITY", ascending=False).head(10)
st.bar_chart(dense.set_index("WARD_NAME")["POP_DENSITY"])

st.subheader("Top 10 Composite Score Wards")
comp = df.sort_values(by="COMPOSITE_SCORE", ascending=False).head(10)
st.bar_chart(comp.set_index("WARD_NAME")["COMPOSITE_SCORE"])

# Dataset table
st.subheader("Ward Indicators Table")
st.dataframe(df, height=500)

st.success("Dashboard Loaded Successfully")
