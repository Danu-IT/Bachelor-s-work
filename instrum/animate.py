from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt
import instrum.realisation as realisation
import instrum.vox as vox
import re

style.use("ggplot")


def diagramm(arr, width, nameY):
    key = []
    for i in range(len(arr)):
        key.append((i * 10) / 100)
    plt.bar(key, arr, width=width)
    plt.ylabel(nameY)
    plt.xlabel("distance")
    plt.show()


def lineGraph(arr, root):
    x_arr = []

    with open(root) as f:
        for line in f:
            x_arr.append(line[2 : len(line) - 2].split(","))

    x_arr_number = [[float(i) for i in row] for row in x_arr]

    key = []
    for i in range(len(arr)):
        key.append((i * 10) / 100)

    x_0 = x_arr[0][5]
    x_1 = x_arr[1][5]
    x_2 = x_arr[2][5]

    print(x_0, x_1, x_2)

    plt.plot(key, x_arr_number[0])
    plt.plot(key, x_arr_number[1])
    plt.plot(key, x_arr_number[2])
    plt.ylabel("square")
    plt.xlabel("distance")
    plt.show()


def lineGraphHard():
    plt.plot([10, 20, 30], [12.239905800253629, 25.99889625815505, 29.37343204913785])
    plt.plot([10, 20, 30], [12.123457131490587, 22.803239683236825, 24.99190295951493])
    plt.plot([10, 20, 30], [9.848026506005528, 19.154892232217954, 22.349918492063058])
    plt.ylabel("сигнал одр, отн ед")
    plt.xlabel("mus")
    plt.show()


def lineGraphHardInom():
    x_arr = []

    with open("outputs/cross-section.txt") as f:
        for line in f:
            x_arr.append(line[2 : len(line)].split(","))

    x_arr_number = [[float(i) for i in row] for row in x_arr]
    plt.plot(x_arr_number[0])
    plt.plot(x_arr_number[1])
    plt.plot(x_arr_number[2])
    plt.ylabel("weight")
    plt.xlabel("size")
    plt.show()


def graphOfPointsOfDifferentColors(root, view):
    list_current_X = []
    list_current_Y = []
    list_current_Z = []
    list_current_I = []

    with open(root) as f:
        for line in f:
            current_line = {}
            line = line.split()
            current_line["i"] = line[0].split(":")[1]
            current_line["x"] = line[1].split(":")[1]
            current_line["y"] = line[2].split(":")[1]
            current_line["z"] = line[3].split(":")[1]

            list_current_X.append(float(current_line["x"]))
            list_current_Y.append(float(current_line["y"]))
            list_current_Z.append(float(current_line["z"]))
            list_current_I.append(int(current_line["i"]))

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection="3d")

    arr = {}
    itteration = 0

    for i in range(len(list_current_I)):
        if int(list_current_I[i]) >= itteration and itteration + 1 != int(
            list_current_I[-1]
        ):
            beginning = list_current_I.index(itteration + 1)
            end = list_current_I.index(itteration + 2)

            match = False
            while not match:
                curent_color = "#" + realisation.random_color()
                match = re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", curent_color)
            if view == "line":
                arr[itteration] = ax.plot3D(
                    list_current_X[beginning:end],
                    list_current_Y[beginning:end],
                    list_current_Z[beginning:end],
                    color=curent_color,
                    marker=",",
                )
            else:
                arr[itteration] = ax.scatter(
                    list_current_X[beginning:end],
                    list_current_Y[beginning:end],
                    list_current_Z[beginning:end],
                    color=curent_color,
                )

            itteration += 1
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    ax.set_zlabel("Z Label")

    plt.title("simple 3D current photon coordinates")

    photonlist = []
    countlist = []

    for key, value in arr.items():
        photonlist.append(value)
        countlist.append(key)
    for i in range(len(countlist)):
        countlist[i] = "photon " + str(countlist[i] + 1)

    print(photonlist)
    plt.legend(
        tuple(photonlist),
        tuple(countlist),
        loc="upper center",
        ncols=8,
        fontsize="xx-small",
    )

    plt.show()
