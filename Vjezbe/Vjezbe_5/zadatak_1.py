import calculus
import math
import sympy
import matplotlib.pyplot as plt

def kubna(x):
    return (5 * (x ** 3)) - (2 * (x ** 2)) + (2 * x) - 3

def trigonometrijska(x):
    return math.sin(x)

donja = -2
gornja = 2
korak = 0.1
numericki = calculus.druga(kubna, donja, gornja, korak)

x = sympy.Symbol("x")
f = kubna(x)
a = sympy.diff(f, x)
i = donja
analiticke = []
tocke = []
while i < gornja:
    analiticke.append(a.subs(x, i))
    tocke.append(i)
    i += korak

plt.plot(tocke, analiticke)
plt.plot(tocke, numericki, ls='', marker='.')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("")
plt.show()