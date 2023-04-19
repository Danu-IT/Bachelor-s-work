import random
import instrum.realisation as realisation
import instrum.animate as animate
import instrum.vox as vox
import instrum.animation as animation
from concurrent.futures import ProcessPoolExecutor
import math

mu_s = 10                   # коэффициентом рассеяния
mu_a = 0.15                 # коэффициентом поглощения
g = 0.8                     # параметр анизатропии
photons = 1000
size = 100                   # граница          # фотоны

array_current = []          # массив координат
slice = 5
sliceThinkness = 0.5
f = open('outputs/current.txt', 'w')

left = - (size / 2)
right = (size / 2)

a = 100
mas = [0] * a
maks = 0
for i in range(a):
    mas[i] = [0] * (a * 2)
# arr = []
# for i in range(100):
#     arr.append(0)

for i in range(photons):
    # Действительные координаты
    current = {'x': 0, 'y': 0, 'z': 0}
    # Изменение направления фотона
    direction_of_movement = {'Yx': 0, 'Yy': 0, 'Yz': 1}
    w = 1  # Вес фотона

    while (left <= current['x'] < right and left <= current['y'] < right and -1 <= current['z'] < 100):
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

        if (current['y'] > -sliceThinkness and current['y'] < sliceThinkness and abs(current['x']) < 10 and abs(current['z']) < 10 and (current['z']) > 0):
            indeks1 = math.floor(((current['x']-10) / 10) * 100)
            indeks2 = math.floor((current['z'] / 10) * 100)
            mas[indeks2][indeks1] += w
            if (maks < mas[indeks2][indeks1]):
                maks = mas[indeks2][indeks1]

        if (i <= 50):
            f.write(
                f"i:{current['i']}  x:{current['x']}  y:{current['y']}  z:{current['z']}\n")

        w = realisation.photon_weight(w, mu_s, mu_a)
        if (w < 0.000001):
            # print('Фотон поглощен')
            break

        # if (current['z'] < 0):
        #     answer = math.floor(
        #         realisation.distanceBetweenPoints(current) / 10 * 100)
        #     if (answer < 100):
        #         arr[answer] += w
        #     break
        # if (math.floor(current['z']) == slice):
        #     array_current.append(
        #         {'x': math.floor(current['x']), 'y': math.floor(current['y']), 'z': math.floor(current['z']), 'w': w})
# График передвижения фотона в среде по точкам
# animate.graphOfPointsOfDifferentColors('point')
# График передвижения фотона в среде линиями
# animate.graphOfPointsOfDifferentColors('line')
# Гистограмма кол-во фотонов к расстоянию
# animate.diagramm(arr, 0.1, 'count')
# Гистограмма площадь кольца к расстоянию
# seq = realisation.calcSquare(arr)
# animate.diagramm(seq, 0.1, 'square')

# vox.voxVisualizerCub(size, array_current)
vox.voxVisualizer(maks, mas)
