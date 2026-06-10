# AeroTrajectorySim V2 Algorithm

## Goal

Simulate and plot the trajectories of projectiles under gravity.

## Inputs

- Launch velocity(one value)
- Launch angles(list of many angles to test)

## Outputs

- Trajectory plot containing multiple launch angles on one graph, useful for comparison

## Algorithm
1. Take the launch angles you want to compare and store them in a list
2. Create a function that takes a launch angle and velocity as inputs, and outputs data into lists containing x, y, and time at each point that will be plotted. In the function:
    1. Set launch velocity and launch angle.
    2. Calculate horizontal and vertical velocity components.
    3. Set x position, y position, and time to 0.
    4. Create collections to store x positions, y positions, and times.
    5. Repeat:
        a. Store current position and time.
        b. Update x position.
        c. Update y position.
        d. Update vertical velocity using gravity.
        e. Advance time.
    6. Stop when y position <= 0 and time > 0.
3. Loop through this function multiple times, each time with a new angle to be tested.
4. Plot x position vs y position of all outside the loop
5. Label the graph and add a legend, then show the output graph