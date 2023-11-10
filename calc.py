class SimpleCalc:
    res = 0.0
    operators = {
        '+': lambda res, x: res + x,
        '-': lambda res, x: res - x,
        '*': lambda res, x: res * x,
        '/': lambda res, x: res / x,
        '%': lambda res, x: res % x,
     }