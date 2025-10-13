# Battery Health Notifier

A Python script that monitors your laptop's battery health and sends desktop notifications based on battery status.

## Features

- **Real-time Battery Monitoring**: Continuously tracks battery percentage, charging status, and time remaining
- **Smart Notifications**: Alerts when battery is low (≤20%) or fully charged (≥80%)
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Customizable Thresholds**: Easily adjust low and high battery thresholds
- **Lightweight**: Minimal resource usage with configurable check intervals

## Requirements

```bash
pip install psutil plyer
```

- `psutil`: For battery information retrieval
- `plyer`: For desktop notifications (optional but recommended)

## Installation

1. Clone the repository
2. Navigate to the battery_health_notifier directory
3. Install dependencies:
   ```bash
   pip install psutil plyer
   ```

## Usage

Run the script:

```bash
python battery_health_notifier.py
```

### Customization

You can modify the monitoring parameters by editing the `monitor_battery()` function call:

```python
monitor_battery(
    check_interval=60,    # Check every 60 seconds
    low_threshold=20,     # Low battery warning at 20%
    high_threshold=80     # High charge notification at 80%
)
```

## How It Works

1. The script uses `psutil.sensors_battery()` to read battery information
2. It continuously monitors:
   - Battery percentage
   - Charging/discharging status
   - Estimated time remaining
3. Sends notifications when:
   - Battery drops to or below the low threshold while discharging
   - Battery reaches or exceeds the high threshold while charging

## Example Output

```
Battery Health Notifier Started
Low threshold: 20%, High threshold: 80%
Checking every 60 seconds...

Battery: 85% | Charging | Time remaining: N/A
Battery: 95% | Charging | Time remaining: 0h 15m
[Battery Charged] Battery at 95%. Consider unplugging.
```

## Notes

- The script will run continuously until stopped with Ctrl+C
- If `plyer` is not installed, notifications will only print to console
- Battery information availability depends on your system's hardware and OS support

## License

This project is part of the 100 Lines of Python Code collection.
