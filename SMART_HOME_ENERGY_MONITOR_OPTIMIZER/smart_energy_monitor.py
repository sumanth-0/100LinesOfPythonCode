import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from collections import defaultdict

class SmartHomeEnergyMonitor:
    def __init__(self):
        self.devices = {
            'AC': {'power': 1500, 'status': 'off', 'priority': 'low'},
            'Heater': {'power': 2000, 'status': 'off', 'priority': 'medium'},
            'Refrigerator': {'power': 150, 'status': 'on', 'priority': 'high'},
            'TV': {'power': 100, 'status': 'off', 'priority': 'low'},
            'Lights': {'power': 60, 'status': 'off', 'priority': 'medium'},
            'Washer': {'power': 500, 'status': 'off', 'priority': 'low'}
        }
        self.usage_history = defaultdict(list)
        self.max_power = 3000
        
    def simulate_usage(self, hours=24):
        print("\n🏠 Simulating Smart Home Energy Usage...\n")
        current_time = datetime.now()
        for hour in range(hours):
            time_stamp = (current_time + timedelta(hours=hour)).strftime("%H:%M")
            for device in self.devices:
                self.devices[device]['status'] = 'on' if random.random() > 0.5 else 'off'
            total_power = sum(d['power'] for d in self.devices.values() if d['status'] == 'on')
            self.usage_history['time'].append(time_stamp)
            self.usage_history['power'].append(total_power)
        print(f"✅ Simulated {hours} hours of usage data")
        
    def analyze_usage(self):
        total_energy = sum(self.usage_history['power'])
        avg_power = total_energy / len(self.usage_history['power'])
        peak_power = max(self.usage_history['power'])
        print(f"\n📊 Energy Usage Analysis:")
        print(f"   Total Energy: {total_energy:.2f} Wh")
        print(f"   Average Power: {avg_power:.2f} W")
        print(f"   Peak Power: {peak_power:.2f} W")
        print(f"   System Capacity: {self.max_power} W")
        return avg_power, peak_power
        
    def optimize(self):
        print(f"\n⚡ Energy Optimization Recommendations:\n")
        avg_power, peak_power = self.analyze_usage()
        if peak_power > self.max_power:
            print(f"   ⚠️  Peak load ({peak_power}W) exceeds capacity ({self.max_power}W)!")
            print("   💡 Recommendation: Stagger high-power device usage")
        high_usage = [(d, data['power']) for d, data in self.devices.items() 
                      if data['priority'] == 'low' and data['power'] > 200]
        if high_usage:
            print("   💡 High-power, low-priority devices found:")
            for device, power in high_usage:
                print(f"      - {device}: {power}W (Consider off-peak usage)")
        always_on = [d for d, data in self.devices.items() 
                     if data['status'] == 'on' and data['priority'] != 'high']
        if always_on:
            print(f"   💡 Devices that can be turned off: {', '.join(always_on)}")
        potential_savings = sum(self.devices[d]['power'] for d in always_on) * 0.3
        print(f"   💰 Potential monthly savings: ${potential_savings * 24 * 30 * 0.0001:.2f}")
        
    def visualize(self):
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        plt.plot(range(len(self.usage_history['power'])), self.usage_history['power'], 
                 marker='o', color='#2ecc71', linewidth=2)
        plt.axhline(y=self.max_power, color='r', linestyle='--', label='Max Capacity')
        plt.xlabel('Hour')
        plt.ylabel('Power (W)')
        plt.title('Energy Usage Over Time')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.subplot(1, 2, 2)
        device_avg = {d: data['power'] for d, data in self.devices.items()}
        plt.bar(device_avg.keys(), device_avg.values(), color='#3498db')
        plt.xlabel('Device')
        plt.ylabel('Power Rating (W)')
        plt.title('Device Power Consumption')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    monitor = SmartHomeEnergyMonitor()
    monitor.simulate_usage(24)
    monitor.optimize()
    monitor.visualize()
