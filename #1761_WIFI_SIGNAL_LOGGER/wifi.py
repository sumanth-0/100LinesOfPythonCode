import subprocess
import csv
import time
from datetime import datetime
import matplotlib.pyplot as plt
from collections import deque

def get_wifi_info():
    info = {
        "SSID": None,
        "BSSID": None,
        "Radio type": None,
        "Channel": None,
        "Receive rate (Mbps)": None,
        "Transmit rate (Mbps)": None,
        "Signal": None
    }
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"], encoding="utf-8")
        for line in result.split("\n"):
            line = line.strip()
            if line.startswith("SSID") and not line.startswith("SSID name"):
                info["SSID"] = line.split(":", 1)[1].strip()
            elif line.startswith("BSSID"):
                info["BSSID"] = line.split(":", 1)[1].strip()
            elif line.startswith("Radio type"):
                info["Radio type"] = line.split(":", 1)[1].strip()
            elif line.startswith("Channel"):
                info["Channel"] = line.split(":", 1)[1].strip()
            elif line.startswith("Receive rate"):
                try:
                    info["Receive rate (Mbps)"] = float(line.split(":", 1)[1].replace("Mbps", "").strip())
                except:
                    info["Receive rate (Mbps)"] = None
            elif line.startswith("Transmit rate"):
                try:
                    info["Transmit rate (Mbps)"] = float(line.split(":", 1)[1].replace("Mbps", "").strip())
                except:
                    info["Transmit rate (Mbps)"] = None
            elif line.startswith("Signal"):
                info["Signal"] = int(line.split(":", 1)[1].replace("%", "").strip())
    except Exception as e:
        print("Error reading Wi-Fi info:", e)
    return info

def moving_average(data, window_size=5):
    if len(data) == 0:
        return []
    if len(data) < window_size:
        avg_value = sum(data) / len(data)
        return [avg_value] * len(data)
    avg = []
    for i in range(len(data)):
        start = max(0, i - window_size + 1)
        avg.append(sum(data[start:i+1]) / (i - start + 1))
    return avg

def log_and_plot(interval=5, filename="wifi_metrics_log.csv", max_points=100):
    times = deque(maxlen=max_points)
    signals = deque(maxlen=max_points)
    tx_rates = deque(maxlen=max_points)

    # Setup CSV
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow([
                "Timestamp", "SSID", "BSSID", "Radio type", "Channel",
                "Receive rate (Mbps)", "Transmit rate (Mbps)", "Signal (%)"
            ])

        # Setup live plot
        plt.ion()
        fig, ax = plt.subplots(figsize=(14, 6))
        line_signal, = ax.plot([], [], "o-", label="Signal Strength (%)")
        line_tx, = ax.plot([], [], "g--", label="Transmit Rate (Mbps)")
        ax.set_ylim(0, 100)
        ax.set_xlim(0, max_points)
        ax.set_xlabel("Samples")
        ax.set_ylabel("Value")
        ax.set_title("Live Wi-Fi Metrics (Signal & Transmit Rate)")
        ax.legend()
        plt.tight_layout()

        while True:
            data = get_wifi_info()
            timestamp = datetime.now().strftime("%H:%M:%S")

            if data["Signal"] is not None:
                times.append(timestamp)
                signals.append(data["Signal"])
                tx_rates.append(data["Transmit rate (Mbps)"] or 0)

                writer.writerow([
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    data["SSID"], data["BSSID"], data["Radio type"], data["Channel"],
                    data["Receive rate (Mbps)"], data["Transmit rate (Mbps)"], data["Signal"]
                ])
                file.flush()

                print(f"[{timestamp}] SSID: {data['SSID']}, "
                      f"Signal: {data['Signal']}%, "
                      f"TX: {data['Transmit rate (Mbps)']} Mbps, "
                      f"RX: {data['Receive rate (Mbps)']} Mbps, "
                      f"Channel: {data['Channel']}")
            else:
                print(f"[{timestamp}] Unable to read Wi-Fi info.")

            if len(signals) > 0:
                avg_signal = moving_average(list(signals))
                line_signal.set_xdata(range(len(signals)))
                line_signal.set_ydata(signals)

                line_tx.set_xdata(range(len(tx_rates)))
                line_tx.set_ydata(tx_rates)

                # Spaced x-axis labels
                step = max(1, len(times) // 10)
                ax.set_xticks(range(0, len(times), step))
                ax.set_xticklabels([times[i] for i in range(0, len(times), step)], rotation=45, ha="right")

                ax.relim()
                ax.autoscale_view()
                plt.tight_layout()
                plt.pause(0.01)

            time.sleep(interval)

if __name__ == "__main__":
    log_and_plot(interval=3)
