#행렬을 활용한 신경망 구현

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([1.0, 0.5])
#1단계 신경망의 가중치와 편향
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])


#2단계 신경망의 가중치와 편향
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

# 1단계 신경망 행렬의 곱셈
A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)
print("=========1단계 신경망===========")
print(A1)  # [0.3 0.7 1.1]
print(Z1)  # [0.57444252 0.66818777 0.75026011]
print("============================")

# 2단계 신경망 행렬의 곱셈
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print("=========2단계 신경망===========")
print(A2)  # [0.615 1.25 ]
print(Z2)  # [0.649 0.777]
print("============================")


# 항등 함수
def identity_function(x):
    return x
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)
print("=========최종출력===========")
print(A3)  # [0.6  1.2]
print(Y)  # [0.6  1.2]
print("============================")