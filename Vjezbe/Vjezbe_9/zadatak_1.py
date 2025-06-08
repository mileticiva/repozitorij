import numpy as np
import math
import matplotlib.pyplot as plt

G = 6.67408e-11
Ms = 1.989e30
Mz = 5.9742e24

Zrx = 1.496e11
Zry = 0
Zvx = 0
Zvy = 29783
Zax = 0
Zay = 0

Srx = 0
Sry = 0
Svx = 0
Svy = 0
Say = 0
Sax = 0

sunce_x = []
sunce_y = []
zemlja_x = []
zemlja_y = []

trajanje = 365.242 * 24 * 3600

korak = 60 * 60 * 24
for i in range(0, int(trajanje), korak):
    dx = Zrx - Srx
    dy = Zry - Sry
    r = math.sqrt(dx ** 2 + dy ** 2)

    if r == 0:
        Zax = 0
        Zay = 0
    else:
        Zax = -G * Ms * dx / r**3
        Zay = -G * Ms * dy / r**3

    Zvx = Zvx + Zax * korak
    Zvy = Zvy + Zay * korak

    Zrx = Zrx + Zvx * korak
    Zry = Zry + Zvy * korak

    if r == 0:
        Sax = 0
        Say = 0
    else:
        Sax = -G * Mz * (-dx) / r**3
        Say = -G * Mz * (-dy) / r**3

    Svx = Svx + Sax * korak
    Svy = Svy + Say * korak

    Srx = Srx + Svx * korak
    Sry = Sry + Svy * korak

    sunce_x.append(Srx)
    sunce_y.append(Sry)
    zemlja_x.append(Zrx)
    zemlja_y.append(Zry)

plt.plot(sunce_x, sunce_y)
plt.plot(zemlja_x, zemlja_y)
plt.scatter(sunce_x[0], sunce_y[0], color="blue", s=100)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Putanje Sunca i Zemlje")
plt.show()