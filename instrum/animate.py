from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt
import instrum.realisation as realisation
import instrum.vox as vox
import re

style.use('ggplot')


def diagramm(dict, width, nameY):
    plt.bar(list(dict.keys()), list(dict.values()), width=width)
    plt.ylabel(nameY)
    plt.xlabel('distance')
    plt.show()


def graphOfPointsOfDifferentColors(view):
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
                curent_color = '#' + realisation.random_color()
                match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', curent_color)
            if (view == 'line'):
                arr[itteration] = ax.plot3D(list_current_X[beginning:end], list_current_Y[beginning:end],
                                            list_current_Z[beginning:end], color=curent_color, marker=',')
            else:
                arr[itteration] = ax.scatter(list_current_X[beginning:end], list_current_Y[beginning:end],
                                             list_current_Z[beginning:end], color=curent_color)

            itteration += 1
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.title("simple 3D current photon coordinates")

    photonlist = []
    countlist = []

    for key, value in arr.items():
        photonlist.append(value)
        countlist.append(key)
    for i in range(len(countlist)):
        countlist[i] = 'photon ' + str(countlist[i] + 1)

    plt.legend(tuple(photonlist), tuple(countlist),
               loc='upper center', ncols=8, fontsize='xx-small')

    plt.show()


def voxVisualizer(array_current):
    nn = 11
    size = 20

    res = vox.voxCreate(size, array_current)

    def explode(data):
        size = np.array(data.shape)*2
        data_e = np.zeros(size - 1, dtype=data.dtype)
        data_e[::2, ::2, ::2] = data
        return data_e

    # build up the numpy logo
    n_voxels = np.zeros((nn, nn, nn), dtype=bool)

    for i in range(len(res)):
        if (res[i][3] != 0):
            n_voxels[int(res[i][0]), int(res[i][1]),
                     int(res[i][2])] = True

    facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
    edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
    filled = np.ones(n_voxels.shape)

    # upscale the above voxel image, leaving gaps
    filled_2 = explode(filled)
    fcolors_2 = explode(facecolors)
    ecolors_2 = explode(edgecolors)

    # Shrink the gaps
    x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
    # print(x,y,z)
    x[0::2, :, :] += 0.95
    y[:, 0::2, :] += 0.95
    z[:, :, 0::2] += 0.95

    # ---------
    # size of the voxels
    # x[1::2, :, :] += 0.1
    # y[:, 1::2, :] += 0.1
    # z[:, :, 1::2] += 0.1

    # print(x)
    # ---------

    # x[1::2, :, :] += 0.95
    # y[:, 1::2, :] += 0.95
    # z[:, :, 1::2] += 0.95

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlim(-5, 10)
    ax.set_ylim(-5, 10)
    ax.set_zlim(-5, 10)
    ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)

    plt.show()
