import math
import numpy as np
from random import randint
import random


def free_run_l(mu_s, mu_a):
    return -math.log(1 - random.random()) * (1 / (mu_s + mu_a))

def begin_corn_create():
    fi = random.random() * (2 * math.pi)
    teta = random.random() * math.pi

    cosx = math.sin(fi) * math.sin(teta)
    cosy = math.cos(fi) * math.sin(teta)
    cosz = math.cos(teta)

    return {'Yx': cosx, 'Yy': cosy, 'Yz': cosz}

def corners(g):
    fi = (math.pi * 2) * random.random()
    if (g == 0):
        teta = (2 * random.random()) - 1
    elif (g > 0):
        teta = 1 / (2 * g) * (1 + math.pow(g, 2) -
                              math.pow((1 - math.pow(g, 2)) / (1 - g + 2 * g * random.random()), 2))
    return [fi, math.acos(teta)]


def changing_the_direction_of_movement(dir, fi, teta):
    if abs(dir['Yz']) > 0.9999:
        x = math.cos(fi) * math.sin(teta)
        y = math.sin(fi) * math.sin(teta)
        z = np.sign(dir['Yz']) * math.cos(teta)

    else:
        delsqrt = (math.sin(teta)) / (math.sqrt(1 - math.pow(dir['Yz'], 2)))

        x = delsqrt * (dir['Yx'] * dir['Yz'] * math.cos(fi) - dir['Yy']
                       * math.sin(fi)) + (dir['Yx'] * math.cos(teta))

        y = delsqrt * (dir['Yy'] * dir['Yz'] * math.cos(fi) +
                       dir['Yx'] * math.sin(fi)) + (dir['Yy'] * math.cos(teta))

        z = - math.sin(teta) * math.cos(fi) * math.sqrt(1 -
                                                        math.pow(dir['Yz'], 2)) + (dir['Yz'] * math.cos(teta))

    return [x, y, z]


def photon_weight(p, mu_s, mu_a):
    return p * (mu_s / (mu_s + mu_a))


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    str = ('{:X}{:X}{:X}').format(r, g, b)
    if len(str) < 6:
        random_color()
    return ('{:X}{:X}{:X}').format(r, g, b)


def distanceBetweenPoints(current):
    return math.sqrt(math.pow((current['x'] - 0), 2) + math.pow((current['y'] - 0), 2))


def calcSquare(arr):
    sq = []
    for i in list(arr):
        sq_i = math.pi * math.pow((10 / len(arr)), 2) * ((2 * i) - 1)
        sq.append(sq_i)
    return sq
