import numpy as np 
import sympy as smp 
from sympy import *
import matplotlib.pyplot as plt

x = smp.symbols(' x ')
N = 10
f = smp.atan(x)
f_taylor = f.subs(x,0)

for i in range(1, N):
    f_taylor += smp.diff(f, x, i).subs(x, 0)*(x-0)**i / smp.factorial(i)
        
pretty_print(f_taylor)

f_num = smp.lambdify(x, f)
f_taylor_num = smp.lambdify(x, f_taylor)

x = np.linspace(-1, 1, 1000)
y = f_taylor_num(x)

plt.plot(x,y)
plt.plot(x, f_num(x), ':')
plt.show()
