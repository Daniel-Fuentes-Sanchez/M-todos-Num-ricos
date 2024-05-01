import numpy as np

def Steffensen(Function,Initial_Aproximation,Tolerance,Iterations):

    i = 0
    
    p_0 = Initial_Aproximation

    while i <= Iterations:

        p_1 = Function(p_0)
        p_2 = Function(p_1)
        p   = p_0 - (p_1 - p_0)**2/(p_2 - 2*p_1 + p_0)

        if abs(p - p_0) < Tolerance:
            return p,i
        
        i = i+1

        p_0 = p

    return p,i

def Function(p):
    return p**3 + 4*p**2 - 10

Initial_Aproximation = 1.5

Tolerance  = 1e-4
Iterations = 10

Root,i = Steffensen(Function,Initial_Aproximation,Tolerance,Iterations)

print("       Raíz:", Root)
print("Iteraciones:", i)