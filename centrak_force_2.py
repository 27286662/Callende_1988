import numpy as np
import matplotlib.pyplot as plt
#Import math Library
import math 

def plot_effective_potential(p_phi,m,g): 
    # Generate data points
    r = np.linspace(0.3, 5, 1000)
    plt.figure()
    color = iter(plt.cm.rainbow(np.linspace(0, 1, 10)))
    for k in range(1, 10,1):
        k = k/10
        print(k)
        c = next(color)
        V_eff = p_phi**2/(2*m*r**2) - g**2 * np.exp(-k*m*r)/(r) 
            # Plot the potential values
        plt.plot(r, V_eff, c=c  ,label='k='+str(k))
    
    # Adding legend, which helps us recognize the curve according to it's color
    plt.legend()    
    plt.xlabel('r') 
    plt.ylabel('V_eff')
    plt.title('posible orbits potential')
    plt.grid(True)
    ######################################plt.axis('equal')
    
    # range in y
    plt.axis([0.3,5,-0.8,1])
    plt.show()



# Example usage
# k = 1  # constant
m = 1  # mass
p_phi = 1 # Volocity
g = 1.15 # constant 
plot_effective_potential(p_phi, m, g)