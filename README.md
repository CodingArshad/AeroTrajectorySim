# AeroTrajectorySim

A Python project that simulates projectile motion using numerical integration. The simulator compares multiple launch angles, visualizes their trajectories, and extracts key flight statistics from each simulation.

## Current Version (V4)

### Features
- Gravity-only projectile motion simulation using Euler integration
- Multiple launch angle comparison
- Trajectory visualization with Matplotlib
- Flight statistics for each trajectory:
  - Flight time
  - Maximum height
  - Horizontal range
- Structured evaluation pipeline with clearly separated stages:
  - `simulate_trajectory` – generates raw motion data
  - `analyze_trajectory` – extracts flight statistics from raw data
  - `get_flight_stats` – combines simulation and analysis into a single `FlightStats` record
  - `run_simulation` – runs the pipeline across multiple launch angles
  - `report` – prints flight statistics per angle
  - `plot_function` – plots trajectories for all simulated angles

## Technologies
- Python
- Matplotlib

## Project Structure
- **Simulation** – Generates projectile trajectories using Euler integration.
- **Analysis** – Extracts flight statistics from the simulated trajectory data.
- **Visualization** – Plots trajectories and displays a comparison of simulation results.

See `docs/algorithm.md` for the full pipeline design.

## Future Versions
### V5
- User-configurable launch velocity and launch angles (currently hardcoded)
- Improved terminal output formatting (single comparison table instead of per-angle blocks)
- Automatic optimal launch angle search
- Larger parameter sweeps

### V6
- Basic aerodynamic drag model
- Comparison between drag and no-drag trajectories

## Long-Term Goals
- Export simulation data for analysis
- Build machine learning datasets from simulation results
- Expand toward more advanced aerospace and autonomy simulations