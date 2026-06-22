# AeroTrajectorySim

A Python project that simulates projectile motion using numerical integration. The simulator compares multiple launch angles, visualizes their trajectories, and extracts key flight statistics from each simulation.

## Current Version (V5)

### Features
- Gravity-only projectile motion simulation using Euler integration
- User-configurable launch velocity and angle sweep step size, entered at runtime
- Automatic angle sweep across the full 0–90° range, generated from the step size
- Trajectory visualization with Matplotlib for a representative subset of angles (0°, optimal, 90°, and the midpoints between them)
- Flight statistics for each trajectory:
  - Flight time
  - Maximum height
  - Horizontal range
- Single comparison table covering every simulated angle
- Automatic optimal launch angle search (maximum horizontal range)
- Structured evaluation pipeline with clearly separated stages:
  - `get_user_input` – prompts for launch velocity and sweep step size
  - `generate_angle_sweep` – builds the 0–90° angle list from the step size
  - `simulate_trajectory` – generates raw motion data
  - `analyze_trajectory` – extracts flight statistics from raw data
  - `get_flight_stats` – combines simulation and analysis into a single `FlightStats` record
  - `run_simulation` – runs the pipeline across all swept angles
  - `print_comparison_table` – prints a single aligned table of all results
  - `find_optimal_angle` – finds the angle with the greatest horizontal range
  - `plot_function` – plots trajectories for a given list of angles

## Technologies
- Python
- Matplotlib

## Project Structure
- **Simulation** – Generates projectile trajectories using Euler integration.
- **Analysis** – Extracts flight statistics from the simulated trajectory data.
- **Visualization** – Plots trajectories and displays a comparison of simulation results.

See `docs/algorithm.md` for the full pipeline design.

## Future Versions
### V6
- Basic aerodynamic drag model
- Comparison between drag and no-drag trajectories

## Long-Term Goals
- Export simulation data for analysis
- Build machine learning datasets from simulation results
- Expand toward more advanced aerospace and autonomy simulations