import sympy as sp

def analyze_eq(equation):
    x = sp.symbols("x")
    expression = sp.sympify(equation)
    roots = sp.solve(expression, x)
    derivative = sp.diff(expression, x)
    sec_derivative = sp.diff(expression, x, 2)
    y_intercept = expression.subs(x, 0)
    vertex = None


    try:
        polynomial = sp.Poly(expression, x)
        if(polynomial.degree() == 2):
            a = polynomial.coeff_monomial(x**2)
            b = polynomial.coeff_monomial(x)

            x_vertex = -b/(2*a)
            y_vertex = expression.subs(x, x_vertex)


            vertex = [
                str(x_vertex),
                str(y_vertex)                    
            ]

    except sp.PolynomialError:
        pass






    return {
        "Equation": str(expression),
        "Roots": [str(root) for root in roots],
        "Derivative":str(derivative),
        "Second Derivative":str(sec_derivative),
        "Y intercept":str(y_intercept),
        "Vertex": str(vertex)
    }