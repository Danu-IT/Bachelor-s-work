import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
import time


def voxCreate(size, array_current):
    array_voxel = []

    for x in range(size):  # Массив координат
        for y in range(size):
            for z in range(size):
                array_voxel.append([x - size / 2, y - size / 2, z, 0])
    program_starts = time.time()
    for i in range(len(array_current)):
        for j in range(len(array_voxel)):
            if (array_current[i]['x'] == array_voxel[j][0] and
               array_current[i]['y'] == array_voxel[j][1] and
               array_current[i]['z'] == array_voxel[j][2]):
                array_voxel[j][3] += array_current[i]['w']

    now = time.time()
    print("It has been {0} seconds since the loop started".format(
        now - program_starts))

    del array_voxel[len(array_voxel) - 1]

    return array_voxel


def sliceArray(size, res):
    arr = []
    list = [[] for _ in range(size)]

    for i in range(len(res)):
        if (res[i][2] == size / 2):
            arr.append(res[i])

    for i in range(len(list)):
        for j in range(len(arr)):
            index = arr[j][1] + size / 2
            if (i == int(index)):
                list[i].append(arr[j][3])

    return list


def voxVisualizer(size, array_current):
    viridis = cm.get_cmap('viridis', 12)
    res = voxCreate(size, array_current)

    cross_section = sliceArray(size, res)

    viridis = cm.get_cmap('viridis', 256)
    newcolors = viridis(np.linspace(0, 1, 256))
    pink = np.array([248/256, 24/256, 148/256, 1])

    newcolors[:25, :] = pink
    newcmp = ListedColormap(newcolors)

    def plot_examples(cms):
        """
        helper function to plot two colormaps
        """
        np.random.seed(19680801)
        data = cross_section
        fig, axs = plt.subplots(1, 2, figsize=(18, 9), constrained_layout=True)
        for [ax, cmap] in zip(axs, cms):
            psm = ax.pcolormesh(
                data, cmap=cmap, rasterized=True, vmin=0, vmax=10)
            fig.colorbar(psm, ax=ax)
        plt.show()

    plot_examples([viridis, newcmp])
