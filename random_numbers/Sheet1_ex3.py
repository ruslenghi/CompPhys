import matplotlib.pyplot as plt

counter = 0

print("Enter the parameters you wish to use for your rng ")
c = int(input("c:"))
p = int(input("p: "))
seed = int(input("Seed: "))
n = int(input("How many random points do you want to produce within the circle?: "))

r=int(input("Enter the radius of the circle: "))

v = []

i=0

while i < n:

    a = 0
    x = (c * seed) % p
    y = (c*x) % p
    seed = y
    x = (4*float(x/p)-2)*r
    y = (4*float(y/p)-2)*r
    a = x*x+y*y

    if a < r*r:
        v.append(x)
        v.append(y)
        i += 1

    else:
        pass

if counter >= int(p/2):
    exit(1)

else:
    pass

i=0

while i<n:

    a=v[i]
    b=v[i + 1]
    i += 2
    plt.scatter(a,b,c="blue")

plt.show()

