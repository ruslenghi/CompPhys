import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import math


class Forest:

    def __init__(self, l, p):
        self.l = l
        self.p = p
        self.lt = 0
        self.k = 0
        self.perc = False
        self.sp = 0
        self.M = []
        w = [0] * self.l
        for k in range(self.l):
            w[k] = [0] * self.l
        self.x = w
        self.z = []
        self.w = []

    def SpawnFakeForest (self):
        self.x = np.random.randint(0, 4, (self.l, self.l))

    def SpawnForest (self):
        self.x = [0] * self.l
        for k in range(self.l):
            self.x[k] = [0] * self.l
        i = 0
        j = 0
        while i < self.l:
            s = np.random.rand()
            if s < self.p:
                self.x[i][j] = 1
            if j < self.l - 1:
                j += 1
            else:
                j = 0
                i += 1
        return self.x

    def PrintForest (self):
        cmap = colors.ListedColormap(['white', 'green', 'red', 'black'])
        bounds = [0, 1, 2, 3, 4]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        fig, ax = plt.subplots()
        ax.imshow(self.x, cmap=cmap, norm=norm)
        plt.savefig('Fire.png')
        plt.show()

    def BurnForest(self):
        i = 0
        j = 0
        y = [0] * self.l
        for k in range(self.l):
            y[k] = [0] * self.l
        redcount = 0
        # i set fire to the first row
        while j < self.l:
            if self.x[i][j] == 1:
                self.x[i][j] = 2
                redcount += 1
            j += 1
        self.sp = 2
        self.lt = 2
        i = 0

        # i build a copy of the forest at time t_0
        while i < self.l:
            j = 0
            while j < self.l:
                y[i][j] = self.x[i][j]
                j += 1
            i += 1
        Nr = False
        redcount = 0
        while Nr == False:
            i = 0
            while i < self.l:
                j = 0
                while j < self.l:
                    if y[i][j] == 2:
                        if j != self.l - 1:
                            if y[i][j + 1] == 1:
                                self.x[i][j + 1] = 2
                                redcount += 1
                        if j != 0:
                            if y[i][j - 1] == 1:
                                self.x[i][j - 1] = 2
                                redcount += 1
                        if i != self.l - 1:
                            if y[i + 1][j] == 1:
                                self.x[i + 1][j] = 2
                                redcount += 1
                        if i != 0:
                            if y[i - 1][j] == 1:
                                self.x[i - 1][j] = 2
                                redcount += 1
                    j += 1
                i += 1
            i = 0
            while i < self.l:
                j = 0
                while j < self.l:
                    if y[i][j] == 2:
                        self.x[i][j] = 3
                    j += 1
                i += 1
            i = 0
            while i < self.l:
                j = 0
                while j < self.l:
                    y[i][j] = self.x[i][j]
                    j += 1
                i += 1
            if redcount == 0:
                Nr = True
            for k in range(self.l):
                if self.x[self.l-1][k] == 3:
                    self.perc = True
            if self.perc == False:
                self.sp += 1
            self.lt += 1
            redcount = 0

    def HK (self):
        k = 2
        M=[]
        M.append(0)
        M.append(0)
        i = 0

        while i < self.l:
            j = 0
            while j < self.l:
                if self.x[i][j] != 0:
                    if i == 0 and j == 0:
                        self.x[i][j] = k
                        k += 1
                        M.append(1)

                    elif i == 0 and j != 0:
                        if self.x[i][j - 1] != 0:
                            self.x[i][j] = self.x[i][j - 1]
                            M[self.x[i][j - 1]] += 1
                        if self.x[i][j - 1] == 0:
                            self.x[i][j] = k
                            k += 1
                            M.append(1)

                    elif i != 0 and j == 0:
                        if self.x[i - 1][j] != 0:
                            self.x[i][j] = self.x[i - 1][j]
                            M[self.x[i - 1][j]] += 1
                        if self.x[i - 1][j] == 0:
                            self.x[i][j] = k
                            k += 1
                            M.append(1)

                    else:
                        if self.x[i][j - 1] != 0 and self.x[i - 1][j] != 0:
                            if self.x[i - 1][j] > self.x[i][j - 1]:
                                min = self.x[i][j - 1]
                                max = self.x[i - 1][j]
                                M[max] = 0
                                self.x[i][j] = min
                                M[min] += 1

                                for n in range(i + 1):
                                    for m in range(j + 1):
                                        if self.x[n][m] == max:
                                            self.x[n][m] = min
                                            M[min] += 1

                            elif self.x[i - 1][j] < self.x[i][j - 1]:
                                min = self.x[i - 1][j]
                                max = self.x[i][j - 1]
                                M[max] = 0
                                self.x[i][j] = min
                                M[min] += 1
                                for n in range(i + 1):
                                    for m in range(j + 1):
                                        if self.x[n][m] == max:
                                            self.x[n][m] = min
                                            M[min] += 1

                            elif self.x[i - 1][j] == self.x[i][j - 1] != 0:
                                self.x[i][j] = self.x[i - 1][j]
                                M[self.x[i - 1][j]] += 1

                        elif self.x[i][j - 1] != 0 and self.x[i - 1][j] == 0:
                            self.x[i][j] = self.x[i][j - 1]
                            M[self.x[i][j - 1]] += 1

                        elif self.x[i][j - 1] == 0 and self.x[i - 1][j] != 0:
                            self.x[i][j] = self.x[i - 1][j]
                            M[self.x[i - 1][j]] += 1

                        elif self.x[i][j - 1] == self.x[i - 1][j] == 0:
                            self.x[i][j] = k
                            k += 1
                            M.append(1)
                j += 1
            i += 1
        self.k = k
        self.M = M

    def Set_z_w(self):
        w = []
        v = []
        for m in range(self.k):
            if self.M[m] != 0:
                v.append(self.M[m])

        v.sort()
        j = 1
        n = 0
        w.append(1)

        while j < len(v):
            if v[j - 1] == v[j]:
                w[n] += 1
                j += 1
            else:
                n += 1
                w.append(1)
                j += 1
        z = []
        z.append(v[0])
        j = 1

        while j < len(v):
            if v[j - 1] != v[j]:
                z.append(v[j])
                j += 1
            else:
                j += 1
        j = 0
        while j < len(z):
            w[j] = math.log(w[j]/(self.l*self.l))
            j += 1
        self.z = z
        self.w = w

    def BurnTree(self):
        m = 0

        self.SpawnForest()
        self.PrintForest()
        copy = self
        metacopy = Forest(self.l, self.p)
        appo = Forest(self.l, self.p)
        for k in range(self.l):
            for n in range(self.l):
                metacopy.x[k][n] = copy.x[k][n]
                appo.x[k][n] = copy.x[k][n]

        while copy.perc == False:
            redcount = 0
            if m < copy.l and copy.x[0][m] == 1:
                copy.x[0][m] = 2
                metacopy.x[0][m] = 2
                redcount += 1

                while redcount != 0:
                    counter = 0
                    i=0
                    j=0

                    while i < self.l:
                        while j < self.l:
                            if copy.x[i][j] == 2 and i > 0:
                                if copy.x[i - 1][j] == 1:
                                    metacopy.x[i - 1][j] = 2
                                    counter += 1

                            if copy.x[i][j] == 2 and i < copy.l-1:
                                if copy.x[i + 1][j] == 1:
                                    metacopy.x[i + 1][j] = 2
                                    counter += 1

                            if copy.x[i][j] == 2 and j > 0:
                                if copy.x[i][j - 1] == 1:
                                    metacopy.x[i][j - 1] = 2
                                    counter += 1

                            if copy.x[i][j] == 2 and j < copy.l-1:
                                if copy.x[i][j + 1] == 1:
                                    metacopy.x[i][j + 1] = 2
                                    counter += 1
                            j += 1
                        i += 1
                        j=0
                    i = 0
                    j = 0

                    while i < copy.l:
                        while j < copy.l:
                            if copy.x[i][j] == 2:
                                 metacopy.x[i][j] = 3
                            j += 1
                        j = 0
                        i += 1

                    for k in range(self.l):
                        for n in range(self.l):
                            copy.x[k][n] = metacopy.x[k][n]
                    redcount = counter

                for k in range(copy.l):
                    if copy.x[copy.l - 1][k] == 3:
                        for s in range(self.l):
                            for n in range(self.l):
                                appo.x[s][n] = copy.x[s][n]

                        copy.perc = True
            m += 1
            for k in range(self.l):
                for n in range(self.l):
                    copy.x[k][n] = appo.x[k][n]
                    metacopy.x[k][n] = appo.x[k][n]

            if m == copy.l and copy.perc == False:
                self.SpawnForest()
                self.PrintForest()
                copy = self
                for k in range(self.l):
                    for n in range(self.l):
                        metacopy.x[k][n] = copy.x[k][n]
                        appo.x[k][n] = copy.x[k][n]
                m = 0
        return appo
