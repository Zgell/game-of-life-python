import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
import matplotlib.animation as animation
from random import randint
from math import floor, sqrt

def createMatrix(size):
    return np.random.choice([0, 1], size*size, p=[0.9, 0.1]).reshape(size, size)

def createGlider(x, y, mat, dir = 'se'):
    glider = np.array([[0, 0, 1],
                        [1, 0, 1],
                        [0, 1, 1]])
    if (dir == 'ne'):
        glider = np.flipud(glider)
    elif (dir == 'sw'):
        glider = np.fliplr(glider)
    elif (dir == 'nw'):
        glider = np.fliplr(np.flipud(glider))
    mat[x:x+3, y:y+3] = glider

def createPulsar(x, y, mat):
    pulsar = np.array([[0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]])
    mat[x:x+13, y:y+13] = pulsar

def createRPent(x, y, mat):
    rpent = np.array([[0, 1, 1],
                    [1, 1, 0],
                    [0, 1, 0]])
    mat[x:x+3, y:y+3] = rpent

def update(i, mat, matsize):
    # Update stuff
    newmat = mat.copy()
    for y in range(matsize):
        for x in range(matsize):
            cell_sum = 0
            # Corner Checks
            if (x > 0 and y > 0): #If not in top-left corner
                cell_sum += floor(mat[y-1][x-1])
            if (x < (matsize - 1) and y > 0): #If not in top-right corner
                cell_sum += floor(mat[y-1][x+1])
            if (x < (matsize - 1) and y < (matsize - 1)): #If not in bottom-right corner
                cell_sum += floor(mat[y+1][x+1])
            if (x > 0 and y < (matsize - 1)):
                cell_sum += floor(mat[y+1][x-1])
            if (x > 0):
                cell_sum += floor(mat[y][x-1])
            if (x < (matsize - 1)):
                cell_sum += floor(mat[y][x+1])
            if (y > 0):
                cell_sum += floor(mat[y-1][x])
            if (y < (matsize - 1)):
                cell_sum += floor(mat[y+1][x])

            if (mat[y][x] == 1) and (cell_sum < 2 or cell_sum > 3):
                newmat[y][x] = 0
            elif (mat[y][x] < 1) and (cell_sum == 3):
                newmat[y][x] = 1
            elif (mat[y][x] == 1) and (cell_sum == 2 or cell_sum == 3):
                newmat[y][x] = 1

    matrix.set_data(newmat)
    mat[:] = newmat[:]
    return matrix,

matsize = 100
mat = createMatrix(matsize)
#mat = np.zeros((matsize, matsize))
#createRPent(40, 40, mat)

fig, ax = plt.subplots(figsize = (8, 8))
fig.suptitle("John Conway's Game of Life", fontsize = 20)
fig.canvas.set_window_title('Game of Life')
matrix = ax.matshow(mat, cmap = plt.get_cmap('gray'), vmin = 0, vmax = 1)

ani = animation.FuncAnimation(fig, update, fargs = (mat, matsize,), interval = 50)
plt.show()