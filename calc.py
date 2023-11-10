import math


class SimpleCalc:
    res = 0.0
    operators = {
        '+': lambda res, x: res + x,
        '-': lambda res, x: res - x,
        '*': lambda res, x: res * x,
        '/': lambda res, x: res / x,
        '%': lambda res, x: res % x,
        'log': lambda res, x: math.log(res, x),
        'sin': lambda res, x: math.sin(res),
        'cos': lambda res, x: math.cos(res),
        'tg': lambda res, x: math.tan(res),
        'round_math': lambda res, x: round(res),
        'round_up': lambda res, x: math.ceil(res),
        'round_down': lambda res, x: math.floor(res),
        'gcd': lambda res, x: math.gcd(res)
    }

    def input(self):
        inp = input(f'{self.res} ')
        [operator, number] = (inp.strip().split() + ['0'])[:2]
        number = float(number) if '.' in number else int(number)
        self.calc(operator, number)
    
    def calc(self, operator: str, number: int | float):
        try:
            self.res = self.operators[operator](self.res, number)
            return self.res
        except:
            print('Пум пум ОБШИБОЧКА')