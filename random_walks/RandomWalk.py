import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import math


class RW:
    def __init__(self, N):
        self.N = N
        self.R_2 = 0
        self.R_4 = 0
        w = [0] * self.N
        for k in range(self.N):
            w[k] = [0] * 2
        self.x = w

    def SpawnRW(self):
        self.x[0][0] = 0
        self.x[0][1] = 0
        for i in range(1, self.N):
            a = np.random.random()
            if a > 0.5:
                a = 1
            else:
                a = -1
            m = np.random.random()
            self.x[i][0] = a*m + self.x[i-1][0]
            b = np.random.random()
            if b > 0.5:
                b = 1
            else:
                b = -1
            c = b*math.sqrt(1-pow(m, 2))
            self.x[i][1] = c + self.x[i-1][1]
        t = pow(self.x[self.N-1][0], 2) + pow(self.x[self.N-1][1], 2)
        self.R_2 = t
        self.R_4 = pow(t, 2)


    def SpawnSARW(self, R):
        getout = False
        count = 0
        self.x[0][0] = 0
        self.x[0][1] = 0
        i = 1
        while i < self.N and getout == False:
            a = np.random.random()
            if a > 0.5:
                a = 1
            else:
                a = -1

            m = R * np.random.random()
            check1 = a * m + self.x[i - 1][0]
            b = np.random.random()
            if b > 0.5:
                b = 1
            else:
                b = -1
            c = b * math.sqrt(R*R - pow(m, 2))
            check2 = c + self.x[i - 1][1]
            j = 0
            while j < i:
                dist = pow(self.x[j][0]-check1,2) + pow(self.x[j][1]-check2,2)
                #Consider the possibility of including a little epsilon in the next if statement
                if dist < R*R:
                    j = i+5
                    i -= 1
                    count += 1
                    if count == 10:
                        getout = True
                else:
                    j += 1
            if j == i:
                self.x[i][0] = check1
                self.x[i][1] = check2
                count = 0
            i += 1

        t = pow(self.x[self.N - 1][0], 2) + pow(self.x[self.N - 1][1], 2)
        self.R_2 = t
        self.R_4 = pow(t, 2)

    def PrintRW(self):
        print(self.x)

