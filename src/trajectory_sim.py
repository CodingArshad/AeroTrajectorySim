import math
import matplotlib.pyplot as plt
from dataclasses import dataclass

# Set initial conditions
g = 9.81
dt = 0.1
Cd = 0.47
Area = 0.00785
rho = 1.225
mass = 0.1
k = (Cd * rho * Area) / (2 * mass)

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

## Function to apply drag to simulation
def simulate_trajectory_drag(launch_vel, launch_angle):
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

        speed = math.sqrt((x_vel ** 2) + (y_vel ** 2))

        drag_decel = k * speed ** 2

        x_vel -= (drag_decel * x_vel / speed) * dt
        y_vel -= (drag_decel * y_vel / speed) * dt

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

## Function to cleanly return the flight statistics with no drag
def get_flight_stats(launch_vel, launch_angle):
    x, y, times = simulate_trajectory(launch_vel, launch_angle)
    return FlightStats(launch_angle=launch_angle, flight_time=times[-1], max_height=max(y), horizontal_range=x[-1])

## Function to cleanly return the flight statistics with drag applied
def get_flight_stats_drag(launch_vel, launch_angle):
    x, y, times = simulate_trajectory_drag(launch_vel, launch_angle)
    return FlightStats(launch_angle=launch_angle, flight_time=times[-1], max_height=max(y), horizontal_range=x[-1])

## Function to use the report function and cleanly print all results(with and without drag)
def print_comparison_table(results, title):
    print(title + '\n')
    print('| Launch Angle (deg) | Flight Time (s) | Max Height (m) |   Range (m)   |')
    print('|-----------------------------------------------------------------------|')
    for result in results:
        print(f'| {math.degrees(result.launch_angle):10.2f} degrees | {result.flight_time:7.2f} seconds | {result.max_height:7.2f} meters | {result.horizontal_range:6.2f} meters |')
    print('-------------------------------------------------------------------------\n')

## Function to find the optimal angle
def find_optimal_angle(results):
    optimal = results[0]
    for result in results:
        if result.horizontal_range > optimal.horizontal_range:
            optimal = result
    return optimal

## Function to run the simulation with no drag
def run_simulation(angles, launch_vel):
    results = []
    for angle in angles:
        stat = get_flight_stats(launch_vel, angle)
        results.append(stat)
    return results

## Function to run the simulation with drag applied
def run_simulation_drag(angles, launch_vel):
    results = []
    for angle in angles:
        stat = get_flight_stats_drag(launch_vel, angle)
        results.append(stat)
    return results

# Function to plot the trajectory for each launch angle
def plot_comparison(launch_vel, launch_angles):
    for i in range(len(launch_angles)):
        x_no_drag, y_no_drag, _ = simulate_trajectory(launch_vel, launch_angles[i])
        x_drag, y_drag, _ = simulate_trajectory_drag(launch_vel, launch_angles[i])

        # Store trajectory for plotting
        plt.plot(x_no_drag, y_no_drag, label='No Drag: {:.2f} degrees'.format(math.degrees(launch_angles[i])))
        plt.plot(x_drag, y_drag, label='Drag: {:.2f} degrees'.format(math.degrees(launch_angles[i])))

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
results_no_drag = run_simulation(launch_angles, launch_vel)
results_drag = run_simulation_drag(launch_angles, launch_vel)
print_comparison_table(results_no_drag, 'No Drag Results:')
print_comparison_table(results_drag, 'Drag Results:')

## Find and print the optimal launch angle
optimal_no_drag = find_optimal_angle(results_no_drag)
optimal_drag = find_optimal_angle(results_drag)

print(f'Optimal Launch Angle without Drag: {math.degrees(optimal_no_drag.launch_angle):.2f} degrees, Range: {optimal_no_drag.horizontal_range:2f} meters')
print(f'Optimal Launch Angle with Drag: {math.degrees(optimal_drag.launch_angle):.2f} degrees, Range: {optimal_drag.horizontal_range:2f} meters')

## Plot optimal angle with and without drag
### We are not printing every launch angle because the graph would be unreadable
plot_angles = [optimal_no_drag.launch_angle, optimal_drag.launch_angle]
plot_comparison(launch_vel, plot_angles)