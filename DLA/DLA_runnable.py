from DLA import DLA

N = 16
l = 51
g = 300
a = 0
for k in range(N):
    if a == 0:
        dla1 = DLA(l, 601)
    else:
        dla1 = appo
    for i in range(g):
        dla1.OnePiece()
    a += 5
    
    appo = DLA(l+10, 601)
    appo.t = dla1.t
    for i in range(l):
        for j in range(l):
            appo.x[l + 15 + i][l + 15 + j] = dla1.x[l+i][l+j]

    l += 10

dla1.PrintGrid()
