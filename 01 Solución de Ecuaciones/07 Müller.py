import numpy as np

def Muller(Function,p_0,p_1,p_2,Tolerance,Iterations):

    h_1 = p_1 - p_0
    h_2 = p_2 - p_1

    delta_1 = (Function(p_1) - Function(p_0))/h_1
    delta_2 = (Function(p_2) - Function(p_1))/h_2

    d = (delta_2 - delta_1)/(h_2 + h_1)
    
    i = 2

    while i <= Iterations:

        b = delta_2 + h_2*d
        D = np.sqrt(b**2 - 4*Function(p_2)*d) if abs(b ** 2 - 4 * Function(p_2) * d) >= 0 else 0

        if abs(b - D) < abs(b + D):
            E = b + D

        else:
            E = b - D
        
        h = -2*Function(p_2)/(b+D)
        p = p_2 + h

        if abs(h) < Tolerance:
            return p,i
        
        p_0 = p_1
        p_1 = p_2
        p_2 = p

        h_1 = p_1 - p_0
        h_2 = p_2 - p_1

        delta_1 = (Function(p_1) - Function(p_0))/h_1
        delta_2 = (Function(p_2) - Function(p_1))/h_2

        d = (delta_2 - delta_1)/(h_2 + h_1)
        i = i+1

    return p,i        

def Function(x):
    return x**4 - 3*x**3 + x**2 + x + 1

p_0 = 0.5
p_1 = 1.0
p_2 = 1.5

Tolerance  = 1e-5
Iterations = 20

Root,i = Muller(Function,p_0,p_1,p_2,Tolerance,Iterations)

print("       Raíz:", Root)
print("Iteraciones:", i)