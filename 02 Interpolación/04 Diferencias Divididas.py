def Diferencias_Divididas(Evaluate,X,Y):

    n = len(X)

    F = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):

        F[i][0] = Y[i]

    for j in range(1,n):

        for i in range(j,n):
            
            F[i][j] = (F[i][j-1] - F[i-1][j-1])/(X[i] - X[i-j])

    S = F[0][0]
    
    for i in range(1,n):

        Prod = F[i][i]

        for j in range(i):

            Prod *= (Evaluate - X[j])

        S += Prod

    return S
    
Evaluate = 1.5

X = [1.0,1.3,1.6,1.9,2.2]
Y = [0.7651977,0.6200860,0.4554022,0.2818186, 0.1103623]

R = Diferencias_Divididas(Evaluate,X,Y)

print("Evaluación:", R)