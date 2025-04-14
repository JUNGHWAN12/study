#다중 신경망 구현 및 정리
import numpy as np

def sigmoid(x): # 시그모이드 함수
    return 1 / (1 + np.exp(-x))

def identity_function(x): # 항등 함수
    return x 

def softmax(a): # 소프트맥스 함수
    c = np.max(a) # 오버플로우 방지
    exp_a = np.exp(a - c) # 지수 함수
    sum_exp_a = np.sum(exp_a) # 합
    y = exp_a / sum_exp_a # 소프트맥스 함수
    return y

# 신경망 초기화
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

# 신경망의 순전파 구현
# 입력층 -> 은닉층 1 -> 은닉층 2 -> 출력층
def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    A1 = np.dot(x, W1) + b1
    Z1 = sigmoid(A1)
    A2 = np.dot(Z1, W2) + b2
    Z2 = sigmoid(A2)
    A3 = np.dot(Z2, W3) + b3
    Y = identity_function(A3)

    return Y
network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print("=========최종출력===========")
print(y)  # [0.3  0.7]
print("============================")