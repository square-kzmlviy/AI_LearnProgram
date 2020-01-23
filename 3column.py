import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    # 引数に実数しか対応できない(numpy配列を受け付けない)

    #NumPy配列に対し不等号の演算を用いれば各要素にブーリアン型の生成される
    y = x > 0
    
    #astype()メソッドで任意の型（今回はnp.int型）に変更できる
    return y.astype(np.int)

def sigmoid_function(x):

    #np.exp(-x)はe^-xを表す
    #スカラ値とNumPy配列の計算出の演算は配列の各要素間で演算される
    return 1 / (1 + np.exp(-x))

input_data1 = np.arange(-5.0, 5.0, 0.1)
output_data1 = step_function(input_data1)

input_data2 = np.arange(-5.0, 5.0, 0.1)
output_data2 = sigmoid_function(input_data2)

#グラフデータ生成
plt.plot(input_data1, output_data1)
plt.plot(input_data2, output_data2)

#y軸の範囲を設定
plt.ylim(-0.1, 1.1)
plt.show()