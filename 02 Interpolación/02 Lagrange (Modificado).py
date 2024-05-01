import numpy as np
import matplotlib.pyplot as plt

def Lagrange(X,Y,Point):

    Grade = len(X)

    Sum = 0

    for i in range(Grade):
        
        Product = 1
        
        for j in range(Grade):

            if i != j:
                Product *= (Point - X[j])/(X[i] - X[j])

        Sum += Product*Y[i]

    return Sum

def Evaluate(X,Y,Vector):

    n = len(Vector)
    v = np.zeros(n)

    for i in range(n):
        v[i] = Lagrange(X,Y,Vector[i])

    return v

Function = lambda X: np.log(X)
Image    = np.vectorize(Function)

LI = float(input("Límite inferior: "))
LS = float(input("Límite superior: "))
n = int(input("Número de nodos: "))

Point = 2

x = np.linspace(LI,LS,n)
y = Function(x)

vx  = np.linspace(np.min(x),np.max(x),100)
vy = Evaluate(x,y,vx)

VFunction = np.log(vx)

S = Lagrange(x,y,Point)

print("Evaluación:", S)


plt.plot(x,y,"o r")
plt.plot(vx,vy,"b",label = "Estimación")
plt.plot(vx,VFunction,"g",label = "Función")

plt.grid(True)

plt.legend(loc = "lower right")

plt.show()