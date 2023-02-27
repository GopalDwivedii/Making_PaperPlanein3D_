import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')


def f(x, y):
    return np.cos(np.sqrt(x ** 2 + y ** 2))-np.sqrt(np.sqrt(y ** 2 + x ** 2))+np.tanh(np.sqrt(y ** 2 + x ** 2))


theta = 9 * np.pi * np.random.random(100)
r = 6 * np.random.random(100)*np.pi
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.tanh(theta))
z = f(x, y)
# z1 = f1(x, y)
# z2 = f2(x, y)

ax1=fig.add_subplot(111, projection='3d',label='tanx')
ax1.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')

plt.show()
