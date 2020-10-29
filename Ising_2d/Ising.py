import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

class Ising:
    def __init__(self, L, T):
        self.L = L
        self.T = T
        self.b = 1/T
        self.E = 0
        w = [0] * self.L
        for k in range(self.L):
            w[k] = [0] * self.L
        self.x = w

    def SetGS(self):
        for i in range(self.L):
            for j in range(self.L):
                self.x[i][j] = 1
        self.E = 0

    def Energy(self):
        H = 0
        for i in range(self.L):
            for j in range(self.L):
                if i != 0 and j != 0 and i != self.L-1 and j != self.L-1:
                    H += -(self.x[i][j]*self.x[i-1][j])
                    H += -(self.x[i][j] * self.x[i + 1][j])
                    H += -(self.x[i][j] * self.x[i][j-1])
                    H += -(self.x[i][j] * self.x[i][j+1])

                if i == 0 and j != 0 and j != self.L-1:
                    H += -(self.x[i][j] * self.x[self.L-1][j])
                    H += -(self.x[i][j] * self.x[i + 1][j])
                    H += -(self.x[i][j] * self.x[i][j - 1])
                    H += -(self.x[i][j] * self.x[i][j + 1])

                if j == 0 and i != 0 and i != self.L-1:
                    H += -(self.x[i][j] * self.x[i-1][j])
                    H += -(self.x[i][j] * self.x[i + 1][j])
                    H += -(self.x[i][j] * self.x[i][self.L-1])
                    H += -(self.x[i][j] * self.x[i][j + 1])

                if j == self.L-1 and i != 0 and i != self.L-1:
                    H += -(self.x[i][j] * self.x[i-1][j])
                    H += -(self.x[i][j] * self.x[i + 1][j])
                    H += -(self.x[i][j] * self.x[i][self.L-2])
                    H += -(self.x[i][j] * self.x[i][0])

                if i == self.L-1 and j != 0 and j != self.L-1:
                    H += -(self.x[i][j] * self.x[self.L-2][j])
                    H += -(self.x[i][j] * self.x[0][j])
                    H += -(self.x[i][j] * self.x[i][j-1])
                    H += -(self.x[i][j] * self.x[i][j+1])

                if j == 0 and i == 0:
                    H += -(self.x[i][j] * self.x[self.L-1][j])
                    H += -(self.x[i][j] * self.x[i + 1][j])
                    H += -(self.x[i][j] * self.x[i][self.L-1])
                    H += -(self.x[i][j] * self.x[i][j + 1])

                if j == self.L-1 and i == 0:
                    H += -(self.x[i][j] * self.x[self.L-1][j])
                    H += -(self.x[i][j] * self.x[1][j])
                    H += -(self.x[i][j] * self.x[i][self.L-2])
                    H += -(self.x[i][j] * self.x[i][0])

                if j == 0 and i == self.L-1:
                    H += -(self.x[i][j] * self.x[self.L-2][j])
                    H += -(self.x[i][j] * self.x[0][j])
                    H += -(self.x[i][j] * self.x[i][self.L-1])
                    H += -(self.x[i][j] * self.x[i][1])

                if j == self.L-1 and i == self.L-1:
                    H += -(self.x[i][j] * self.x[self.L-2][j])
                    H += -(self.x[i][j] * self.x[0][j])
                    H += -(self.x[i][j] * self.x[i][self.L-2])
                    H += -(self.x[i][j] * self.x[i][0])

        H = 1/2 * H
        return H

    def Delta(self, i, j):
        h = 0
        if i != 0 and j != 0 and i != self.L - 1 and j != self.L - 1:
            h += self.x[i][j+1] + self.x[i][j-1] + self.x[i-1][j] + self.x[i+1][j]
        if i == 0 and j != 0 and j != self.L - 1:
            h += self.x[i][j + 1] + self.x[i][j - 1] + self.x[self.L-1][j] + self.x[i + 1][j]
        if j == 0 and i != 0 and i != self.L - 1:
            h += self.x[i][j + 1] + self.x[i][self.L-1] + self.x[i - 1][j] + self.x[i + 1][j]
        if j == self.L - 1 and i != 0 and i != self.L - 1:
            h += self.x[i][0] + self.x[i][j - 1] + self.x[i - 1][j] + self.x[i + 1][j]
        if i == self.L - 1 and j != 0 and j != self.L - 1:
            h += self.x[i][j + 1] + self.x[i][j - 1] + self.x[i - 1][j] + self.x[0][j]
        if j == 0 and i == 0:
            h += self.x[i][j + 1] + self.x[i][self.L-1] + self.x[self.L-1][j] + self.x[i + 1][j]
        if j == self.L - 1 and i == 0:
            h += self.x[i][0] + self.x[i][j - 1] + self.x[self.L - 1][j] + self.x[i + 1][j]
        if j == 0 and i == self.L - 1:
            h += self.x[i][j + 1] + self.x[i][self.L - 1] + self.x[i - 1][j] + self.x[0][j]
        if j == self.L - 1 and i == self.L - 1:
            h += self.x[i][0] + self.x[i][j - 1] + self.x[i - 1][j] + self.x[0][j]
        delta = 2*h*self.x[i][j]
        return delta

    def Metropolis(self):
        for i in range(self.L*self.L):
            a = np.random.randint(0, self.L)
            b = np.random.randint(0, self.L)
            d = self.Delta(a, b)
            self.x[a][b] = - self.x[a][b]
            self.E += d
            if d > 0:
                p = np.exp(-self.b*d)
                eta = np.random.rand()
                if eta > p:
                    self.x[a][b] = - self.x[a][b]
                    self.E -= d

    def Magnetization(self):
        m = 0
        for i in range(self.L):
            for j in range(self.L):
                m += self.x[i][j]
        return m/(self.L*self.L)

    def PrintLattice(self):
        cmap = colors.ListedColormap(['blue', 'red'])
        bounds = [-1, 1]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        fig, ax = plt.subplots()
        ax.imshow(self.x, cmap=cmap, norm=norm)
        plt.show()
