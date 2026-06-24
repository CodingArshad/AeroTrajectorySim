# AeroTrajectorySim

A Python project that simulates projectile motion using numerical integration. The simulator compares multiple launch angles under both drag and no-drag conditions, extracts key flight statistics, and visualizes the effect of aerodynamic drag on the optimal trajectory.

## Current Version (V6)

### Features
- Projectile motion simulation using Euler integration — with and without aerodynamic drag
- Hardcoded drag model based on a simple sphere (Cd, area, air density, mass) combined into a single drag factor k
- User-configurable launch velocity and angle sweep step size, entered at runtime
- Automatic angle sweep across the full 0–90° range
- Two separate comparison tables: one for no-drag results, one for drag results
- Automatic optimal launch angle search for both conditions (maximum horizontal range)
- Trajectory plot comparing the no-drag optimal and drag optimal trajectories on the same graph
- Structured evaluation pipeline with clearly separated stages:
  - `get_user_input` – prompts for launch velocity and sweep step size
  - `generate_angle_sweep` – builds the 0–90° angle list from the step size
  - `simulate_trajectory` – Euler integration, no drag
  - `simulate_trajectory_drag` – Euler integration with drag applied per timestep
  - `analyze_trajectory` – extracts flight statistics from raw trajectory data
  - `get_flight_stats` / `get_flight_stats_drag` – combines simulation and analysis into a `FlightStats` record
  - `run_simulation` / `run_simulation_drag` – runs the full sweep for each condition
  - `print_comparison_table` – prints a labelled aligned table of results
  - `find_optimal_angle` – finds the angle with the greatest horizontal range
  - `plot_comparison` – plots drag vs no-drag trajectories for the two optimal angles

## Technologies
- Python
- Matplotlib

## Project Structure
- **Simulation** – Generates projectile trajectories using Euler integration, with and without drag.
- **Analysis** – Extracts flight statistics from the simulated trajectory data.
- **Visualization** – Plots drag vs no-drag trajectories and displays comparison tables.

See `docs/algorithm.md` for the full pipeline design.

## Long-Term Goals
- Export simulation data for analysis
- Build machine learning datasets from simulation results
- Expand toward more advanced aerospace and autonomy simulations