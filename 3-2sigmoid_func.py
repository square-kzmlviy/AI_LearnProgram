import numpy as np
import matplotlib.pylab as plt

def sigmoid_function(x):

    #np.exp(-x)はe^-xを表す
    #スカラ値とNumPy配列の計算出の演算は配列の各要素間で演算される
    return 1 / (1 + np.exp(-x))

input_data = np.arange(-5.0, 5.0, 0.1)
output_data = sigmoid_function(input_data)
plt.plot(input_data, output_data)
plt.ylim(-0.1, 1.1)
plt.show()
