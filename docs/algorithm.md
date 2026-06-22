# AeroTrajectorySim V5 Algorithm

## Goal
Simulate projectile motion across a user-defined sweep of launch angles, identify the angle that maximizes range, and present results as a single comparison table plus selected trajectory plots.

---

## Inputs
- Launch velocity (m/s) — user-provided at runtime
- Sweep step size (degrees) — user-provided; sweep range is fixed at 0–90°, since every physically meaningful launch angle falls in that range
- Gravity (g)
- Time step (dt)

---

## Outputs
A list of FlightStats objects, one per swept angle, each containing:
- launch_angle
- flight_time
- max_height
- horizontal_range

Plus:
- a single printed comparison table covering every simulated angle
- the optimal launch angle (maximum horizontal_range) highlighted/reported separately
- trajectory plots for a small selected subset of angles (not the entire sweep, to keep the plot readable)

---

## Data Structure

### FlightStats
A structured record containing:
- launch_angle
- flight_time
- max_height
- horizontal_range

One instance per simulation.

---

## Core Functions

### 1. get_user_inputs()
**Input:**
- none (reads from terminal input)

**Output:**
- velocity
- step (degrees)

**Purpose:**
Replace the hardcoded `launch_vel` and `launch_angles` constants with runtime user input. Should validate that velocity > 0 and step > 0.

---

### 2. generate_angle_sweep(step)
**Input:**
- step (degrees)

**Output:**
- list of angles in radians, covering the fixed range 0–90°

**Purpose:**
Replace the old fixed three-angle list with a generated sweep, so the number of simulated angles scales with the requested step instead of being hardcoded. The range itself (0–90°) is not a parameter, since it never needs to change.

---

### 3. simulate_trajectory(v, angle)
**Input:**
- velocity
- angle (radians)

**Output:**
- x[], y[], time[]

**Purpose:**
Numerically simulate motion using Euler integration until y <= 0. (Unchanged from V4.)

---

### 4. analyze_trajectory(x, y, t)
**Input:**
- trajectory lists

**Output:**
- flight_time = last time value
- max_height = max(y)
- horizontal_range = last x value

(Unchanged from V4.)

---

### 5. get_flight_stats(v, angle)
**Input:**
- velocity
- angle

**Process:**
1. Call simulate_trajectory
2. Call analyze_trajectory
3. Return FlightStats object

**Output:**
- FlightStats

(Unchanged from V4 — formerly named `organize_flight_stats` in earlier drafts of this doc.)

---

### 6. run_simulation(angles, velocity)
**Input:**
- list of angles (from generate_angle_sweep)
- velocity

**Process:**
- loop through angles
- call get_flight_stats
- store results in list

**Output:**
- list[FlightStats]

(Unchanged from V4, now expected to handle larger lists from a sweep.)

---

### 7. find_optimal_angle(results)
**Input:**
- list[FlightStats]

**Process:**
- scan the list for the entry with the maximum horizontal_range

**Output:**
- the single FlightStats with the greatest horizontal_range

**Purpose:**
Answers "which launch angle produced the farthest shot?" without requiring a separate optimization library — a direct scan over already-simulated results is sufficient since the sweep is discrete.

---

### 8. print_comparison_table(results)
**Input:**
- list[FlightStats]

**Output:**
- one aligned table printed to the terminal, one row per angle, columns for flight_time, max_height, horizontal_range

**Purpose:**
Replaces the old per-angle `report()` block (which printed four lines per angle) with a single readable table — necessary once the sweep produces many more angles than the old fixed list of three.

---

### 9. plot_trajectories(angles, velocity)
**Input:**
- whatever list of angles the caller passes in

**Process:**
- re-run simulate_trajectory per angle given
- plot x vs y

**Purpose:**
Plots exactly the angles it's given — it has no opinion about which angles are "interesting" or how many to show. That selection decision belongs to the caller (see Execution Flow below), keeping this function a pure consumer like the rest of the reporting/plotting layer.

---

## Execution Flow

1. Call get_user_inputs() → velocity, step
2. Call generate_angle_sweep(step) → list of angles (radians), covering 0–90°
3. Call run_simulation(angles, velocity) → list[FlightStats]
4. Call print_comparison_table(results)
5. Call find_optimal_angle(results) → optimal_angle, and report it separately
6. Build a fixed 5-angle plotting selection and call plot_trajectories() with it:
   - 0°
   - the midpoint between 0° and optimal_angle
   - optimal_angle
   - the midpoint between optimal_angle and 90°
   - 90°

---

## Design Rule

- Simulation only produces raw motion data
- Analysis only extracts metrics
- get_flight_stats combines both into a single structured object
- Reporting, table-printing, optimal-angle search, and plotting do NOT compute physics — they only consume FlightStats results
