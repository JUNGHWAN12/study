import numpy as np
import matplotlib.pylab as plt

# 시그모이드 함수
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.title("sigmoid function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()