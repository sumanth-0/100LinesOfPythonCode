# Smart Home Energy Usage Monitor & Optimizer

## Description
A Python script that monitors smart home energy usage, provides optimization recommendations, and visualizes consumption patterns. This tool helps users understand their energy consumption and identify opportunities for savings.

## Features
- **Simulated Data Generation**: Creates realistic energy usage data for common household devices
- **Real-time Monitoring**: Tracks power consumption across multiple devices
- **Usage Analysis**: Calculates total energy, average power, and peak consumption
- **Smart Optimization**: Provides actionable recommendations to reduce energy costs
- **Data Visualization**: Displays usage patterns and device consumption through interactive charts

## Devices Monitored
- Air Conditioner (1500W)
- Heater (2000W)
- Refrigerator (150W)
- TV (100W)
- Lights (60W)
- Washer (500W)

## Requirements
```bash
pip install matplotlib
```

## Usage
```bash
python smart_energy_monitor.py
```

## Output
The script will:
1. Simulate 24 hours of energy usage
2. Analyze consumption patterns
3. Provide optimization recommendations
4. Display visualization charts showing:
   - Energy usage over time
   - Power consumption by device

## Optimization Recommendations
The system identifies:
- Peak load warnings when capacity is exceeded
- High-power, low-priority devices for off-peak scheduling
- Devices that can be turned off to save energy
- Potential monthly cost savings

## Example Output
```
🏠 Simulating Smart Home Energy Usage...
✅ Simulated 24 hours of usage data

📊 Energy Usage Analysis:
   Total Energy: 42150.00 Wh
   Average Power: 1756.25 W
   Peak Power: 3810.00 W
   System Capacity: 3000 W

⚡ Energy Optimization Recommendations:
   ⚠️  Peak load (3810W) exceeds capacity (3000W)!
   💡 Recommendation: Stagger high-power device usage
   💡 High-power, low-priority devices found:
      - AC: 1500W (Consider off-peak usage)
   💰 Potential monthly savings: $32.40
```

## Contributing
Submitted for issue #629

## License
MIT License
