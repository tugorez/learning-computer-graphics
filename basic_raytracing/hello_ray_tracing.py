import math
import numpy as np
import matplotlib.pyplot as plt
import random


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color

VIEWPORT_DISTANCE = 1

VIEWPORT = (64, 64)

CANVAS = (VIEWPORT[0] + 1, VIEWPORT[1] + 1)

# Just dots atm
SCENE = [
    [[i, -i, 1], random_color()] for i in range(-32, 33)
] + [
    [[i, i, 1], random_color()] for i in range(-32, 33)
] + [
    [[0, i, 1], random_color()] for i in range(-32, 33)
] + [
    [[i, 0, 1], random_color()] for i in range(-32, 33)
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
        dot_coord = dot[0]
        dot_color = dot[1]
        if same_direction(dot_coord, v):
            return dot_color
    return (0, 0, 0)

if __name__ == '__main__':
    canvas = np.zeros(CANVAS + (3,))
    for i in range(CANVAS[0]):
        for j in range(CANVAS[1]):
            color = get_color((i, j))
            canvas[i][j] = color
    plt.imshow(canvas.astype("uint8"), vmin = 0, vmax = 255, interpolation = 'None')
    plt.show()
