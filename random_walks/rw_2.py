import matplotlib.pyplot as plt
from RandomWalk import RW
import math

M = 1000
R = 1
for m in range(1,11):
    a=0
    b=0
    v = []
    w = []
    N = m*10
    print(m)
    MyRW = RW(N)
    for k in range(M):
        test = 0
        while test == 0:
            MyRW.SpawnSARW(R)
            test = MyRW.x[MyRW.N-1][0]
        v.append(MyRW.R_2)
        w.append(MyRW.R_4)
        MyRW.x[MyRW.N - 1][0] = 0

    for l in range(M):
        a += v[l]/M
        b += w[l]/M
    d = math.sqrt((b - pow(a, 2)) / M) * math.sqrt(1 / M)
    c = d / a
    print(c)
    plt.scatter(N, a, c='b')
    print(N)

plt.xlabel('N')
plt.ylabel('R^2')
plt.title('Average value of R^2 as a function of the number of steps')
plt.savefig('RandomWalk2.png')
plt.show()