# AeroTrajectorySim

A Python project that simulates projectile motion using numerical integration. The simulator compares multiple launch angles, visualizes their trajectories, and extracts key flight statistics from each simulation.

## Current Version (V3)

### Features
- Gravity-only projectile motion simulation
- Multiple launch angle comparison
- Trajectory visualization with Matplotlib
- Flight statistics for each trajectory:
  - Flight time
  - Maximum height
  - Horizontal range
- Modular simulation function with separate analysis and visualization stages

## Technologies
- Python
- Matplotlib
- Math

## Project Structure
- **Simulation** – Generates projectile trajectories using Euler integration.
- **Analysis** – Extracts flight statistics from the simulated trajectory data.
- **Visualization** – Plots trajectories and displays a comparison of simulation results.

## Future Versions
### V4
- User-configurable launch velocity
- User-configurable launch angles
- Improved terminal output formatting

### V5
- Automatic optimal launch angle search
- Larger parameter sweeps
- Improved experiment workflow

### V6
- Basic aerodynamic drag model
- Comparison between drag and no-drag trajectories

## Long-Term Goals
- Export simulation data for analysis
- Build machine learning datasets from simulation results
- Expand toward more advanced aerospace and autonomy simulations