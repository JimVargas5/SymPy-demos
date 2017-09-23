#messin around with SymPy
from sympy import *

'''START:
general algebraic testing'''
print(sqrt(8))
#2*sqrt(2)

x = Symbol('x')
print(limit(sin(x)/x, x, 0))
#1

print(integrate(1/x, x))
#log(x)

r1 = Rational(4,5)
r2 = Rational(5, 4)
print(r1 + r2)
#41/20

print(r1/r2)
#16/25

y = Symbol('y')
xprs1 = x+3
xprs2 = -1 + -3*y - 4*x
print(xprs1+xprs2)
#-3*x - 3*y + 2

print(x*xprs1)
#x*(x + 3)

print(expand(x*xprs2))
#-4*x**2 - 3*x*y - x

print(factor(-4*x**2 - 3*x*y - x))
#-x*(4*x + 3*y + 1)



'''END:
general algebraic testing'''
