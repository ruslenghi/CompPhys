import matplotlib.pyplot as plt
from Percolation import Forest

l = 800
p = 0.8

MyForest = Forest(l, p)
MyForest.SpawnForest()
MyForest.HK()
MyForest.Set_z_w()

plt.plot(MyForest.z, MyForest.w, 'r.')

p = 0.7

MyForest = Forest(l, p)
MyForest.SpawnForest()
MyForest.HK()
MyForest.Set_z_w()

plt.plot(MyForest.z, MyForest.w, 'b.')

p = 0.6

MyForest = Forest(l, p)
MyForest.SpawnForest()
MyForest.HK()
MyForest.Set_z_w()

plt.plot(MyForest.z, MyForest.w, 'm.')


plt.axis([0, 100, -15, 0])
plt.xlabel('Cluster size')
plt.ylabel('log(n_s)')
plt.title('Occurence of different cluster sizes for different values of p')
plt.savefig('Cluster_size_big_p.png')
plt.show()
