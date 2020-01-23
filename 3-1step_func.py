import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    # 引数に実数しか対応できない(numpy配列を受け付けない)

    #NumPy配列に対し不等号の演算を用いれば各要素にブーリアン型の生成される
    y = x > 0
    
    #astype()メソッドで任意の型（今回はnp.int型）に変更できる
    return y.astype(np.int)


# -5 ~ 5　0.1刻みの配列を生成
input_data = np.arange(-5.0, 5.0, 0.1)
output_data = step_function(input_data)

#グラフデータ生成
plt.plot(input_data, output_data)

#y軸の範囲を設定
plt.ylim(-0.1, 1.1)
plt.show()