# AeroTrajectorySim V4 Algorithm

## Goal
Simulate projectile motion for multiple launch configurations and return structured flight results using a clean evaluation pipeline.

---

## Inputs
- Launch velocity (m/s) — user-defined
- Launch angles (degrees → radians)
- Gravity (g)
- Time step (dt)

---

## Outputs
A list of FlightStats objects, each containing:
- launch_angle
- flight_time
- max_height
- horizontal_range

Plus:
- trajectory plots for selected angles
- printed comparison table

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

### 1. simulate_trajectory(v, angle)
**Input:**
- velocity
- angle (radians)

**Output:**
- x[], y[], time[]

**Purpose:**
Numerically simulate motion using Euler integration until y <= 0.

---

### 2. analyze_trajectory(x, y, t)
**Input:**
- trajectory lists

**Output:**
- flight_time = last time value
- max_height = max(y)
- horizontal_range = last x value

---

### 3. organize_flight_stats(v, angle)
**Input:**
- velocity
- angle

**Process:**
1. Call simulate_trajectory
2. Call analyze_trajectory
3. Return FlightStats object

**Output:**
- FlightStats

---

### 4. run_simulation(angles, velocity)
**Input:**
- list of angles
- velocity

**Process:**
- loop through angles
- call evaluate_configuration
- store results in list

**Output:**
- list[FlightStats]

---

### 5. report(results)
**Input:**
- list[FlightStats]

**Output:**
- formatted table printed to terminal

---

### 6. plot_trajectories(angles, velocity)
**Input:**
- selected angles

**Process:**
- re-run simulate_trajectory per angle
- plot x vs y

---

## Execution Flow

1. Define inputs (velocity, angles, dt, g)
2. Run run_simulation()
3. Store list of FlightStats
4. Call report()
5. Call plot_trajectories()

---

## Design Rule

- Simulation only produces raw motion data
- Analysis only extracts metrics
- Evaluation combines both into a single structured object
- Reporting and plotting do NOT compute physics