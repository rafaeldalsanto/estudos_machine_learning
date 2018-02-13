import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt

x = np.arange(-50, 50, 1)
p = Polynomial([0, 1])
plt.plot(x, p(x), color='blue')
plt.title('y = ax + b')
plt.grid()
plt.show()

x = np.arange(-50, 50, 1)
p = Polynomial([0, 1, 1])
plt.plot(x, p(x), color='blue')
plt.title('y = ax\u00B2 + bx + c')
plt.grid()
plt.show()

x = np.arange(-50, 50, 1)
p = Polynomial([0, 1, 1, 1])
plt.plot(x, p(x), color='blue')
plt.title('y = ax\u00B3 + bx\u00B2 + cx + d')
plt.grid()
plt.show()

x = np.arange(-50, 50, 1)
p = Polynomial([0, 1, 1, 1, 1])
plt.plot(x, p(x), color='blue')
plt.title('y = ax\u2074 + bx\u00B3 + cx\u00B2 + dx + e')
plt.grid()
plt.show()


x = np.arange(-50, 50, 1)
p = Polynomial([0, 1, 1, 1, 1, 1])
plt.plot(x, p(x), color='blue')
plt.title('y = ax\u2075 + bx\u2074 + cx\u00B3 + dx\u00B2 + ex + f')
plt.grid()
plt.show()
