import matplotlib.pyplot as plt
import numpy as np
i=np.arange(-4*(np.pi),4*(np.pi),0.1)
y=np.sin(i)
plt.plot(i,y)#adding legend
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('my first graph')
plt.show()
