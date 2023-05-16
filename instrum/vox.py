import math
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
import time
from matplotlib.animation import FuncAnimation


def coordinatesCartesian(size):
    array_voxel = []
    for x in range(size):  # Массив координат
        for y in range(size):
            for z in range(size):
                array_voxel.append([x - size / 2, y - size / 2, z, 0])
    return array_voxel


# def twoDimensionalSystem(size, slice):
#     array_voxel = []
#     for x in range(size):  # Массив координат
#         for y in range(size):
#             array_voxel.append([x - size / 2, y - size / 2, slice, 0])
#     return array_voxel


# def sliceArray(size, res):
#     list = [[] for _ in range(size)]
#     maks = 0
#     for i in range(len(list)):
#         for j in range(len(res)):
#             index = res[j][1] + size / 2
#             if (i == int(index)):
#                 if (maks < res[j][3]):
#                     maks = res[j][3]
#                 list[i].append(res[j][3])
#     return [list, maks]


# def voxCreate(array_current, array_voxel):
#     program_starts = time.time()
#     for i in range(len(array_current)):
#         for j in range(len(array_voxel)):
#             if (array_current[i]['x'] == array_voxel[j][0] and
#                array_current[i]['y'] == array_voxel[j][1]):
#                 array_voxel[j][3] += array_current[i]['w']

#     now = time.time()
#     print("It has been {0} seconds since the loop started".format(
#         now - program_starts))

#     return array_voxel


def voxVisualizer(maks, array_current, param):
    viridis = cm.get_cmap('viridis', 256)
    newcolors = viridis(np.linspace(0, 1, 256))
    pink = np.array([248/256, 24/256, 148/256, 0])

    newcolors[:25, :] = pink
    newcmp = ListedColormap(newcolors)

    def plot_examples(cms):
        """
        helper function to plot two colormaps
        """
        np.random.seed(19680801)
        data = array_current

        log = cm.scale.get_scale_names()[0]
        #print(log)
        fig, axs = plt.subplots(1, 2, figsize=(
            18, 9), constrained_layout=True)
        for [ax, cmap] in zip(axs, cms):
            psm = ax.pcolormesh(
                data, cmap=cmap, rasterized=True,
                norm=log, )
            fig.colorbar(psm, ax=ax)
        #plt.xlim(-100, 100)
        plt.show()

    plot_examples([viridis, newcmp])


# def voxVisualizerCub(size, array_current):
#     nn = 11
#     array_voxel = coordinatesСartesian(size)
#     res = voxCreate(array_current, array_voxel)

#     def explode(data):
#         size = np.array(data.shape)*2
#         data_e = np.zeros(size - 1, dtype=data.dtype)
#         data_e[::2, ::2, ::2] = data
#         return data_e

#     # build up the numpy logo
#     n_voxels = np.zeros((nn, nn, nn), dtype=bool)

#     for i in range(len(res)):
#         if (res[i][3] != 0):
#             n_voxels[int(res[i][0]), int(res[i][1]),
#                      int(res[i][2])] = True

#     facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
#     edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
#     filled = np.ones(n_voxels.shape)

#     # upscale the above voxel image, leaving gaps
#     filled_2 = explode(filled)
#     fcolors_2 = explode(facecolors)
#     ecolors_2 = explode(edgecolors)

#     # Shrink the gaps
#     x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
#     # print(x,y,z)
#     x[0::2, :, :] += 0.95
#     y[:, 0::2, :] += 0.95
#     z[:, :, 0::2] += 0.95

#     # ---------
#     # size of the voxels
#     # x[1::2, :, :] += 0.1
#     # y[:, 1::2, :] += 0.1
#     # z[:, :, 1::2] += 0.1

#     # print(x)
#     # ---------

#     # x[1::2, :, :] += 0.95
#     # y[:, 1::2, :] += 0.95
#     # z[:, :, 1::2] += 0.95

#     fig = plt.figure()
#     ax = fig.add_subplot(projection='3d')
#     # ax.set_xlim(-5, 10)
#     # ax.set_ylim(-5, 10)
#     # ax.set_zlim(-5, 10)
#     ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)

#     plt.show()

