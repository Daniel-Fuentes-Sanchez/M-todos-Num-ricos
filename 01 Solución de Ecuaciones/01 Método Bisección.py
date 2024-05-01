def Bisection(Function,a,b,Tolerance,Iterations):
    
    if Function(a)*Function(b)>=0:
        raise ValueError("La raíz de la función no se ubica en el intervalo establecido.")
    
    i=0

    while (b-a)/2 > Tolerance and i < Iterations:
        
        Midpoint = (a+b)/2

        if Function(Midpoint) == 0:
            return Midpoint,i
        
        elif Function(a)*Function(Midpoint) < 0:
            b = Midpoint
        else:
            a = Midpoint

        i += 1

    return Midpoint,i

def Function(x):
    return x**3 + 4*x**2 - 10

a = 1  
b = 2
Tolerance  = 1e-3 
Iterations = 15

Root, i = Bisection(Function,a,b,Tolerance,Iterations)
print("       Raíz:", Root)
print("Iteraciones:", i)