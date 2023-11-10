import math


class SimpleCalc:
    res = 0.0

    def __init__(self) -> None:
        self.operators = {
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
            'gcd': lambda res, x: float(math.gcd(int(res), int(x))),
            'help': lambda res, x: self.__help()
        }

    def input(self, inp=None) -> float | int | None:
        if not inp:
            inp = input(f'{self.res} ')
        [operator, number] = (inp.strip().split() + ['0'])[:2]
        try:
            number = float(number) if '.' in number else int(number)
            return self.calc(operator, number)
        except:
            print('Пум пум ОБШИБОЧКА')
    
    def calc(self, operator: str, number: int | float) -> float | int:
        self.res = self.operators[operator](self.res, number)
        return self.res
    
    def __help(self) -> float | int:
        print('Operators:', *self.operators.keys(), sep='\n\t')
        return self.res
