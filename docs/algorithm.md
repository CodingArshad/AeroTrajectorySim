# AeroTrajectorySim V6 Algorithm

## Goal
Extend the V5 simulation with a drag model, run both drag and no-drag sweeps across 0–90°, identify the optimal angle under each condition, and compare them in a single table and a two-line trajectory plot.

---

## Inputs
- Launch velocity (m/s) — user-provided at runtime
- Sweep step size (degrees) — user-provided; sweep range fixed at 0–90°
- Gravity (g) — hardcoded constant
- Time step (dt) — hardcoded constant
- Drag constants — all hardcoded, physical properties of a simple sphere:
  - Cd = 0.47 (drag coefficient)
  - A = 0.00785 m² (cross-sectional area)
  - rho = 1.225 kg/m³ (air density at sea level)
  - mass = 0.1 kg
  - These four combine into a single drag factor k = (Cd * rho * A) / (2 * mass), computed once at the top of the file and reused in the drag simulation function

---

## Outputs
Two lists of FlightStats objects (one per sweep, drag and no-drag), each containing:
- launch_angle
- flight_time
- max_height
- horizontal_range

Plus:
- a single comparison table showing both drag and no-drag results side by side for every swept angle
- the optimal angle (max horizontal_range) reported separately for both conditions
- a two-line trajectory plot for the no-drag optimal angle only: one line with drag, one without

---

## Data Structure

### FlightStats
Unchanged from V5:
- launch_angle
- flight_time
- max_height
- horizontal_range

One instance per simulation. No drag flag needed — the two sweeps produce two separate lists, so each list is already implicitly all-drag or all-no-drag.

---

## Core Functions

### 1. get_user_input()
Unchanged from V5. Returns velocity, step.

---

### 2. generate_angle_sweep(step)
Unchanged from V5. Returns list of angles in radians, 0–90°.

---

### 3. simulate_trajectory(v, angle)
Unchanged from V5. Euler integration, no drag.

---

### 4. simulate_trajectory_drag(v, angle)
**Input:**
- velocity
- angle (radians)

**Output:**
- x[], y[], time[]

**Purpose:**
Same structure as simulate_trajectory, but at each timestep also computes and applies drag deceleration before updating velocity.

**Drag calculation per timestep:**
1. Compute current speed: `speed = sqrt(x_vel² + y_vel²)`
2. Compute drag deceleration magnitude: `drag_decel = k * speed²`
3. Apply it to each velocity component, opposing the current direction of travel:
   - `x_vel -= (drag_decel * x_vel / speed) * dt`
   - `y_vel -= (drag_decel * y_vel / speed) * dt`
4. Then apply gravity to y_vel as usual: `y_vel -= g * dt`
5. Then update positions as usual

Note: when speed is 0 the division would cause a crash — but in practice this can't happen mid-flight since the projectile is always moving. No special guard needed.

---

### 5. analyze_trajectory(x, y, t)
Unchanged from V5.

---

### 6. get_flight_stats(v, angle)
Unchanged from V5. Calls simulate_trajectory (no drag).

---

### 7. get_flight_stats_drag(v, angle)
**Input:**
- velocity
- angle

**Process:**
1. Call simulate_trajectory_drag
2. Call analyze_trajectory
3. Return FlightStats object

**Output:**
- FlightStats

Same structure as get_flight_stats, but uses the drag simulation.

---

### 8. run_simulation(angles, velocity)
Unchanged from V5. Returns list[FlightStats] without drag.

---

### 9. run_simulation_drag(angles, velocity)
**Input:**
- list of angles
- velocity

**Process:**
- loop through angles
- call get_flight_stats_drag
- store results in list

**Output:**
- list[FlightStats]

Same structure as run_simulation, but uses drag versions.

---

### 10. find_optimal_angle(results)
Unchanged from V5. Works on either drag or no-drag results list.

---

### 11. print_comparison_table(results_no_drag, results_drag)
**Input:**
- list[FlightStats] — no-drag results
- list[FlightStats] — drag results

**Output:**
- one aligned table printed to terminal, one row per angle, with columns for both no-drag and drag values side by side: launch_angle, range (no drag), range (drag), max_height (no drag), max_height (drag)

**Purpose:**
Updated from V5 to show both conditions together so the effect of drag is immediately visible per angle.

---

### 12. plot_comparison(launch_vel, optimal_angle)
**Input:**
- launch velocity
- the optimal angle (in radians) found from the no-drag results

**Process:**
1. Call simulate_trajectory(launch_vel, optimal_angle) → no-drag x, y
2. Call simulate_trajectory_drag(launch_vel, optimal_angle) → drag x, y
3. Plot both x vs y on the same axes with clear labels: "No Drag" and "Drag"
4. Add title, axis labels, legend, show

**Purpose:**
Replaces the V5 5-angle plot_function. Shows exactly two trajectories — drag vs no-drag — for the single most interesting angle (the theoretical optimum), making the effect of drag visually obvious.

---

## Execution Flow

1. Call get_user_input() → velocity, step
2. Call generate_angle_sweep(step) → angles
3. Call run_simulation(angles, velocity) → results_no_drag
4. Call run_simulation_drag(angles, velocity) → results_drag
5. Call print_comparison_table(results_no_drag, results_drag)
6. Call find_optimal_angle(results_no_drag) → optimal_no_drag, print it
7. Call find_optimal_angle(results_drag) → optimal_drag, print it
8. Call plot_comparison(velocity, optimal_no_drag.launch_angle)

---

## Design Rule

- Simulation only produces raw motion data
- Analysis only extracts metrics
- get_flight_stats / get_flight_stats_drag combine both into a single structured object
- Reporting, table-printing, optimal-angle search, and plotting do NOT compute physics — they only consume FlightStats results
