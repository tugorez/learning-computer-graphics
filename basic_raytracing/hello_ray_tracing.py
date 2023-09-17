import math
import numpy as np

def magnitude(v):
    return math.sqrt(sum([vi * vi for vi in v]))


def normalize(v):
    m = magnitude(v)
    return v / m

def same_direction(a, b):
    na = normalize(a)
    nb = normalize(b)
    return na == nb

if __name__ == '__main__':
    a = np.array([4, 5])
    b = np.array([8, 10])
    print(same_direction(a, b))

