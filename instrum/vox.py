import math


def voxCreate(size, array_current):
    array_voxel = []

    for x in range(size):  # Массив координат
        for y in range(size):
            for z in range(size):
                array_voxel.append([x - size / 2, y - size / 2, z, 0])

    for i in range(len(array_voxel)):
        for f in range(len(array_current)):
            if (math.floor(array_current[f]['x']) == array_voxel[i][0] and
                math.floor(array_current[f]['y']) == array_voxel[i][1] and
                    math.floor(array_current[f]['z']) == array_voxel[i][2]):
                array_voxel[i][3] += array_current[f]['w']

    del array_voxel[len(array_voxel) - 1]

    return array_voxel
