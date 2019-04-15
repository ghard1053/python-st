
# グラフ描画
%matplotlib inline
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [61, 62, 63, 62, 67, 58, 54]

plt.plot(x, y)
plt.grid(color='0.8')
plt.slow()


# y = 3x
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1.0, 1.01, 0.01)
y = 3 * x

plt.plot(x, y)
plt.grid(color='0.8')
plt.show()


# 連立方程式
from sympy import Symbol, solve

a = Symbol('a')
b = Symbol('b')
ex1 = a + b - 1
ex2 = 5*a + b -3

print(solve((ex1, ex2)))


# 直交
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 6)
y = 1/2 * x + 1/2
y2 = -2 * x + 7

plt.plot(x, y)
plt.plot(x, y2)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()
