import sympy as sp
from sympy.parsing.latex import parse_latex

def parse_equation(equation):
    return parse_latex(equation, backend="lark")

def analyze_eq(equation):
    x = sp.symbols("x")
    expression = parse_equation(equation)
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
    "equation": str(expression),
    "equation_latex": sp.latex(expression),

    "roots": [str(root) for root in roots],
    "roots_latex": [sp.latex(root) for root in roots],

    "derivative": str(derivative),
    "derivative_latex": sp.latex(derivative),

    "second_derivative": str(sec_derivative),
    "second_derivative_latex": sp.latex(sec_derivative),

    "y_intercept": str(y_intercept),
    "y_intercept_latex": sp.latex(y_intercept),

    "vertex": [sp.latex(value) for value in vertex] if vertex else None
    }



def graph_analysis(equation):


    x = sp.symbols("x")
    expression =  parse_equation(equation)
    num = 500
    start = -10
    stop = 10
    i = start
    step = (stop -  start) /(num -1)
    y_values = []
    x_values = []


    while i<=stop: 
        x_values.append(i)
        y = expression.subs(x, i)
        y = float(y)
        y_values.append(y)
        i = i + step

    

    return {
        "x": x_values,
        "y": y_values

    }

if __name__ == "__main__":
    result = graph_analysis("x**2")
    print(len(result["x"]))
    print(len(result["y"]))
    print(result["x"][0], result["y"][0])
    print(result["x"][-1], result["y"][-1])