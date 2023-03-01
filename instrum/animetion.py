# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib.animation import FuncAnimation
# plt.style.use('seaborn-pastel')

# fig = plt.figure()
# ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
# line, = ax.plot([], [], lw=3)


# def init():
#     line.set_data([], [])
#     return line,


# def animate(i):
#     x = np.linspace(0, 4, 1000)
#     y = np.sin(2 * np.pi * (x - 0.01 * i))
#     line.set_data(x, y)
#     return line,


# anim = FuncAnimation(fig, animate, init_func=init,
#                      frames=200, interval=20, blit=True)

# anim.save('sine_wave.gif', writer='imagemagick')


# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt


# z = 4 * np.tan(np.random.randint(10, size=(500))) + \
#     np.random.randint(100, size=(500))
# x = 4 * np.cos(z) + np.random.normal(size=500)
# y = 4 * np.sin(z) + 4 * np.random.normal(size=500)

# fig = plt.figure(figsize=(16, 9))
# ax = plt.axes(projection="3d")

# ax.grid(b=True, color='grey',
#         linestyle='-.', linewidth=0.3,
#         alpha=0.2)


# my_cmap = plt.get_cmap('hsv')

# sctt = ax.scatter(x, y, z,
#                   alpha=0.8,
#                   c=x + y + z,
#                   cmap=my_cmap,
#                   marker='^')

# plt.title("simple 3D scatter plot")
# ax.set_xlabel('X-axis', fontweight='bold')
# ax.set_ylabel('Y-axis', fontweight='bold')
# ax.set_zlabel('Z-axis', fontweight='bold')
# fig.colorbar(sctt, ax=ax, shrink=0.5, aspect=5)

# plt.show()
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

colors = ['b', 'c', 'y']

c1 = ax.scatter(np.random.rand(100), np.random.rand(100),
                np.random.rand(100), color=colors[0])
c2 = ax.scatter(np.random.rand(100), np.random.rand(100),
                np.random.rand(100), color=colors[1])
c3 = ax.scatter(np.random.rand(100), np.random.rand(100),
                np.random.rand(100), color=colors[2])

plt.legend((c1, c2, c3), ('class one', 'class two',
           'class three'), loc='upper right')

plt.show()
