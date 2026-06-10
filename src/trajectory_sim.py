import math
import matplotlib.pyplot as plt

# Set initial conditions
launch_vel = 10
launch_angles = [math.radians(angle) for angle in [20, 45, 65, 90, 130]]
g = 9.81

def simulate_trajectory(launch_vel, launch_angle):
    # Constants
    x_pos = 0
    y_pos = 0
    dt = 0.1
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
    x, y, times = simulate_trajectory(launch_vel, launch_angles[i])
    plt.plot(x, y, label='{:.2f} degrees'.format(math.degrees(launch_angles[i])))
# Plot trajectory
plt.title('Trajectory Graph')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.legend()
plt.show()