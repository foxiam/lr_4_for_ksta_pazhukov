import math


class SimpleCalc:
    """Класс простого калькулятора"""
    res = 0.0

    def __init__(self) -> None:
        """
        Инициализация операторов
        """

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
        """
        Метод ввода оператора и числа из консоли
        Args:
            inp:    str строка с оператором и числом(опционально).

        Examples:
            >>> calculator = SimpleCalc()
            >>> calculator.input('+ 5')
            5.0
            >>> calculator.input()
            input * 3
            15.0

        Returns:
            float | int | None результат расчетов
        """

        if not inp:
            inp = input(f'{self.res} ')
        try:
            [operator, number] = (inp.strip().split() + ['0'])[:2]
            number = float(number) if '.' in number else int(number)
            return self.calc(operator, number)
        except:
            print('Пум пум ОБШИБОЧКА')
    
    def calc(self, operator: str, number: int | float = 0.0) -> float | int:
        """
        Метод ввода оператора и числа из консоли
        Args:
            operator:    str оператор.
            number:      int | float число(опционально)

        Examples:
            >>> calculator = SimpleCalc()
            >>> calculator.calc('+', 5.5)
            5.0
            >>> calculator.calc('round_up')
            6

        Returns:
            float | int | None результат расчетов
        """

        self.res = self.operators[operator](self.res, number)
        return self.res
    
    def __help(self) -> float | int:
        """
        Вывод всех доступных операторов в консоль
        """

        print('Operators:', *self.operators.keys(), sep='\n\t')
        return self.res
