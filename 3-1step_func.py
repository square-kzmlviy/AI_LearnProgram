import numpy as np

def step_function(x):
    # 引数に実数しか対応できない(numpy配列を受け付けない)

    #NumPy配列に対し不等号の演算を用いれば各要素にブーリアン型の生成される
    y = x > 0
    
    #astype()メソッドで任意の型（今回はnp.int型）に変更できる
    return y.astype(np.int)

input_data = np.array([1.0, 2.0, 3, 0])
output_data = step_function(input_data)
print(output_data)