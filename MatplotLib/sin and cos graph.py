# sin x and cosx graph using matplot lib

import numpy as np 
import matplotlib.pyplot as plt 

print(np.pi)

x =np.arange(0, 5*np.pi, 0.1)
y_sinx = np.sin(x)
y_cosx = np.cos(x)
y_tanx = np.tan(x)

plt.subplot(2, 2, 1)
plt.plot(x, y_sinx,'r--')
plt.title('Sin_ X')

plt.subplot(2, 2, 2)
plt.plot(x, y_cosx,'g--')
plt.title('Cos_ X')

plt.subplot(2, 2, 3)
plt.plot(x, y_tanx,'y--')
plt.title('Tan_X')

#save figure to save imaage locally
plt.savefig('Sine cosine Graph.png')
plt.show()
