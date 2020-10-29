from IsingModel import Ising
import matplotlib.pyplot as plt
import math
from matplotlib import colors

L = 50
T = 0

fig1 = plt.figure()
plt.title('Magnetization as a function of temperature')
ax = fig1.add_subplot(1, 1, 1)
fig2 = plt.figure()
plt.title('Energy as a function of temperature')
bx = fig2.add_subplot(1, 1, 1)
while T < 4:
    if 0 <= T < 1.8 or T > 2.5:
        T += 0.2
    elif 1.8 <= T < 2.18 or 2.4 < T <= 2.5:
        T += 0.1
    elif 2.18 <= T <= 2.4:
        T += 0.03
    Lat = Ising(L, T)
    Lat.SetGS()
    m = 0
    E = 0
    Sm = 0
    Se = 0
    v = []
    w = []
    for k in range(100):
        Lat.Metropolis()
        
    for j in range(100):
        Lat.Metropolis()
        E += Lat.E/100
        v.append(Lat.E)
        m += Lat.Magnetization()/100
        w.append(Lat.Magnetization())
        
    for l in range(100):
        Se += (v[l]-E)*(v[l]-E)
        Sm += (w[l]-m)*(w[l]-m)

    Se = math.sqrt(Se/100)
    Sm = math.sqrt(Sm/100)
    ax.errorbar(T, m, yerr=Sm, c='k', fmt = 'o')
    bx.errorbar(T, E, yerr=Se, c='b', fmt = 'o')
    print(T)

fig1.savefig("Magnetization.png")
fig2.savefig("Energy.png")
plt.show()
