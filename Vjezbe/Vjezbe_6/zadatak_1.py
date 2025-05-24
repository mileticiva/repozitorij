from harmonic_oscillator import HarmonicOscillator
import matplotlib.pyplot as plt
import numpy as np

m = 0.1
k = 10
x = 0.3
v = 0

h = HarmonicOscillator(m, k, x, v)
h.oscillate(2)
h.plot_trajectory()
h.reset()

h.oscillate(2, 0.05)
x1 = h.poz[:]
koraci1 = h.koraci[:]
h.reset()

h.oscillate(2, 0.01)
x2 = h.poz[:]
koraci2 = h.koraci[:]
h.reset()

o = np.sqrt(k / m)
t = np.linspace(0, 2, 100)
A = x
B = v / o

analiticko = A * np.cos(o * t) + B * np.sin(o * t)

plt.plot(koraci1, x1, ls='', marker='.')
plt.plot(koraci2, x2, ls='', marker='.')
plt.plot(t, analiticko)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("x - t graf")
plt.ylim(min(analiticko) - 0.1, max(analiticko) + 0.1)

plt.show()