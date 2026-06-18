# AeroTrajectorySim V3 Algorithm

## Goal
Simulate projectile motion under gravity for multiple launch angles and extract key flight statistics from each trajectory.

---

## Inputs
- Launch velocity (m/s)
- List of launch angles (degrees → converted to radians)
- Gravity (g)
- Time step (dt)

---

## Outputs
For each launch angle:
- x positions (list)
- y positions (list)
- time values (list)

And across all angles:
- angles
- flight_times
- max_heights
- ranges

---

## Algorithm

### 1. Setup
- Define launch velocity
- Define list of launch angles
- Convert angles to radians
- Set gravity (g)
- Set time step (dt)
- Initialize empty result lists:
  - angles
  - flight_times
  - max_heights
  - ranges

---

### 2. Simulation Function (single angle)

For a given angle:

1. Initialize position and time:
   - x_pos = 0
   - y_pos = 0
   - time = 0

2. Compute velocity components:
   - x_vel = v * cos(angle)
   - y_vel = v * sin(angle)

3. Initialize storage lists:
   - x
   - y
   - times

4. While y_pos > 0:
   - Append current x_pos, y_pos, time
   - Update x_pos using x_vel
   - Update y_pos using y_vel
   - Update y_vel using gravity
   - Increment time

5. Return x, y, times

---

### 3. Experiment Loop

For each angle:

1. Run simulation function
2. Receive x, y, times

3. Compute:
   - flight_time = last element of times
   - max_height = max(y)
   - range = last element of x

4. Store results:
   - angles.append(angle)
   - flight_times.append(flight_time)
   - max_heights.append(max_height)
   - ranges.append(range)

---

### 4. Visualization

After all runs:

- Plot all x vs y trajectories
- Label each trajectory by angle
- Add title, labels, legend
- Display plot
- print angles, flight_times, max_heights, and ranges in a nice format