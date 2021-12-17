import sympy as sp
from scipy import linspace, exp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def dxdy(y, x):
    k = 2;
    dydx = -k * y
    return dydx
	
x_sc = np.linspace(0, 10, 100)
y0 = 2**0.5
y_sc = np.array(odeint(dxdy, y0, x_sc)).ravel()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax1.set_title('sympy')
ax2.set_title('scipy')
ax3.set_title('delta')

y = sp.Function('y')
x = sp.Symbol('x', positive = True)
diffeq = sp.Eq(y(x).diff(x) + 2*y(x), 0) 
res = sp.dsolve(diffeq, ics = {y(0):y0}).rhs
f = sp.lambdify(x, res, 'numpy')

ax1.plot(x_sc, f(x_sc))
ax2.plot(x_sc, y_sc)
ax3.plot(x_sc, f(x_sc) - y_sc)

fig.savefig("ep3.png")
