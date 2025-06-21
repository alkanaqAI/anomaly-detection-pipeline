# Anomaly Detection Pipeline

End-to-end ETL + ML pipeline for time-series anomaly detection using real-world data.

## 🔧 Project Structure
```text
anomaly-detection-pipeline/
├── app/
│   └── streamlit_app.py
├── data/
│   ├── AAPL_raw.csv
│   ├── AAPL_clean.csv
│   └── AAPL_with_anomalies.csv
├── notebooks/
│   ├── 01_fetch_stock_data.ipynb
│   ├── 02_clean_transform.ipynb
│   └── 03_train_anomaly_model.ipynb
├── requirements.txt
├── .gitignore
└── README.md

## 📈 Dataset
Using `yfinance` to get hourly AAPL stock data for the past 7 days.

## 🚀 Roadmap
- [x] Project setup
- [ ] Data cleaning
- [ ] Anomaly detection model
- [ ] Streamlit or REST API deployment
