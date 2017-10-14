import sympy as sympy

'''START:
Limits'''

sympy.init_printing()

a, b, x, y, z = sympy.symbols('a b x y z')

sympy.Limit(sympy.sin(x) / x, x, 0)
#(symbolic) (expression, variable of limit, 
#               what the variable of the limit is apprpaching)

sympy.limit(sympy.sin(x) / x, x, 0)
# 1

sympy.Limit(1/x, x, sympy.oo)
# lim_x->infinity [a/x]

sympy.Limit(1./x, x, 0, dir='+')
# limit from the positive side
# one is a float

sympy.Limit(1./x, x, -sympy.oo, dir='-').doit()
# limit to -infinity from the negative side

'''END:
Limits'''

