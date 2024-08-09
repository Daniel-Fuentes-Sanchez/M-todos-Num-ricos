import numpy as np

def Neville(Evaluate, X, Y):

    n = len(X)
    Q = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):

        Q[i][0] = Y[i]

    for i in range(n):
        
        for j in range(1,i+1):
            
            Q[i][j] = ((Evaluate - X[i-j])*Q[i][j-1] - (Evaluate - X[i])*Q[i-1][j-1])/(X[i] - X[i-j])

    return Q[n-1][n-1]

X = [1.0,1.3,1.6,1.9,2.2]
Y = [0.7651977,0.6200860,0.4554022,0.2818186, 0.1103623]

Evaluate = 1.5

N = Neville(Evaluate, X, Y)

print("Evaluación:", N)