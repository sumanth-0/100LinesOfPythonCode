#!/usr/bin/env python3
"""Road Trip Route Planner - Plan optimal routes between cities"""

import heapq
from typing import Dict, List, Tuple, Optional

# Static map of cities with distances (km) and travel times (hours)
CITY_MAP = {
    'New York': [('Boston', 215, 3.5), ('Philadelphia', 95, 1.8), ('Washington', 225, 3.8)],
    'Boston': [('New York', 215, 3.5), ('Portland', 105, 2.0)],
    'Philadelphia': [('New York', 95, 1.8), ('Washington', 140, 2.3), ('Pittsburgh', 305, 5.0)],
    'Washington': [('New York', 225, 3.8), ('Philadelphia', 140, 2.3), ('Richmond', 110, 1.8)],
    'Pittsburgh': [('Philadelphia', 305, 5.0), ('Cleveland', 135, 2.2), ('Columbus', 185, 3.0)],
    'Cleveland': [('Pittsburgh', 135, 2.2), ('Detroit', 170, 2.8), ('Columbus', 145, 2.4)],
    'Detroit': [('Cleveland', 170, 2.8), ('Chicago', 280, 4.5)],
    'Chicago': [('Detroit', 280, 4.5), ('Milwaukee', 90, 1.5), ('St Louis', 300, 4.8)],
    'Columbus': [('Pittsburgh', 185, 3.0), ('Cleveland', 145, 2.4), ('Cincinnati', 110, 1.8)],
    'Cincinnati': [('Columbus', 110, 1.8), ('Louisville', 100, 1.6), ('Indianapolis', 110, 1.8)],
    'Indianapolis': [('Cincinnati', 110, 1.8), ('Chicago', 185, 3.0), ('Louisville', 115, 1.9)],
    'Louisville': [('Cincinnati', 100, 1.6), ('Indianapolis', 115, 1.9), ('Nashville', 175, 2.8)],
    'Nashville': [('Louisville', 175, 2.8), ('Memphis', 210, 3.3), ('Atlanta', 250, 4.0)],
    'Atlanta': [('Nashville', 250, 4.0), ('Charlotte', 245, 3.9), ('Jacksonville', 345, 5.5)],
    'Charlotte': [('Atlanta', 245, 3.9), ('Richmond', 300, 4.8)],
    'Richmond': [('Washington', 110, 1.8), ('Charlotte', 300, 4.8)],
    'Milwaukee': [('Chicago', 90, 1.5)],
    'St Louis': [('Chicago', 300, 4.8), ('Memphis', 285, 4.5)],
    'Memphis': [('St Louis', 285, 4.5), ('Nashville', 210, 3.3)],
    'Portland': [('Boston', 105, 2.0)],
    'Jacksonville': [('Atlanta', 345, 5.5)]
}

def dijkstra(start: str, end: str, optimize: str = 'distance') -> Optional[Tuple[List[str], float]]:
    """Find optimal route using Dijkstra's algorithm"""
    if start not in CITY_MAP or end not in CITY_MAP:
        return None
    
    idx = 1 if optimize == 'distance' else 2
    pq = [(0, start, [start])]
    visited = set()
    
    while pq:
        cost, city, path = heapq.heappop(pq)
        if city in visited:
            continue
        if city == end:
            return path, cost
        visited.add(city)
        for neighbor, dist, time in CITY_MAP.get(city, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + (dist if idx == 1 else time), neighbor, path + [neighbor]))
    return None

def display_route(route: List[str], cost: float, optimize: str):
    """Display route information"""
    print(f"\n{'='*60}")
    print(f"Route ({optimize.upper()} optimized):")
    for i, city in enumerate(route):
        print(f"  {i+1}. {city}")
        if i < len(route) - 1:
            print("     ↓")
    unit = 'km' if optimize == 'distance' else 'hours'
    print(f"\nTotal {optimize}: {cost:.1f} {unit}")
    print(f"{'='*60}")

def main():
    print("\n🚗 ROAD TRIP ROUTE PLANNER 🗺️")
    print("Available cities:")
    cities = sorted(CITY_MAP.keys())
    for i in range(0, len(cities), 3):
        print("  " + ", ".join(cities[i:i+3]))
    
    try:
        start = input("\nEnter starting city: ").strip()
        end = input("Enter destination city: ").strip()
        print("\nOptimization options:")
        print("  1. Shortest distance")
        print("  2. Fastest time")
        choice = input("Choose option (1/2): ").strip()
        
        optimize = 'distance' if choice == '1' else 'time'
        result = dijkstra(start, end, optimize)
        
        if result:
            route, cost = result
            display_route(route, cost, optimize)
        else:
            print(f"\n❌ No route found between {start} and {end}")
    except KeyboardInterrupt:
        print("\n\nExiting...")

if __name__ == "__main__":
    main()
