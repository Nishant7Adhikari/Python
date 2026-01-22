import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 10, 400) 
y = x**(1/2) 

plt.plot(x, y) 

plt.xlabel("x") 
plt.ylabel("y") 
plt.title("y = x**(1/2)") 

plt.grid(True) 
plt.show()