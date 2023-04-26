import instrum.realisation as realisation
import instrum.animate as animate
import instrum.vox as vox
import instrum.animation as animation
from concurrent.futures import ProcessPoolExecutor
import math

mu_s = 10                   # коэффициентом рассеяния
mu_a = 0.05                 # коэффициентом поглощения
g = 0.99                   # параметр анизатропии
photons = 10000              # фотоны
size = 100                  # граница
left = - (size / 2)
right = (size / 2)
x_max = 10

array_current = []          # массив координат
slice = 5
sliceThinkness = 0.5
a = 100

# masY = [0] * a
# maksY = 0
# for i in range(a):
#     masY[i] = [0] * (a * 2)

# masZ = [0] * a
# maksZ = 0
# for i in range(a):
#     masZ[i] = [0] * (a * 2)

w_arr = []
for i in range(100):
    w_arr.append(0)

f = open('outputs/current.txt', 'w')
diff = open('outputs/different_g.txt', 'a')

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

        # if i == 20:
        #     diff.write(
        #         f"i:{4}  x:{current['x']}  y:{current['y']}  z:{current['z']}\n")

        # if (current['y'] > -sliceThinkness and current['y'] < sliceThinkness and abs(current['x']) < x_max and abs(current['z']) < x_max and (current['z']) > 0):
        #     indeks1 = math.floor(((current['x'] - 10) / x_max) * 100)
        #     indeks2 = math.floor((current['z'] / x_max) * 100)
        #     masY[indeks2][indeks1] += w
        #     if (maksY < masY[indeks2][indeks1]):
        #         maksY = masY[indeks2][indeks1]

        # if (current['z'] > -sliceThinkness and current['z'] < sliceThinkness and abs(current['x']) < x_max and abs(current['y']) < x_max):
        #     indeks1 = math.floor(((current['x'] - 10) / x_max) * 100)
        #     indeks2 = math.floor(((current['y'] - 10) / x_max) * 50)
        #     masZ[indeks2][indeks1] += w
        #     if (maksZ < masZ[indeks2][indeks1]):
        #         maksZ = masZ[indeks2][indeks1]

        if (i <= 50):
            f.write(
                f"i:{current['i']}  x:{current['x']}  y:{current['y']}  z:{current['z']}\n")

        w = realisation.photon_weight(w, mu_s, mu_a)
        if (w < 0.0001):
            # print('Фотон поглощен')
            break

        if (current['z'] < 0):
            answer = math.floor(
                realisation.distanceBetweenPoints(current) / x_max * 100)
            if (answer < 100):
                w_arr[answer] += w
            break
# График передвижения фотона в среде по точкам
# animate.graphOfPointsOfDifferentColors('outputs/current.txt', 'point')
# График передвижения фотона в среде линиями
animate.graphOfPointsOfDifferentColors('outputs/current.txt', 'line')
animate.graphOfPointsOfDifferentColors('outputs/different_g.txt', 'line')
# Гистограмма кол-во фотонов к расстоянию
animate.diagramm(w_arr, 0.1, 'count')
# Гистограмма площадь кольца к расстоянию
seq = realisation.calcSquare(w_arr)
animate.diagramm(seq, 0.1, 'square')

# vox.voxVisualizerCub(size, array_current)
# vox.voxVisualizer(maksZ, masZ, 'z')
# vox.voxVisualizer(maksY, masY, 'y')
