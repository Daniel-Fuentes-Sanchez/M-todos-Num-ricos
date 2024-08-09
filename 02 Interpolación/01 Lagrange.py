import numpy as np
import matplotlib.pyplot as plt

def Lagrange(X,Y,Grade,Point):

    Sum = 0

    for i in range(Grade):
        
        Product = 1
        
        for j in range(Grade):

            if i != j:
                Product *= (Point - X[j])/(X[i] - X[j])

        Sum += Product*Y[i]

    return Sum

X = [1, 4, 6]
Y = [0, 1.386294, 1.791759]

x = np.linspace(np.min(X),np.max(X),100)
y = np.log(x)

Grade = len(X)
Point = 2

S = Lagrange(X,Y,Grade,Point)

print("Evaluación:", S)

plt.plot(X,Y,"o b")
plt.plot(x,y,"r",label = "Función")

plt.grid(True)

plt.legend(loc = "lower right")

plt.show()