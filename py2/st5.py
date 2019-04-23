
# 行列の足し算
import numpy as np
A = np.matrix([[50, 40], [10, 10]])
B = np.matrix([[30, 100], [20, 15]])
A + B
0.8 * A

# 行列の掛け算
A = np.matrix([[1, 3], [2, 1]])
B = np.matrix([[150, 250], [130, 230]])
A * B

# 逆行列
A = np.matrix([[5, 3], [2, 1]])
B = np.linalg.inv(A)

# 逆行列で連立方程式を解く
A = np.matrix([[5, 3], [2, 1]])
inv_A = np.linalg.inv(A)
B = np.matrix([[9], [4]])
inv_A * B

# ベクトルと行列
import numpy as np
p = np.matrix([[3], [2]])
A = np.matrix([[2, 0], [1, 2]])
A * p

# x軸に対して線対称
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

p = np.matrix([[1, 3, 3, 1], [1, 1, 2, 1]])

A = np.matrix([[1, 0], [0, -1]])

p2 = A * p
print(p2)

p = np.array(p)
p2 = np.array(p2)
plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color='0.8')
plt.show()

# 図形の相似拡大
p = np.matrix([[1, 1, 2, 1], [3, 1, 1, 3]])

A = np.matrix([[3, 0], [0, 3]])

p2 = A * p
print(p2)

p = np.array(p)
p2 = np.array(p2)
plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color='0.8')
plt.show()
