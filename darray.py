import numpy as np

# 행렬의 곱셈
# 1차원 배열과 2차원 배열의 곱셈
# 1차원 배열은 행렬의 행으로 간주되고, 2차원 배열은 행렬로 간주된다.
X = np.array([1,2])
W = np.array([[1, 3, 5], [2, 4, 6]])
Y = np.dot(X, W)
print(Y)  # [ 9 12 15]
