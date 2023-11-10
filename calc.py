class SimpleCalc:
    res = 0.0
    operators = {
        '+': lambda res, x: res + x,
        '-': lambda res, x: res - x,
        '*': lambda res, x: res * x,
        '/': lambda res, x: res / x,
        '%': lambda res, x: res % x,
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