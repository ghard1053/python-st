
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
