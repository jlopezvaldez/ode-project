#made by jonathan lopez 09/19/2021
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#our ode model
def model(y,t,k):
    # k = 0.95 test condition
    dydt = (k)/((((k/t)-k + 1)**2)*(t**2)) #derivitve of amdahls law
    return dydt

y0 = 1 #initial condition

t = np.linspace(1,256) #time points

k = .5
y1 = odeint(model,y0,t,args=(k,))

k = .75
y2 = odeint(model,y0,t,args=(k,))

k = .9
y3 = odeint(model,y0,t,args=(k,))

k = .95
y4 = odeint(model,y0,t,args=(k,))

# y = odeint(model,y0,t)

# each different plot for
plt.plot(t,y1, 'r-', linewidth = 2, label='k=0.50')
plt.plot(t,y2, 'b--', linewidth = 2, label='k=0.75')
plt.plot(t,y3, 'g:', linewidth = 2, label='k=0.90')
plt.plot(t,y4, 'k+', linewidth = 2, label='k=0.95')

# this changes the ticks within the plot
# plt.xticks(np.arange(min(t), max(t)+2, 15))

plt.xlabel('Number of Processors n')
plt.ylabel('Speedup Time')
plt.legend()
plt.show()

