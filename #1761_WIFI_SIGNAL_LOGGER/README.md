# 📡 Wi-Fi Metrics Logger & Live Plotter
Monitors and logs real-time Wi-Fi connection metrics (signal strength, transmit/receive rates, channel, etc.) with live graphing.

## 🚀 Features
- Fetches current Wi-Fi interface details using `netsh wlan show interfaces`
- Logs all metrics to a CSV file with timestamps
- Displays **live interactive plot** of:
  - Signal Strength (%)
  - Transmit Rate (Mbps)
- Smooths signal data with a **moving average**
- Limits memory usage with fixed-size deques (`max_points`)
- Updates every few seconds (configurable)

## 📦 Installation
```bash
pip install matplotlib
```

## 💻 Usage
```bash
python wifi.py
```

## 📝 Output
- `wifi_metrics_log.csv` – Timestamped log file
- `Live plot window` – Real-time graph

## 🔧 Requirements
- Python 3.x
- matplotlib
