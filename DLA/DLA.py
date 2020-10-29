import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import math

class DLA:

    def __init__(self, l, cc):

        #pick l odd

        self.l = l
        self.t = 0
        self.cc = cc
        w = [0] * 3 * self.l
        for k in range(3 * self.l):
            w[k] = [0] * 3 * self.l

        z = [0] * self.l
        for k in range(self.l):
            z[k] = [0] * self.l

        self.x = w
        self.y = z
        self.x[int((3*self.l-1)/2)][int((3*self.l-1)/2)] = 1

    def SpawnStart(self):

        p = np.random.rand()

        if 0.25 > p > 0:
            x = 2*self.l-1
            y = np.random.randint(self.l-1, 2*self.l)

        if 0.5 > p > 0.25:
            x = self.l-1
            y = np.random.randint(self.l-1, 2*self.l)

        if 0.75 > p > 0.5:
            x = np.random.randint(self.l-1, 2*self.l)
            y = 2*self.l-1

        if 1 > p > 0.75:
            x = np.random.randint(self.l-1, 2*self.l)
            y = self.l-1

        v = []

        v.append(x)
        v.append(y)

        return v

    def RandStep(self, v):

        p = np.random.randint(1,5)

        if p == 1:
            v[0] += 1

        if p == 2:
            v[0] += -1

        if p == 3:
            v[1] += 1

        if p == 4:
            v[1] -= 1

    def OnePiece(self):

        v = self.SpawnStart()

        while self.x[v[0]-1][v[1]] == 0 and self.x[v[0]+1][v[1]] == 0 and self.x[v[0]][v[1]-1] == 0 and self.x[v[0]][v[1]+1] == 0:

            self.RandStep(v)

            if v[0] > (5/2) * self.l or v[0] < 1/2 * self.l:
                v = self.SpawnStart()

            if v[1] > (5 / 2) * self.l or v[1] < 1 / 2 * self.l:
                v = self.SpawnStart()

        self.t += 1
        print(self.t)

        a = int(self.t/self.cc)
        a = a % 6
        a += 1

        self.x[v[0]][v[1]] = a


    def PrintGrid (self):

        for i in range(self.l):
            for j in range(self.l):
                self.y[i][j] = self.x[self.l+i][self.l+j]

        cmap = colors.ListedColormap(['black', 'blue', 'blue', 'red', 'red', 'yellow'])
        bounds = [0, 1, 2, 3, 4, 5, 6]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        fig, ax = plt.subplots()
        ax.imshow(self.y, cmap=cmap, norm=norm)

        plt.savefig('DLAg3.png')
        plt.show()