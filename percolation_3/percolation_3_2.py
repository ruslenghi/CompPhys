from Percolation import Forest
import math
import matplotlib.pyplot as plt

# Set l to be an odd number

l = 81
p = 0.592
v = []
w = []
k = 1

while k < l+1:
    if l%k == 0:
        v.append(k)
    k += 1

MyForest = Forest(l, p)
MyForest = MyForest.BurnTree()
MyForest.PrintForest()

a = l-1
a = int(a/2)
print(a)

z = []
t = []

if MyForest.x[a][a] == 3:
    R = 1
    
    while R < l:
        t.append(R)
        y = int(a - (R-1)/2)
        N = 0
        i = 0
        
        while i < R:
            j = 0
            while j < R:
                if MyForest.x[y+i][y+j] == 3:
                    N += 1
                j += 1
            i += 1
        z.append(N)
        R += 2
        
    print(z)
    
    for m in range(len(t)):
        t[m]=math.log(t[m])
        z[m] = math.log(z[m])
        
    a = t[int(l/3)-1] - t[6]
    b = z[int(l/3)-1] - z[6]
    c = b / a
    
    plt.scatter(t, z)
    plt.xlabel('log(R)')
    plt.ylabel('log(N(R))')
    plt.title('Sandbox method for a cluster in a ' + str(l) + " X " + str(l) + " lattice")
    plt.figtext(0.17, 0.8, "Estimate of d_f: " + str(c))
    plt.savefig('Sandbox.png')
    plt.show()

else:
    print("The center of the lattice does not belong to the percolating cluster, rerun the program")
