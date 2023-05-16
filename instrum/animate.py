from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt
import instrum.realisation as realisation
import instrum.vox as vox
import re

style.use('ggplot')


def diagramm(arr, width, nameY):
    key = []
    for i in range(len(arr)):
        key.append((i * 10) / 100)
    print(arr)
    plt.bar(key, arr, width=width)
    plt.ylabel(nameY)
    plt.xlabel('distance')
    plt.show()


def lineGraph(arr, root):
    x_arr = []

    with open(root) as f:
        for line in f:
            print(line)
            x_arr.append(line[2: len(line) - 2].split(','))
    # print(x_arr)
    key = []
    # for i in range(len(arr)):
    #     key.append((i * 10) / 100)
    # print(x_arr)
    # plt.bar(key, x_arr[2], width=0.1)
    # plt.xlabel('distance')
    # plt.show()
    for i in range(len(arr)):
        key.append((i * 10) / 100)
    # print(x_arr)
#   plt.yticks([0,2,10,40])
#    plt.yscale('log')

    li_xarr = [15.717540102947426,9.804689259721462,7.627013765467798,5.779832846633721,4.660413480938467,4.337912893704379,3.713873699154815,2.861373593513759,2.2287226799101396,1.6123235752512075,1.8484563182778029,1.275189359942141,1.1556552781190628,1.0608276031878225,0.6187176602589329,0.5905807259946625,0.5119842608675486,0.36823574942359427,0.28247408156381937,0.19032139655839073,0.23290702058302357,0.18078257189450023,0.1177326117755698,0.05488118888330306,0.08631841290840507,0.07655499162499727,0.028471602536573538,0.03195487440197257,-0.0010618707994124762,0.0039499181730908795,-0.003018548110162447,-0.0027985222572735214,-0.016971702626605148,-0.015961538190186208,-0.019109914365047678,-0.022027452893513853,-0.019635939817977996,-0.022165827758107114,-0.021224914483086322,-0.028915309260506852,-0.028886166467560558,-0.02543670000934789,-0.030719991719879172,-0.029830663971267678,-0.029861632778748953,-0.029821566218455754,-0.030865030829037802,-0.031264586077108594,-0.031328234983255474,-0.03127552196597294,-0.03137080809941658,-0.03132605685015447,-0.03123397763407163,-0.0307263939040222,-0.031313457782392154,-0.031386602647927996,-0.03139988536498643,-0.03133973026477181,-0.03135869211118609,-0.031415926535897934,-0.03138749863780773,-0.031415926535897934,-0.031415926535897934,-0.031243262098943732,-0.03140120986533692,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.03139988536498643,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.03140120986533692,-0.031396868020737975,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934,-0.031415926535897934]


    plt.plot((key), li_xarr)
    #plt.plot(list(reversed(key)), x_arr[1])
    #plt.plot(list(reversed(key)), x_arr[2])
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
            current_line['i'] = line[0].split(':')[1]
            current_line['x'] = line[1].split(':')[1]
            current_line['y'] = line[2].split(':')[1]
            current_line['z'] = line[3].split(':')[1]

            list_current_X.append(float(current_line['x']))
            list_current_Y.append(float(current_line['y']))
            list_current_Z.append(float(current_line['z']))
            list_current_I.append(int(current_line['i']))

    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection='3d')

    arr = {}
    itteration = 0

    for i in range(len(list_current_I)):
        if int(list_current_I[i]) >= itteration and itteration + 1 != int(list_current_I[-1]):
            beginning = list_current_I.index(itteration + 1)
            end = list_current_I.index(itteration + 2)

            match = False
            while not match:
                curent_color = '#' + realisation.random_color()
                match = re.search(
                    r'^#(?:[0-9a-fA-F]{3}){1,2}$', curent_color)
            if (view == 'line'):
                arr[itteration] = ax.plot3D(list_current_X[beginning:end], list_current_Y[beginning:end],
                                            list_current_Z[beginning:end], color=curent_color, marker=',')
            else:
                arr[itteration] = ax.scatter(list_current_X[beginning:end], list_current_Y[beginning:end],
                                             list_current_Z[beginning:end], color=curent_color)

            itteration += 1
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.title("simple 3D current photon coordinates")

    photonlist = []
    countlist = []

    for key, value in arr.items():
        photonlist.append(value)
        countlist.append(key)
    for i in range(len(countlist)):
        countlist[i] = 'photon ' + str(countlist[i] + 1)

    print(photonlist)
    plt.legend(tuple(photonlist), tuple(countlist),
               loc='upper center', ncols=8, fontsize='xx-small')

    plt.show()
