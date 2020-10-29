from Percolation import Forest
import math
import matplotlib.pyplot as plt

l = 80
p = 0.592
v = []
w = []
k = 1

while k < l+1:
    if l%k == 0:
        v.append(k)
    k += 1

print(v)

MyForest = Forest(l, p)
MyForest = MyForest.BurnTree()
MyForest.PrintForest()

for s in range(len(v)):

    e = v[s]
    N = 0
    n = 0

    while n < MyForest.l:

        m = 0

        while m < MyForest.l:

            i = 0

            while i < e:

                j = 0

                while j < e:

                    if MyForest.x[i + n][j + m] == 3:
                        N += 1
                        j = e
                        i = e

                    j += 1

                i += 1

            i = 0
            m += e

        n += e

    w.append(N)

print(w)

for i in range(len(v)):
    v[i] = -v[i]

v.sort()
w.sort()

for i in range(len(v)):
    v[i] = -v[i]
    v[i] = math.log(1/v[i])
    w[i] = math.log(w[i])

print(w)
print(v)

a = v[7]-v[1]
b = w[7]-w[1]

c = b/a

plt.scatter(v,w)
plt.xlabel('log(1/ε)')
plt.ylabel('log(N(ε))')
plt.title('Box Counting method for a cluster in a ' + str(l) + " X " + str(l) + " lattice")
plt.figtext(0.17, 0.8, "Estimate of d_f: " + str(c))
plt.savefig('BoxCounting.png')
plt.show()
