import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

############################# Assignment 1 #############################
def assignment1():
    # trapets metod
    def trapets(fun, a, b, n):
        h = (b - a) / n  # n delintervall
        x = np.linspace(a, b, n + 1)  # n+1 griddpunkter
        y = fun(x)
        return h * (np.sum(y[1:-1]) + 0.5 * (y[0] + y[-1]))

    f = lambda x: np.log(1 + np.sin(x)) * np.cos(x)
    I10 = trapets(f, 0, np.pi / 2, 10)
    I100 = trapets(f, 0, np.pi / 2, 100)
    I1000 = trapets(f, 0, np.pi / 2, 1000)

    return "\n n=10: " + str(I10) + "\n n=100: " + str(I100) + "\n n=1000: " + str(I1000)

############################# Assignment 2 #############################
def assignment2():
    I, tol= integrate.quad(lambda x:(np.exp(-x)*np.cos(x)), 0, np.inf)
    return str(I), str(tol)

############################# Assignment 3 #############################
# (a)
def assignment3():
    t = np.linspace(0,4*np.pi,100); # Generera vektor t med element från 0 till 4 pi
    x = 5*t-(5*np.sin(t)); # Beräkna x-koordinaterna för motsvarande t
    y = 5-5*np.cos(t); # Beräkna y-koordinaterna för motsvarande t
    plt.plot(x,y) # Plotta kurvan
    plt.xlabel('x') # Skriv text på x-axeln
    plt.ylabel('y') # Skriv text på y-axeln
    plt.grid() # Lägg in rutnät
    
    # (b)
    L, tol= integrate.quad(lambda t:np.sqrt((5 - 5*np.cos(t))**2 + (5*np.sin(t))**2), 0,4*np.pi)
    return str(L), str(tol)

############################# Assignment 4 #############################
def assignment4():
    L,tol=integrate.quad(lambda x:np.sqrt(1 + (0.2*x)**2), -5, 5)
    
    return str(L), str(tol)

############################# Print #############################
# print(assignment1())
# print(assignment2())
# print(assignment3())
# print(assignment4())
