import numpy as np

def Secante(Function,Initial_Aproximation_0,Initial_Aproximation_1,Tolerance,Iterations):

    i = 1
    p_0 = Initial_Aproximation_0
    p_1 = Initial_Aproximation_1

    q_0 = Function(p_0)
    q_1 = Function(p_1)

    while i <= Iterations:

        p = p_1 - q_1*(p_1 - p_0)/(q_1 - q_0)

        if abs(p - p_1) < Tolerance:
            return p,i
        
        i = i+1
        
        p_0 = p_1
        q_0 = q_1
        p_1 = p
        q_1 = Function(p)

    return p,i

def Function(p):
    return p**3 + 4*p**2 - 10

Initial_Aproximation_0 = 0.5
Initial_Aproximation_1 = (np.pi)/4

Tolerance  = 1e-4
Iterations = 10

Root,i = Secante(Function,Initial_Aproximation_0,Initial_Aproximation_1,Tolerance,Iterations)
print("       Raíz:", Root)
print("Iteraciones:", i)