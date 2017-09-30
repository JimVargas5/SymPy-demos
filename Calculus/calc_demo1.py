import sympy as sympy

'''START:
Derivatives and Partial Derivatives'''

sympy.init_printing()

a, b, x, y, z = sympy.symbols('a b x y z')

f = sympy.cos(x * y) + sympy.sin(z * x)
f
sympy.Derivative(f, x)
#(symbolic) partial derivative of f wrt x

sympy.Derivative(f, x, x)
#(symbolic) second partial derivative of f wrt x

sympy.Derivative(f, x, 1, y, 3, z, 2)
#(symbolic) long (sixth in total) partial derivative thing of f wrt:
# x once, y three times, z twice

sympy.diff(f, x)
#this is proper, derivative of f wrt x

sympy.Derivative(f, x).doit()
#prints and does it

'''END:
Derivatives and Partial Derivatives'''

'''START:
Integrals'''

sympy.Integral(sympy.sin(x), (x))
#prints indefinite integral

sympy.Integral(sympy.sin(x), (x, 0, sympy.pi))
#prints definite of integral from 0 to pi

sympy.integrate(sympy.sin(x), (x, 0, sympy.pi))
#(proper) does the integration

sympy.integrate((x**2) * (sympy.sin(x)), (x))
#this integral requires the product rule for integration
# -1*x**2 * cos(x) + 2*x * sin(x) + 2*cos(x) 
#does not include a '+ c'

num = x**2 + 4*x - 12
denom = 3*x + 2
sympy.integrate((num) / (denom), (x))
#integral with quotionet of two functions
# (x**2)/6 + (10*x)/9 - (128/27)*log(27*x + 18)
# 'log' refers to the natural log

'''END:
Integrals'''
