import math
import matplotlib.pyplot as plt
from dataclasses import dataclass

# Set initial conditions
launch_vel = 10
launch_angles = [math.radians(angle) for angle in [30, 45, 60]]
g = 9.81
dt = 0.1

#Define Functions:

## Function simulates the trajectory and outputs the x, y, and times in lists for a given launch velocity and angle
def simulate_trajectory(launch_vel, launch_angle):
    # Constants
    x_pos = 0
    y_pos = 0
    time = 0

    x_vel = launch_vel * math.cos(launch_angle)
    y_vel = launch_vel * math.sin(launch_angle)

    # Lists to store trajectory points
    x = []
    y = []
    times = []

    # Simulate trajectory
    while True:
        x.append(x_pos)
        y.append(y_pos)
        times.append(time)

        x_pos += x_vel * dt
        y_pos += y_vel * dt
        y_vel -= g * dt
        time += dt

        if y_pos <= 0 and time > 0:
            break
    return x, y, times

## Function to compute the flight statistics for a given launch angle
def analyze_trajectory(x, y, times):
    flight_time = times[-1]
    max_height = max(y)
    horizontal_range = x[-1]
    return flight_time, max_height, horizontal_range

## Data class to store flight statistics
@dataclass
class FlightStats:
    launch_angle: float
    flight_time: float
    max_height: float
    horizontal_range: float

## Function to cleanly return the flight statistics
def get_flight_stats(launch_vel, launch_angle):
    x, y, times = simulate_trajectory(launch_vel, launch_angle)
    return FlightStats(launch_angle=launch_angle, flight_time=times[-1], max_height=max(y), horizontal_range=x[-1])

## Function to output the results in a formatted table
def report(results):
    print(f"Launch Angle: {math.degrees(results.launch_angle):.2f} degrees")
    print(f"Flight Time: {results.flight_time:.2f} seconds")
    print(f"Max Height: {results.max_height:.2f} meters")
    print(f"Range: {results.horizontal_range:.2f} meters")

## Function to run the simulation
def run_simulation(angles, launch_vel):
    results = []
    for angle in angles:
        stat = get_flight_stats(launch_vel, angle)
        results.append(stat)
    return results

# Function to plot the trajectory for each launch angle
def plot_function(launch_vel, launch_angles):
    for i in range(len(launch_angles)):
        x, y, times = simulate_trajectory(launch_vel, launch_angles[i])
        # Store trajectory for plotting
        plt.plot(x, y, label='{:.2f} degrees'.format(math.degrees(launch_angles[i])))

    # Plot trajectory
    plt.title('Trajectory Graph')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.legend()
    plt.show()

# Run the simulation and plot the results
results = run_simulation(launch_angles, launch_vel)
for result in results:
    report(result)
plot_function(launch_vel, launch_angles)