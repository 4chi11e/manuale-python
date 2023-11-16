# tutorial ed esempi in questi siti:
# https://numpy.org/doc/stable/user/quickstart.html
# https://apmonitor.com/che263/index.php/Main/PythonPlots

import numpy as np
from numpy import pi
x = np.linspace(0,2*pi,100) # 100 valori nell'intervallo 0 2pi
# x = np.arange(0, 2*pi, 0.1) # valori nell'intervallo 0 2pi con passo 0.1
y = np.sin(x)
z = np.cos(x)
A = np.array([1,1])

import matplotlib.pyplot as plt
plt.plot(x,y,'r--',linewidth=3)
plt.plot(x,z,'k:',linewidth=2)
plt.plot(A[0],A[1],'o', label='A')
plt.legend(['y','z', 'A'])
plt.xlabel('x')
plt.ylabel('values')
# plt.xlim([0, 3])
# plt.ylim([-1.5, 1.5])
plt.savefig('myFigure.png')
plt.savefig('myFigure.eps')
plt.show()