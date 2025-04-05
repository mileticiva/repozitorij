import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(sila, masa, vrijeme):
    a = sila / masa
    
    korak = 0.5
    koraci = int(vrijeme / korak)

    t = np.linspace(0, vrijeme, koraci)

    akc = []
    for i in range(koraci):
        akc.append(a)

    x = []
    v = []
    for i in range(koraci):
        x.append(0)
        v.append(0)

    for i in range(1, koraci):
        v[i] = v[i-1] + a * korak
        x[i] = x[i-1] + v[i-1] * korak

    plt.subplot(3, 1, 1)
    plt.plot(t, x)
    plt.ylabel("Pomak (m)")
    plt.title("x-t graf")

    plt.subplot(3, 1, 2)
    plt.plot(t, v)
    plt.ylabel("Brzina (m/s)")
    plt.title("v-t graf")

    plt.subplot(3, 1, 3)
    plt.plot(t, akc)
    plt.xlabel("Vrijeme (s)")
    plt.ylabel("Ubrzanje (m/s²)")
    plt.title("a-t graf")

    plt.show()

def kosi_hitac(v0, kut, vrijeme):
    kut = np.radians(kut)

    v0x = v0 * np.cos(kut)
    v0y = v0 * np.sin(kut)

    g = 9.81
    korak = 0.5
    koraci = int(vrijeme / korak)

    t = np.linspace(0, vrijeme, koraci)

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
    plt.ylim(-120, 100)

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
    plt.ylim(-120, 100)

    plt.tight_layout()
    plt.show()