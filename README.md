# AeroTrajectorySim

A Python project that simulates projectile motion under gravity and visualizes trajectories using Matplotlib.

## Current Version (V2)
- Gravity-only projectile simulation
- Multi-angle trajectory comparison
- Reusable simulation function for trajectory generation
- Euler method numerical integration (time-stepped physics)

## Inputs
- Launch velocity (m/s)
- List of launch angles (degrees, converted internally to radians)

## Outputs
- 2D trajectory plot (x vs y)
- Multiple trajectories displayed on a single graph with labels

## Core Features
- Function-based simulation design
- Separation of simulation and visualization
- Loop-based experiment execution
- Basic physics model (constant gravity)

## Future Versions
- Flight statistics (time of flight, max height, range)
- Data export (CSV / structured datasets)
- Drag and air resistance model
- NumPy-based vectorized simulation upgrade
- Interactive parameter input system