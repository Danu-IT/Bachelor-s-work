import instrum.realisation as realisation
import instrum.animate as animate
import instrum.vox as vox
import instrum.animation as animation
from concurrent.futures import ProcessPoolExecutor
import math
import matplotlib.pyplot as plt
import numpy as np
from functools import partial

mu_s = 10                   # коэффициентом рассеяния
mu_a = 0.15                 # коэффициентом поглощения
g = 0.9                     # параметр анизатропии
photons = 1000              # фотоны
size = 100                  # граница
left = - (size / 2)
right = (size / 2)
x_max = 10

array_current = []          # массив координат
slice = 5
sliceThinkness = 0.5
a = 100

masY = [0] * a
maksY = 0
for i in range(a):
    #masY[i] = [0] * (a * 2)
    masY[i] = [0] * 200

masZ = [0] * a
maksZ = 0
for i in range(a):
    masZ[i] = [0] * (a * 2)
    #masZ[i] = [0] * 101

#w_arr = []
#for i in range(100):
#    w_arr.append(0)

f = open('outputs/current.txt', 'w')
m = open('outputs/weight.txt', 'a')
w_arr = []                             # total_w
w_total = 0
z_arr = []
z_max_el = []
#current_z_list = []

for iter_z in range(1):

    for i in range(photons):
        # Действительные координаты
        current = {'x': 0, 'y': 0, 'z': 4.5} #
        # Изменение направления фотона
        direction_of_movement = {'Yx': 0, 'Yy': 0, 'Yz': 1}
        w = 1  # Вес фотона
        w_total = 0

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


            if (current['y'] > -sliceThinkness and current['y'] < sliceThinkness and abs(current['x']) < x_max and abs(current['z']) < x_max and (current['z']) > 0):
                indeks1 = math.floor(((current['x'] - 10) / x_max) * 100)
                indeks2 = math.floor((current['z'] / x_max) * 100)

                #print("indeks1 = ", indeks1)
                #print("indeks2 = ", indeks2)

                masY[indeks2][indeks1] += w
                if (maksY < masY[indeks2][indeks1]):
                    maksY = masY[indeks2][indeks1]

            if (current['z'] > -sliceThinkness and current['z'] < sliceThinkness and abs(current['x']) < x_max and abs(current['y']) < x_max):
                indeks1 = math.floor(((current['x'] - 10) / x_max) * 100)
                indeks2 = math.floor(((current['y'] - 10) / x_max) * 50)
                masZ[indeks2][indeks1] += w
                if (maksZ < masZ[indeks2][indeks1]):
                    # print(current['z'])
                    maksZ = masZ[indeks2][indeks1]
                    #print(masZ[indeks2][indeks1])

            if (i <= 50):
                f.write(f"i:{current['i']}  x:{current['x']}  y:{current['y']}  z:{current['z']}\n")

            w = realisation.photon_weight(w, mu_s, mu_a)
            if w < 0.000001:
                # print('Фотон поглощен')
                break
            #print("i=", i, " z=", current['z'], " w=", w)

            #if math.floor(current['z']) <= iter_z:
            #    #w_total += w
            #    z_arr.append(current['z'])
#w_arr.append(w_total)
#z_arr.append(iter_z)
#print(masZ)
#print(w_arr)

#plt.plot(z_arr, w_arr, '-b')
#plt.axis(w_arr)
#plt.ylim(w_arr[0], w_arr[-1])
#plt.ylabel('Суммарный вес фотонов')
#plt.xlabel('z')
plt.show()

for we in range(len(masZ)):
#    print(masZ[we])
    w_total = sum(masZ[we])
    #print(w_total)
    w_arr.append(w_total)

print(sum(w_arr))
m.write('\t' + str(sum(w_arr)) + ',')

#print(len(z_arr))
w_hard = [16393.901055185288,	8048.740685980214,	3868.0087044391435,	2848.9209774179853,	1746.9798645427413,	1373.2737266890183,	931.4287950572281,	646.5351606129941,	477.2375612752]
z_hard = []
for z_iter in range(len(w_hard)):
    z_hard.append(z_iter/2)
print(w_hard)
print(z_hard)
#plt.yscale('symlog')
plt.plot(z_hard, w_hard, '-b')
#plt.ylim(w_arr[0], w_arr[-1])
plt.ylabel('Суммарный вес фотонов')
plt.xlabel('z')
plt.show()


####

#x = np.linspace(0, np.max(z_hard))
x = np.linspace(0, 10)
y = np.linspace(np.max(w_hard), np.min(w_hard))

print(x)
print(y)
fig, ax = plt.subplots()
plt.yscale('symlog')
ax.plot(x, y)

# Set y scale to exponential
#ax.set_yscale('function', functions=(partial(np.power, 10.0), np.log10))
ax.set(xlim=(0, np.max(10)), ylim=(0, np.max(700)))
#ax.set_xticks([1, 3, 3.5, 3.75, 4.0])

plt.show()

        # if (current['z'] < 0):
        #     answer = math.floor(
        #         realisation.distanceBetweenPoints(current) / x_max * len(w_arr))
        #     print(current)
        #     if (answer < 100):
        #         w_arr[answer] += w
        #     break

# График передвижения фотона в среде по точкам
# animate.graphOfPointsOfDifferentColors('point')
# График передвижения фотона в среде линиями
#animate.graphOfPointsOfDifferentColors('line')
# Гистограмма кол-во фотонов к расстоянию
# animate.diagramm(w_arr, 0.1, 'count')
# Гистограмма площадь кольца к расстоянию
# seq = realisation.calcSquare(w_arr)
# animate.diagramm(seq, 0.1, 'square')

# vox.voxVisualizerCub(size, array_current)

#vox.voxVisualizer(maksZ, masZ, 'z')
#vox.voxVisualizer(maksY, masY, 'y')
