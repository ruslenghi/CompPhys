import matplotlib.pyplot as plt
from RandomWalk import RW
import math

for m in range(1, 11):
    N = m*100
    MyRW = RW(N)
    M = 3000
    a = 0
    b = 0
    v = []
    w = []
    for k in range(M):
        MyRW.SpawnRW()
        v.append(MyRW.R_2)
        w.append(MyRW.R_4)

    for l in range(M):
        a += v[l]/M
        b += w[l]/M

    d = math.sqrt((b-pow(a,2))/M)*math.sqrt(1/M)
    c = d/a
    print(c)
    plt.scatter(N, a, c='r')
    print(N)

plt.xlabel('N')
plt.ylabel('R^2')
plt.title('Average value of R^2 as a function of the number of steps')
plt.savefig('RandomWalk1.png')
plt.show()