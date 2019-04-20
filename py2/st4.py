
# ベクトルの方向を求める
import math
rad = math.atan2(3, 2)
th = math.degrees(rad)


# ベクトル演算
import numpy as np
a = np.array([2, 2])
b = np.array([2, -1])
a + b
a - b
2 * a


# 直線の方程式
from sympy import Symbol, solve
a = Symbol('a')
b = Symbol('b')
ex1 = -1*a + b - 2
ex2 = 2*a + b - 4
solve((ex1, ex2))


# 直線のなす角度
import math
import numpy as np
a = np.array([2, 7])
b = np.array([6, 1])
c = np.array([2, 3])
d = np.array([6, 5])

va = b - a
vb = d - c

norm_a = np.linalg.norm(va)
norm_b = np.linalg.norm(vb)

dot_ab = np.dot(va, vb)

cos_th = dot_ab / (norm_a * norm_b)
rad = math.acos(cos_th)
deg = math.degrees(rad)


# ベクトルの外積
import numpy as np
a = np.array([0, 1, 2])
b = np.array([2, 0, 0])
np.cross(a, b)


# 三角形の面積
a = np.array([2, 4])
b = np.array([3, 1])
cross_ab = np.cross(a, b)
s = np.linalg.norm(cross_ab)
s / 2
