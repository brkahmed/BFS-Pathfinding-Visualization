# BFS Pathfinding Visualization

This project visualizes the Breadth-First Search (BFS) pathfinding algorithm using Pygame and NumPy. It demonstrates finding the shortest path between a start and a target point on a grid map with obstacles.

## Requirements

- Python 3.x
- NumPy
- Pygame

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/brkahmed/bfs-pathfinding-visualization.git
   cd bfs-pathfinding-visualization
   ```

2. Install the required packages:
    ```bash
    pip install numpy pygame
    ```

## Usage
- Run the script to start the visualization:
    ```bash
    python main.py
    ```

- You can create your own map by editing values in map.csv file
  - EMPTY -> 0
  - TARGET -> 1
  - START -> 2
  - OBSTACLE -> 3

## BFS Algorithm
Breadth-First Search (BFS) is used to find the shortest path in an unweighted grid. It explores all possible paths level by level from the start cell until it reaches the target cell, ensuring the shortest path is found.
