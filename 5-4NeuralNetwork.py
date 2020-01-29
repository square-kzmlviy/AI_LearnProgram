import numpy as np
def sigmoid_function(x):

    return 1 / (1 + np.exp(-x))

def identity_function(x):
    return x


def init_data():
    data = {}
    #1層目の重み（数値は適当）
    data['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])

    #2層目の重み（数値は適当）
    data['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])

    #3層目の重み（数値は適当）
    data['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])

    #1層目のバイアス
    data['B1'] = np.array([0.1, 0.2, 0.3])

    #2層目のバイアス
    data['B2'] = np.array([0.1, 0.2])

    #3層目のバイアス
    data['B3'] = np.array([0.1, 0.2])

    return data

def run(data,x):
    W1, W2, W3 = data['W1'], data['W2'], data['W3']
    B1, B2, B3 = data['B1'], data['B2'], data['B3']
    
    A1 = np.dot(X, W1) + B1
    Z1 = sigmoid_function(A1)

    A2 = np.dot(Z1, W2) + B2
    Z2 = sigmoid_function(A2)

    A3 = np.dot(Z2, W3) + B3
    Y = identity_function(A3)

    return Y

NN_data = init_data()
#入力値
X = np.array([1.0, 0.5])
Y = run(NN_data, X)
print(Y)
