from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt
import realistion
import re

style.use('ggplot')


def visualize():
    list_current_X = []
    list_current_Y = []
    list_current_Z = []
    list_current_I = []

    with open("outputs/current.txt") as f:
        for line in f:
            current_line = {}
            line = line.split()
            current_line['i'] = line[0].split(':')[1]
            current_line['x'] = line[1].split(':')[1]
            current_line['y'] = line[2].split(':')[1]
            current_line['z'] = line[3].split(':')[1]

            list_current_X.append(float(current_line['x']))
            list_current_Y.append(float(current_line['y']))
            list_current_Z.append(float(current_line['z']))
            list_current_I.append(int(current_line['i']))

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection='3d')

    arr = {}
    itteration = 0

    for i in range(len(list_current_I)):
        if int(list_current_I[i]) >= itteration and itteration + 1 != int(list_current_I[-1]):
            beginning = list_current_I.index(itteration + 1)
            end = list_current_I.index(itteration + 2)

            match = False
            while not match:
                curent_color = '#' + realistion.random_color()
                match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', curent_color)

            arr[itteration] = ax.scatter(list_current_X[beginning:end], list_current_Y[beginning:end],
                                         list_current_Z[beginning:end], color=curent_color, marker='o')
            itteration += 1

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    plt.title("simple 3D current photon coordinates")

    photonlist = []
    countlist = []

    for key, value in arr.items():
        photonlist.append(value)
        countlist.append(key)

    for i in range(len(countlist)):
        countlist[i] = 'photon ' + str(countlist[i] + 1)

    plt.legend(tuple(photonlist), tuple(countlist), loc='upper right')

    plt.show()
