import numpy as np

def Fix_Point(Function,Initial_Aproximation,Tolerance,Iterations):

    i = 0
    p = Initial_Aproximation

    while i < Iterations:

        p_next = Function(p)

        if abs(p_next - p) < Tolerance:
            return p_next,i
        
        i = i + 1
        p = p_next
        
    return p,i

def Function(p):
    return (1/2)*(10-p**3)**(1/2)

Initial_Aproximation = 1.5
Tolerance = 1e-4
Iterations = 30

Root,i = Fix_Point(Function,Initial_Aproximation,Tolerance,Iterations)
print("       Raíz:", Root)
print("Iteraciones:", i)