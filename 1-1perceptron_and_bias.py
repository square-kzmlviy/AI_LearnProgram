# coding: utf-8
import numpy as np

# 入力値
x=np.array([0,1])

# 重み
w = np.array([0.5, 0.5])

# 入力値
b = -0.7

print(x * w)
print(np.sum(x * w)+b)
