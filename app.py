import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Sample Data
data = pd.DataFrame({
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    'Price': [1000, 500, 300, 200, 100],
    'Quantity': [50, 200, 150, 75, 300],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories']
})

# Page Configuration
st.set_page_config(page_title="Simple Data Dashboard", layout="wide")
st.title("📊 Simple Data Dashboard")

# Data Preview
st.subheader("Data Preview")
st.dataframe(data)

# Summary Statistics
st.subheader("Summary Statistics")
st.write(data.describe())

# Filter Data
st.subheader("Filter Data")
filter_column = st.selectbox("Select Column to Filter", data.columns)
filter_value = st.selectbox("Select Value", data[filter_column].unique())
filtered_data = data[data[filter_column] == filter_value]
st.write(filtered_data)

# Data Visualization
st.subheader("Plot Data")
plot_column = st.selectbox("Select Numeric Column to Plot", data.select_dtypes(include=['int64', 'float64']).columns)
if not filtered_data.empty:
    fig, ax = plt.subplots()
    ax.bar(filtered_data['Product'], filtered_data[plot_column], color='skyblue')
    ax.set_xlabel('Product')
    ax.set_ylabel(plot_column)
    ax.set_title(f'{plot_column} by Product')
    st.pyplot(fig)
else:
    st.info("No data available for the selected filter.")
