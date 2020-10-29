import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


class Forest:

    def __init__(self, l, p):

        self.l = l
        self.p = p
        self.lt = 0
        self.perc = False
        self.sp = 0

        w = [0] * self.l
        for k in range(self.l):
            w[k] = [0] * self.l

        self.x = w

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


l=25
p=0.59274

MyForest = Forest(l, p)
MyForest.SpawnFakeForest()
MyForest.PrintForest()

MyForest.__init__(l,p)
MyForest.SpawnForest()
MyForest.PrintForest()

MyForest.BurnForest()

MyForest.PrintForest()

a=0
N=100

p=0

v=[]
w=[]
lt=[]
sp=[]

b = 0
c = 0
d = 0
i = 0


while p < 1:

    c=0
    d=0

    if i > 1:
        if 0.50 < p < 0.65:
            p += 0.02
        else:
            p += 0.05
    else:
        p += 0.05
    for k in range (N):
        MyForest.__init__(l, p)
        MyForest.SpawnForest()
        MyForest.BurnForest()
        if MyForest.perc == True:
            c+=MyForest.sp
            d+=MyForest.lt
            a+=1
    b = a/N
    v.append(b)
    b = c/N
    sp.append(b)
    b = d/N
    lt.append(b)
    w.append(p)
    print(p)
    a=0
    i += 1

plt.plot(w,v, 'go')
plt.axis([-0.1, 1.1, -0.1, 1.1])
plt.xlabel('p')
plt.ylabel('Probability of Percolation')
plt.title('Probability of Percolation as a function of p (L=25, 100 sampling for each p)')
plt.savefig('L=25_Perc.png')
plt.show()

plt.plot(w,sp, 'go')
plt.axis([-0.1, 1.1, 0, 3*l])
plt.xlabel('p')
plt.ylabel('Shortest path average length')
plt.title('Shortest path average length as a function of p (L=25, 100 sampling for each p)')
plt.savefig('L=25_Sp.png')
plt.show()

plt.plot(w,lt, 'go')
plt.axis([-0.1, 1.1, 0, 3*l])
plt.xlabel('p')
plt.ylabel('Average Lifetime')
plt.title('Average Lifetime as a function of p (L=25, 100 sampling for each p)')
plt.savefig('L=25_Lt.png')
plt.show()


