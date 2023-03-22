import random
import realistion
import animate

mu_s = 10                   # коэффициентом рассеяния
mu_a = 0.1                  # коэффициентом поглощения
size = 100                  # граница
g = 1                       # параметр анизатропии
photons = 10                # фотоны

f = open('outputs/current.txt', 'w')

for i in range(photons):
    # Действительные координаты
    current = {'x': 0, 'y': 0, 'z': 0}
    # Изменение направления фотона
    direction_of_movement = {'Yx': 0, 'Yy': 0, 'Yz': 1}
    p = 1  # Вес фотона

    while (-50 <= current['x'] < 50 and -50 <= current['y'] < 50 and -50 <= current['z'] < 10):
        # Рандомное число
        ξ = random.random()
        # Вычисление углов ϕ и θ
        [fi, teta] = realistion.corners(ξ, g)
        print(teta)
        # Вычисление свободного пробега l
        l = realistion.free_run_l(ξ, mu_s, mu_a)
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
        f.write(
            f"i:{current['i']}  x:{current['x']}  y:{current['y']}  z:{current['z']}\n")
        p = realistion.photon_weight(p, mu_s, mu_a, l)
        if (p < 0.0001):
            print('Фотон поглощен')
            break

animate.visualize()
