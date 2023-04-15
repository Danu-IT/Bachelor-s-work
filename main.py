import random
import instrum.realisation as realisation
import instrum.animate as animate
import instrum.vox as vox
import instrum.animation as animation
from concurrent.futures import ProcessPoolExecutor
import math

mu_s = 10                   # коэффициентом рассеяния
mu_a = 0.15                 # коэффициентом поглощения
g = 1                     # параметр анизатропии

size = 100                   # граница
photons = 2              # фотоны
array_current = []          # массив координат
# slice =

f = open('outputs/current.txt', 'w')

left = - (size / 2)
right = (size / 2)

distances = []

for i in range(photons):
    # Действительные координаты
    current = {'x': 4, 'y': 0, 'z': 0}
    # Изменение направления фотона
    direction_of_movement = {'Yx': 0, 'Yy': 0, 'Yz': 1}
    w = 1  # Вес фотона

    while (left <= current['x'] < right and left <= current['y'] < right and -1 <= current['z'] < 10):
        # Вычисление углов ϕ и θ
        [fi, teta] = realisation.corners(g)
        # Вычисление свободного пробега l
        l = realisation.free_run_l(mu_s, mu_a)
        # Изменение направления движения
        [x, y, z] = realisation.changing_the_direction_of_movement(
            direction_of_movement, fi, teta)

        direction_of_movement['Yx'] = x
        direction_of_movement['Yy'] = y
        direction_of_movement['Yz'] = z

        current['x'] = current['x'] + (l * direction_of_movement['Yx'])
        current['y'] = current['y'] + (l * direction_of_movement['Yy'])
        current['z'] = current['z'] + (l * direction_of_movement['Yz'])
        current['i'] = i + 1
        if (i <= 50):
            f.write(
                f"i:{current['i']}  x:{current['x']}  y:{current['y']}  z:{current['z']}\n")

        w = realisation.photon_weight(w, mu_s, mu_a)
        if (w < 0.0001):
            # print('Фотон поглощен')
            break

        if (current['z'] < 0):
            answer = round(realisation.distanceBetweenPoints(current), 1)
            distances.append(answer)
            break

        array_current.append(
            {'x': math.floor(current['x']), 'y': math.floor(current['y']), 'z': math.floor(current['z']), 'w': w})

# График передвижения фотона в среде по точкам
# animate.graphOfPointsOfDifferentColors('point')
# График передвижения фотона в среде линиями
# animate.graphOfPointsOfDifferentColors('line')
# Гистограмма кол-во фотонов к расстоянию
# rez = realisation.createDict(distances)
# animate.diagramm(rez, 0.1, 'count')
# Гистограмма площадь кольца к расстоянию
# seq = realisation.calcSquare(rez)
# animate.diagramm(seq, 0.1, 'square')

# animate.voxVisualizerCub(array_current)
vox.voxVisualizer(size, array_current)
