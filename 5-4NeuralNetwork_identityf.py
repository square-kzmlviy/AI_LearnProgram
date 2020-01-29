import numpy as np
def sigmoid_function(x):

    return 1 / (1 + np.exp(-x))

def identity_function(x):
    return x

#入力値
X = np.array([1.0, 0.5])

#1層目の重み（数値は適当）
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])

#2層目の重み（数値は適当）
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])

#3層目の重み（数値は適当）
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])

#1層目のバイアス
B1 = np.array([0.1, 0.2, 0.3])

#2層目のバイアス
B2 = np.array([0.1, 0.2])

#3層目のバイアス
B3 = np.array([0.1, 0.2])

A1 = np.dot(X, W1) + B1

#シグモイド関数の適応
Z1 = sigmoid_function(A1)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid_function(A2)

A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)
print(A1)
print(Z1)
print(A2)
print(Z2)
print(A3)
print(Y)



