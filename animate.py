from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt
import realistion

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

    print(list_current_I)
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d')

    current_color = '#' + realistion.random_color()

    ax.scatter(list_current_X, list_current_Y,
               list_current_Z, c=current_color, marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')

    plt.show()
