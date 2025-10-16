import streamlit as st
import pandas as pd

st.set_page_config(page_title="Employee Analytics Dashboard", layout="wide")

st.title("📊 Employee Analytics Dashboard (50K+ Rows)")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("employee_data.csv")

df = load_data()

st.success(f"Loaded {len(df):,} employee records")

# Filters
col1, col2, col3 = st.columns(3)
with col1:
    dept = st.selectbox("Select Department", ["All"] + sorted(df["Department"].unique()))
with col2:
    loc = st.selectbox("Select Location", ["All"] + sorted(df["Location"].unique()))
with col3:
    min_exp = st.slider("Minimum Experience (years)", 0, 15, 0)

# Filtered dataset
filtered_df = df.copy()
if dept != "All":
    filtered_df = filtered_df[filtered_df["Department"] == dept]
if loc != "All":
    filtered_df = filtered_df[filtered_df["Location"] == loc]
filtered_df = filtered_df[filtered_df["Experience"] >= min_exp]

st.write(f"Showing {len(filtered_df):,} matching employees")

# Display data
st.dataframe(filtered_df.head(100))  # limit display for performance

# Summary statistics
st.subheader("📈 Summary Statistics")
st.write(filtered_df.describe())

# Charts
st.subheader("💰 Average Salary by Department")
st.bar_chart(filtered_df.groupby("Department")["Salary"].mean())

st.subheader("📍 Employee Count by Location")
st.bar_chart(filtered_df["Location"].value_counts())