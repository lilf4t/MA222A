import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import math

############################# Assignment 1 #############################
def euler(f,a,b,y0,n):
    x = np.linspace(a,b,n+1) # x-vektor med n+1 gridpunkter
    y = np.zeros(n+1) # Fördefinition av array med y-värdenna som nollor.
    h = (b-a)/n # Steglängd
    y[0] = y0 # Sätt första komponenten till begynnelsevärdet
    for k in range(n):
        y[k+1] = y[k] + h*f(x[k],y[k]) # Beräkning av y-värdenna med Eulers metod.
    return x,y

def assignment1():
    f = lambda x,y: -2*y
    y0=3
    (x1,y1) = euler(f,0,3,y0,20) # Lös med 20 gridpunkter
    (x2,y2) = euler(f,0,3,y0,150) # Lös med 150 gridpunkter
    
    x = np.linspace(0,3,50) # x-värden för att plotta exakta lösningen
    y = y0 * np.exp(-2*x) # Exakta lösningen
   
    # Plottar av lösningarna
    fig, ax = plt.subplots()
    ax.plot(x1,y1,'+',label='euler, n=20')
    ax.plot(x2,y2,'--',label='euler, n=150')
    ax.plot(x,y,label='exakt')
    ax.legend(fontsize=14)
    ax.set_xlabel('x',fontsize=14)
    ax.set_ylabel('y',fontsize=14)
    ax.tick_params(labelsize=14)
    ax.grid('on')    
    return plt.show()

############################# Assignment 2 #############################
def assignment2():
    # a)
    m = 100 #kg
    k = 0.4 #Ns2/m2
    g = 9.82 #m/s2
    v = math.sqrt((m * g) / k)
    
    # b)
    v0 = 70 #m/s
    
    f= lambda x,y: g-((k/m)*(y**2)) # Definiera högerledet i ekvationen
    sol = integrate.solve_ivp(f,[0,10],[v0],\
    t_eval=np.linspace(0,10,100)) # Tät grid för plottning.
    fig ,ax = plt.subplots()
    ax.plot(sol.t,sol.y[0]) # sol.t ger x-värdenna och sol.y
    # är en matris som innehåller lösningen i första raden.
    ax.legend(fontsize=14)
    ax.set_xlabel('tid [s]',fontsize=14)
    ax.set_ylabel('hastigheten ',fontsize=14)
    ax.tick_params(labelsize=14)
    ax.grid('on')
    
    return print("gränshastighet:", v, "m/s") , plt.show()

############################# Assignment 3 #############################
def assignment3():
    a = np.pi/2
    b = 0
    
    fun = lambda x,y: [y[1], -0.3*y[1] - 1*np.sin(y[0])] # Vi inför funktionen i högerledet som en lambda funktion med två komponenter.
    sol = integrate.solve_ivp(fun,[0,30],[a,b],\
        t_eval=np.linspace(0,30,100)) # Tät grid för plottning.
    fig ,ax = plt.subplots()
    ax.plot(sol.t,sol.y[0]) # sol.t ger x-värdenna och sol.y är en matris som innehåller lösningeni första komponenten.
    ax.set_xlabel('x',fontsize=14)
    ax.set_ylabel('y',fontsize=14)
    ax.tick_params(labelsize=14)
    ax.grid('on')

    return plt.show()

############################# Assignment 4 #############################
def assignment4():
     
    m = k = A = 1      # 1
    w0 = np.sqrt(k/m)  # 1
    w = w0             # ändra värden

    fun = lambda t,x: [x[1], -(k/m)*x[0] + (A/m)*np.cos(w*t)] # Vi inför funktionen i högerledet som en lambda funktion med två komponenter.
    sol = integrate.solve_ivp(fun,[0,100],[0,0],\
        t_eval=np.linspace(0,100,100)) # Tät grid för plottning.
    fig ,ax = plt.subplots()
    ax.plot(sol.t,sol.y[0]) # sol.t ger x-värdenna och sol.y är en matris som innehåller lösningeni första komponenten.
    ax.set_xlabel('Tid',fontsize=14)
    ax.set_ylabel('Amplitud',fontsize=14)
    ax.tick_params(labelsize=14)
    ax.grid('on')

    return plt.show()

############################# Print #############################
# print(assignment1())
print(assignment2())
# print(assignment3())
# print(assignment4())

