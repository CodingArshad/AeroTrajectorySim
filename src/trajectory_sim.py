import math
import matplotlib.pyplot as plt
from dataclasses import dataclass

# Set initial conditions
g = 9.81
dt = 0.1

#Define Functions:

## Function to get user input for launch velocity and angles
def get_user_input():
    print('ALL GIVEN VALUES MUST BE POSITIVE NUMBERS')
    launch_vel = float(input('Enter launch velocity (m/s):'))
    step = float(input('Enter angle sweep step size (degrees)'))
    if launch_vel > 0 and step > 0:
        return launch_vel, step
    else:
        print('Your input value is not a valid number for this program')
        exit()

## Function to turn the step into the list of angles
def generate_angle_sweep(step):
    angles_deg = []
    current = 0
    while current <= 90:
        angles_deg.append(current)
        current += step
    return [math.radians(angle) for angle in angles_deg]

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

## Function to use the report function and cleanly print all results
def print_comparison_table(results):
    print('| Launch Angle (deg) | Flight Time (s) | Max Height (m) |   Range (m)   |')
    for result in results:
        print(f'| {math.degrees(result.launch_angle):10.2f} degrees | {result.flight_time:7.2f} seconds | {result.max_height:7.2f} meters | {result.horizontal_range:6.2f} meters |')

## Function to find the optimal angle
def find_optimal_angle(results):
    optimal = results[0]
    for result in results:
        if result.horizontal_range > optimal.horizontal_range:
            optimal = result
    return optimal

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

## Get User Input for velocity and step size and set launch angles between 0 and 90 degrees
launch_vel, step = get_user_input()
launch_angles = generate_angle_sweep(step)

## Run the simulation and print a table of the results
results = run_simulation(launch_angles, launch_vel)
print_comparison_table(results)

## Find and print the optimal launch angle
optimal = find_optimal_angle(results)
print(f'Optimal Launch Angle: {math.degrees(optimal.launch_angle):.2f} degrees, Range: {optimal.horizontal_range:2f} meters')

## Plot the 0 degrees, optimal angle, and 90 degrees, as well as the midpoints between them
### We are not printing every launch angle because the graph would be completely unreadable
midpoint1 = (0 + optimal.launch_angle)/2
midpoint2 = (optimal.launch_angle + math.radians(90))/2
plot_angles = [0, midpoint1, optimal.launch_angle, midpoint2, math.radians(90)]
plot_function(launch_vel, plot_angles)