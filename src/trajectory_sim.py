import math
import matplotlib.pyplot as plt

# Set initial conditions
launch_vel = 10
launch_angle = 45
angle_rad = math.radians(launch_angle)
g = 9.81

x_vel = launch_vel * math.cos(angle_rad)
y_vel = launch_vel * math.sin(angle_rad)

x_pos = 0
y_pos = 0
dt = 0.1
time = 0

# Lists to store trajectory points
x = []
y = []
times = []

# Simulate trajectory
while y_pos >= 0:
    x.append(x_pos)
    y.append(y_pos)
    times.append(time)

    x_pos += x_vel * dt
    y_pos += y_vel * dt
    y_vel -= g * dt
    time += dt

    if y_pos <= 0 and time > 0:
        break

# Plot trajectory
plt.plot(x, y, color='red')
plt.title('Trajectory Graph')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.show()