import random
import realistion
import animate

mu_s = 1                  # коэффициентом рассеяния
mu_a = 0.1                # коэффициентом поглощения
size = 50                 # граница
g = 1                     # параметр анизатропии
photons = 10              # фотоны

f = open('outputs/current.txt', 'w')

for i in range(photons):
    # Действительные координаты
    current = {'x': 0, 'y': 0, 'z': 0}
    # Изменение направления фотона
    direction_of_movement = {'Yx': 0, 'Yy': 0, 'Yz': 1}
    p = 1  # Вес фотона

    while (0 <= current['x'] < size and 0 <= current['y'] < size and 0 <= current['z'] < size):
        # Рандомное число
        ξ = random.random()
        # Вычисление углов ϕ и θ
        [ϕ, θ] = realistion.corners(ξ, g)
        # Вычисление свободного пробега l
        l = realistion.free_run_l(ξ, mu_s, mu_a)

        [x, y, z] = realistion.changing_the_direction_of_movement(
            direction_of_movement, ϕ, θ)

        direction_of_movement['Yx'] = x
        direction_of_movement['Yy'] = y
        direction_of_movement['Yz'] = z

        current['x'] = current['x'] + (l * direction_of_movement['Yx'])
        current['y'] = current['y'] + (l * direction_of_movement['Yy'])
        current['z'] = current['z'] + (l * direction_of_movement['Yz'])
        current['i'] = i + 1

        f.write(
            f"i:{current['i']}  x:{current['x']}  y:{current['y']}  z:{current['z']}\n")

        p = realistion.photon_weight(p, mu_s, mu_a)
        if (p < 0.000001):
            print('Фотон поглощен')
            break

animate.visualize()
