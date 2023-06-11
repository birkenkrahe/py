import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frameNum, img, grid, N):
    # Copy grid to apply rules
    newGrid = grid.copy()

    # Loop through each cell in the grid
    for i in range(N):
        for j in range(N):
            # Compute the sum of the eight neighbors
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]) / 255)

            # Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    # Update the data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# Grid size and animation frames
N = 100
ON = 255
OFF = 0
vals = [ON, OFF]

# Populate grid with random on/off states
grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

# Create the figure and axis objects
fig, ax = plt.subplots()

# Display the grid as an image
img = ax.imshow(grid, interpolation='nearest')

# Animate
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                              frames=10, interval=50, save_count=50)

# Display
plt.show()
