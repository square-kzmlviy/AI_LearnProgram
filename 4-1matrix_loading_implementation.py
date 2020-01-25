import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]])

#.shapeで形状を取得
print(A.shape)

B = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(B.shape)

#np.dotで行列積を取得
C = np.dot(A, B)

print(C.shape)
print(C)