import numpy as np
import matplotlib.pylab as plt

# ReLU 함수
def relu(x):
    return np.maximum(0, x)
x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 5.1)
plt.title("ReLU function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()