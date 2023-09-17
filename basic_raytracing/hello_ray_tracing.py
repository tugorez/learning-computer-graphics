import math
import numpy as np
import matplotlib.pyplot as plt

VIEWPORT_DISTANCE = 1

VIEWPORT = (64, 64)

CANVAS = (VIEWPORT[0] + 1, VIEWPORT[1] + 1)

# Just dots atm
SCENE = [
    [-i, 0, 1] for i in range(32)
]

def magnitude(v):
    return math.sqrt(sum([vi * vi for vi in v]))

def normalize(v):
    m = magnitude(v)
    return v / m

def same_direction(a, b):
    a = np.array(a)
    b = np.array(b)
    na = normalize(a)
    nb = normalize(b)
    e = ((na - nb) ** 2).sum()
    return e <= 0.0001

def get_color(canvas): 
    i, j = canvas
    # change the coordinates system :")
    cx = j - VIEWPORT[0] / 2
    cy = VIEWPORT[1] / 2 - i
    # compute the viewport point
    vx = cx * VIEWPORT[0] / CANVAS[0]
    vy = cy * VIEWPORT[1] / CANVAS[1]
    vz = VIEWPORT_DISTANCE
    v = (vx, vy, vz)

    for dot in SCENE:
        if same_direction(dot, v):
            return (0, 255, 0)
    return (0, 0, 0)

if __name__ == '__main__':
    canvas = np.zeros(CANVAS + (3,))
    for i in range(CANVAS[0]):
        for j in range(CANVAS[1]):
            color = get_color((i, j))
            canvas[i][j] = color
    plt.imshow(canvas, vmin = 0, vmax = 255, interpolation = None)
    plt.show()
