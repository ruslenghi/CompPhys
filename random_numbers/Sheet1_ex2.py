from Sheet_1_ex1 import rng

print("Enter the parameters you wish to use for your rng ")
c = int(input("c:"))
p = int(input("p: "))
seed = int(input("Seed: "))
n = int(input("How many random numbers do you want the rng to produce?: "))

k = int(input("Enter the number of bins you want to divide the interval [0,1] into: "))
d=1/k

gen = rng(c,p,seed,n)
v=gen.generate()
w = []

i=0

while i < k:

    w.append(0)
    i += 1

i=0
j=0
m=0

while i < n:

    x = v[i]

    while x > j:

        j += 1/k
        m +=1

    w[m-1] += 1
    i +=1
    m=0
    j=0

i=0

while i < k:
    print("In the interval number "+ str(i+1) +" there are "+ str(w[i]) +" numbers")
    i += 1

i=0

while i < n:
    print("In the random number in position "+ str(i+1) +" is "+ str(v[i]))
    i += 1

i=0


X=0

a = n/k

while i<k :

    X += ((w[i]-a)*(w[i]-a))/a
    i += 1

print("The Chi square value is: "+ str(X))

#This program is only able to make do Chi square test for a rng that uniformly generates float random numbers in the interval [0,1]
