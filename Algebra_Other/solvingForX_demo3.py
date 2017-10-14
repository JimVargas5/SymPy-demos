import sympy as sympy
import cmath
# cmath is not necesssary

sympy.init_printing()

a, b, x, y, z = sympy.symbols('a b x y z')

'''START:
Roots of polynomials'''

sympy.Eq(x**2 - x, 0)
# x squared minus x equals zero

sympy.solve(x**2 - x, x)
# roots [0,1]

sympy.solve(x**(-2) - x, x)
# complex roots [-sqrt(2*i),sqrty(2*i)]

sympy.factor(x**2 - 4)
# (x-2)(x+2)

sympy.simplify((x-2)*(x+2))
# simplifies

eq = (x**3 + x**2 - x -1)/(x**2 + 2*x + 1)
sympy.factor(eq)
# x - 1
# will factor and then cancel out/simplify

sympy.factor_list(eq)
# (1, [(x - 1, 1), (x + 1, 2)])
# one factor of (x - 1), two factors of (x + 1)

eq2 = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
sympy.apart(eq2)
# gives partial fractions
# (2x-1)/(x**2+x+1)-(1)/(x+4)+(3/x)
# simplify(the answer) will put the partial fractions back

sympy.solve([x + y - 1, x - y - 1], [x,y])
# can do system of equations, they must go into square brackets
# {x:1, y:0}

'''END:
Roots of polynomials'''