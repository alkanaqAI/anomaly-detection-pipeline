import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load data
symbol = "AAPL"
df = pd.read_csv(f"data/{symbol}_with_anomalies.csv", parse_dates=True, index_col=0)

# Clean column names (just in case)
df.columns = df.columns.str.strip()

# Page setup
st.set_page_config(page_title="Stock Anomaly Dashboard", layout="wide")
st.title(f"{symbol} Stock Anomaly Detection")

# Show raw data checkbox
if st.checkbox("Show raw data"):
    st.dataframe(df.tail(20))

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df.index, df['Close'], label='Close Price', color='blue')
ax.scatter(df.index[df['anomaly_flag'] == 1], df['Close'][df['anomaly_flag'] == 1],
           color='red', label='Anomaly', marker='x')
ax.set_title(f"{symbol} Price with Anomalies")
ax.legend()
st.pyplot(fig)
