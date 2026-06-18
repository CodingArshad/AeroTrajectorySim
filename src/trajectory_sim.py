import math
import matplotlib.pyplot as plt

# Set initial conditions
launch_vel = 10
launch_angles = [math.radians(angle) for angle in [30, 45, 60]]
g = 9.81
dt = 0.1

# Results storage
angles = []
flight_times = []
max_heights = []
ranges = []

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

# Simulate trajectory for each launch angle
for i in range(len(launch_angles)):
    # Set initial conditions for the current launch angle
    x, y, times = simulate_trajectory(launch_vel, launch_angles[i])

    # Calculate results
    angle = math.degrees(launch_angles[i])
    max_height = max(y)
    flight_time = times[-1]
    horizontal_range = x[-1]

    # Store results
    angles.append(angle)
    flight_times.append(flight_time)
    max_heights.append(max_height)
    ranges.append(horizontal_range)

    # Store trajectory for plotting
    plt.plot(x, y, label='{:.2f} degrees'.format(math.degrees(launch_angles[i])))

# Plot trajectory
plt.title('Trajectory Graph')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.legend()
plt.show()

# Print results
print("Launch Angle (degrees) | Flight Time (s) | Max Height (m) | Range (m) |")
for i in range(len(angles)):
    print(f"{angles[i]:22.2f} | {flight_times[i]:15.2f} | {max_heights[i]:14.2f} | {ranges[i]:9.2f} |")
