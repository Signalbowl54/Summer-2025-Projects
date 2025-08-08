import sympy as smp    
import numpy as np
import matplotlib.pyplot as plt

x = smp.symbols('x')
f = x ** 5 
a_0 = 1 / smp.pi * smp.integrate(f, (x, -smp.pi, smp.pi))
a_sum = 0
b_sum = 0

for i in range(1,10):
    a_n = (1 / smp.pi) * smp.integrate(f * smp.cos(i * x),(x, -smp.pi, smp.pi))
    b_n = (1 / smp.pi) * smp.integrate(f * smp.sin(i * x),(x, -smp.pi, smp.pi))
    a_sum += a_n * smp.cos(i * x)
    b_sum += b_n * smp.sin(i * x)

f_series = (1/2 * a_0) + a_sum + b_sum
f_series_num = smp.lambdify(x, f_series)
f_num =  smp.lambdify(x, f)

t =  np.linspace(-np.pi, np.pi , 1000)
y = f_series_num(t)

plt.plot(t, y, label='Fourier Series')
plt.plot(t, f_num(t), ':', label='Original Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Fourier Series Approximation')
plt.show()

smp.pprint(f_series)
