# Road Trip Route Planner 🚗🗺️

A simple Python script for planning optimal road trip routes between cities with basic path optimization.

## Features

- **Static City Map**: Pre-configured network of major US cities
- **Dual Optimization Modes**:
  - Shortest distance (km)
  - Fastest time (hours)
- **Dijkstra's Algorithm**: Efficient pathfinding for optimal routes
- **Interactive CLI**: User-friendly command-line interface
- **Visual Route Display**: Clear step-by-step route visualization

## Usage

### Run the Script

```bash
python road_trip_planner.py
```

### Example Session

```
🚗 ROAD TRIP ROUTE PLANNER 🗺️
Available cities:
  Atlanta, Boston, Charlotte
  Chicago, Cincinnati, Cleveland
  ...

Enter starting city: New York
Enter destination city: Chicago

Optimization options:
  1. Shortest distance
  2. Fastest time
Choose option (1/2): 1

============================================================
Route (DISTANCE optimized):
  1. New York
     ↓
  2. Philadelphia
     ↓
  3. Pittsburgh
     ↓
  4. Cleveland
     ↓
  5. Detroit
     ↓
  6. Chicago

Total distance: 985.0 km
============================================================
```

## How It Works

1. **City Network**: The script uses a static graph where cities are nodes and routes are weighted edges
2. **Dijkstra's Algorithm**: Finds the optimal path based on selected criteria (distance or time)
3. **Priority Queue**: Uses heapq for efficient path exploration
4. **Path Reconstruction**: Tracks the complete route from start to destination

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Limitations

- Static map with pre-defined cities (21 major US cities)
- Simplified distance and time calculations
- No real-time traffic data
- Limited to connected cities in the network

## Future Enhancements

- Add more cities and routes
- Support for waypoints/multiple stops
- Export routes to file
- Integration with mapping APIs
- Fuel cost calculations

## Author

Created for issue #617 - 100 Lines of Python Code Project

## License

Open source - feel free to modify and enhance!
