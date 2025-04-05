import numpy as np
import matplotlib.pyplot as plt

v0 = float(input("v0="))
kut = float(input("kut="))

kut = np.radians(kut)

v0x = v0 * np.cos(kut)
v0y = v0 * np.sin(kut)

g = 9.81
korak = 0.5
koraci = int(10 / korak)

t = np.linspace(0, 10, koraci)

x = []
y = []
vx = []
vy = [] 
for i in range(koraci):
    x.append(0)
    y.append(0)
    vx.append(0)
    vy.append(0)

vx[0] = v0x
vy[0] = v0y

for i in range(1, koraci):
    vy[i] = vy[i-1] - g * korak
    vx[i] = vx[i-1]

    x[i] = x[i-1] + vx[i-1] * korak
    y[i] = y[i-1] + vy[i-1] * korak

plt.subplot(1, 3, 1)
plt.plot(x, y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("x - y graf")
plt.ylim(-100, 100)

plt.subplot(1, 3, 2)
plt.plot(t, x)
plt.xlabel("Vrijeme (s)")
plt.ylabel("x (m)")
plt.title("x - t graf")

plt.subplot(1, 3, 3)
plt.plot(t, y)
plt.xlabel("Vrijeme (s)")
plt.ylabel("y (m)")
plt.title("y - t graf")
plt.ylim(-100, 100)

plt.tight_layout()
plt.show()