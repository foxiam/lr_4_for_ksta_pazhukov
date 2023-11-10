class SimpleCalc:
    res = 0.0
    operators = {
        '+': lambda res, x: res + x,
        '-': lambda res, x: res - x,
        '*': lambda res, x: res * x,
        '/': lambda res, x: res / x,
        '%': lambda res, x: res % x,
     }
    
    def calc(self, operator: str, number: int | float):
        try:
            self.res = self.operators[operator](self.res, number)
            return self.res
        except:
            print('Пум пум ОБШИБОЧКА')