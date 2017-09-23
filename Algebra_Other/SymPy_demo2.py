import sympy

'''START:
printing mathematical symbols'''

sympy.init_printing()
#This prints out nice LaTex-y stuff.
#TODO: figure out if this can get on a document (without LaTex)
x, y, z, theta = sympy.symbols('x y z theta')
theta**3
#this would print the theta symbol cubed
sympy.factor(2*x**2 + x*y)
#you know it

'''definite integral symbol'''
sympy.Integral(x**3, x)
#LOL the command-line attempt is so hokey
#  /  3
# | x   dx
# /

a, b = sympy.symbols('a b')
sympy.Integral(x**3, (x, a, b))
#  b/  3
#   | x   dx
#  a/

sympy.Integral(x**3, (x, a, b)).doit()
#just does it

Alpha, alpha, Beta, beta = sympy.symbols('Alpha alpha Beta beta')

'''END:
printing mathematical symbols'''