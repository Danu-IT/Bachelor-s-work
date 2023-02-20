import math
import numpy as np
from random import randint


def free_run_l(random, mu_s, mu_a):
    return -math.log(1 - random) * 1 / (mu_s + mu_a)


def corners(random, g):
    pi = math.pi
    ϕ = (pi * 2) * random
    if (g == 0):
        θ = (2 * random) - 1
    elif (g > 0):
        θ = 1 / (2 * g) * (1 + math.pow(g, 2) -
                           math.pow((1 - g * g) / 1 - g + 2 * g * random, 2))
    return [ϕ, math.cos(θ)]


def changing_the_direction_of_movement(dir, ϕ, θ):
    if abs(dir['Yz']) > 0.9999:
        x = math.cos(ϕ) * math.sin(θ)
        y = math.sin(ϕ) * math.sin(θ)
        z = np.sign(dir['Yz']) * math.cos(θ)

    else:
        sqrt = math.sin(θ) / math.sqrt(1 - math.pow(dir['Yz'], 2))

        x = sqrt * (dir['Yx'] * dir['Yz'] * math.cos(ϕ) - dir['Yy']
                    * math.sin(ϕ)) + (dir['Yx'] * math.cos(θ))

        y = sqrt * (dir['Yy'] * dir['Yz'] * math.cos(ϕ) +
                    dir['Yx'] * math.sin(ϕ)) + dir['Yy'] * math.cos(θ)

        z = - math.sin(θ) * math.cos(ϕ) * math.sqrt(1 -
                                                    math.pow(dir['Yz'], 2)) + (dir['Yz'] * math.cos(θ))

    return [abs(x), abs(y), z]


def photon_weight(p, mu_s, mu_a):
    return p * mu_s / (mu_s + mu_a)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    str = ('{:X}{:X}{:X}').format(r, g, b)
    if len(str) < 6:
        random_color()
    return ('{:X}{:X}{:X}').format(r, g, b)

    # def snells_low(new_ai, new_at, new_n1, new_n2):
    #     self.ai = new_ai    # theta_1
    #     self.at = new_at    # theta_2
    #     self.n1 = new_n1    # n1
    #     self.n2 = new_n2    # n2
    #     new_ai_rad = np.radians(new_ai)
    #     new_at_rad = np.arcsin(new_n1 / new_n2 * np.sin(new_ai_rad))
    #     new_at = np.degrees(new_at_rad)
    #     self.at = new_at
    #     return self.at
