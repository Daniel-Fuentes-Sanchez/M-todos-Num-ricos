import numpy as np

def Newton(Function,Derivate,Initial_Aproximation,Tolerance,Iterations):

    i = 0
    p = Initial_Aproximation

    while i <= Iterations:

        p_next = p - Function(p)/Derivate(p)

        if abs(p_next - p) < Tolerance:
            return p_next,i
        
        i = i + 1
        p = p_next

    return p,i

def Function(p):
    return p**3 + 4*p**2 - 10

def Derivate(p):
    return 3*p**2 + 8*p

Initial_Aproximation = 1.5
Tolerance = 1e-4
Iterations = 10

Root,i = Newton(Function,Derivate,Initial_Aproximation,Tolerance,Iterations)
print("       Raíz:", Root)
print("Iteraciones:", i)