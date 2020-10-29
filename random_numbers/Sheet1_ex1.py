from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

#Function to generate random numbers
class rng():

    def __init__(self, c, p, seed, l):
        self.c=c
        self.p=p
        self.seed=seed
        self.l=l

    #The following method builds a list of length l, filled with random numbers
    def generate(self):

        count=1
        v = []

        v.append((self.seed/self.p))

        while count < self.l :

            x = (self.c*self.seed)%self.p
            v.append(x/(self.p))
            self.seed = x
            count += 1

        return v

    #Function to do a square test given a certain list containing random numbers
    def print_2d(self,v):

        d = len(v)

        if d%2 == 0:
            pass

        else :
            d -= 1

        i=0

        while i<d:

            x=v[i]
            y=v[i + 1]
            i += 2
            plt.scatter(x,y,c="blue")

        plt.show()

    #Function to do a cube test given a certain list containing random numbers
    def print_3d(self,v):

        d = len(v)
        d = int((d/3)//1)*3
        r = int((d/3)//1)

        fig=plt.figure(2)
        ax = Axes3D(fig)

        sequence_containing_x_vals = list(range(r))
        sequence_containing_y_vals = list(range(r))
        sequence_containing_z_vals = list(range(r))

        i = 0
        j = 0

        while j < d:

            sequence_containing_x_vals[i] = v[j]
            sequence_containing_y_vals[i] = v[j + 1]
            sequence_containing_z_vals[i] = v[j + 2]

            i += 1
            j += 3

        ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
        plt.show()

#I build the rng
print("Enter the parameters you wish to use for your rng ")
c = int(input("c:"))
p = int(input("p: "))
seed = int(input("Seed: "))
l = int(input("How many random numbers do you want the rng to produce?: "))

gen_2d = rng(c,p,seed,l)
gen_3d = rng(c,p,seed,l)

#I do the square test
gen_2d.print_2d((gen_2d.generate()))
#I do the cube test
gen_3d.print_3d((gen_3d.generate()))







