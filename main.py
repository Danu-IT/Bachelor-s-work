import random
import realistion
import animate

mu_s = 10                   # коэффициентом рассеяния
mu_a = 0.1                  # коэффициентом поглощения
size = 100                  # граница
g = 0.8                     # параметр анизатропии
photons = 100              # фотоны

f = open('outputs/current.txt', 'w')

left = - (size / 2)
right = (size / 2)

distances = []

for i in range(photons):
    array_current = []
    # Действительные координаты
    current = {'x': 0, 'y': 0, 'z': 0}
    # Изменение направления фотона
    direction_of_movement = {'Yx': 0, 'Yy': 0, 'Yz': 1}
    p = 1  # Вес фотона

    while (left <= current['x'] < right and left <= current['y'] < right and -1 <= current['z'] < 10):
        # Вычисление углов ϕ и θ
        [fi, teta] = realistion.corners(g)
        # Вычисление свободного пробега l
        l = realistion.free_run_l(mu_s, mu_a)
        # Изменение направления движения
        [x, y, z] = realistion.changing_the_direction_of_movement(
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

        p = realistion.photon_weight(p, mu_s, mu_a, l)
        if (p < 0.0001):
            print('Фотон поглощен')
            break
        if (current['z'] < 0):
            # print('z -', current['z'], 'x -',
            #       current['x'], 'y -', current['y'])
            # if (array_current):
            #     print(array_current[-1])
            answer = realistion.distanceBetweenPoints(current)
            distances.append(answer)
            break

        array_current.append(
            {'x': current['x'], 'y': current['y'], 'z': current['z']})

animate.graphOfPointsOfDifferentColors('point')
animate.graphOfPointsOfDifferentColors('line')
animate.diagramm(distances)
