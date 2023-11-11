import math
import unittest
from calc import SimpleCalc

class TestSimpleCalc(unittest.TestCase):

    def test_calc_plus(self):
        calculator = SimpleCalc()
        calculator.input('+ 5')
        self.assertEqual(calculator.input('+ 7'), 12.0)
    
    def test_calc_minus(self):
        calculator = SimpleCalc()
        calculator.input('- 5')
        self.assertEqual(calculator.input('- 7'), -12.0)

    def test_calc_mul(self):
        calculator = SimpleCalc()
        calculator.input('+ 5')
        self.assertEqual(calculator.input('* 7'), 35.0)

    def test_calc_div(self):
        calculator = SimpleCalc()
        calculator.input('+ 5')
        self.assertEqual(calculator.input('/ 2'), 2.5)

    def test_calc_div(self):
        calculator = SimpleCalc()
        calculator.input('+ 5')
        self.assertEqual(calculator.input('/ 2'), 2.5)

    def test_calc_rem_div(self):
        calculator = SimpleCalc()
        calculator.input('+ 5')
        self.assertEqual(calculator.input('% 2'), 1.0)

    def test_calc_log(self):
        calculator = SimpleCalc()
        calculator.input('+ 5')
        self.assertEqual(calculator.input('log 2'), math.log2(5))
        
    def test_calc_rem_sin(self):
        calculator = SimpleCalc()
        calculator.input('+ 5')
        self.assertEqual(calculator.input('sin'), math.sin(5))

    def test_calc_rem_cos(self):
        calculator = SimpleCalc()
        calculator.input('+ 5')
        self.assertEqual(calculator.input('cos'), math.cos(5))

    def test_calc_rem_tg(self):
        calculator = SimpleCalc()
        calculator.input('+ 5')
        self.assertEqual(calculator.input('tg'), math.tan(5))

    def test_calc_rem_ctg(self):
        calculator = SimpleCalc()
        calculator.input('+ 5')
        self.assertEqual(calculator.input('ctg'), 1 / math.tan(5))

    def test_calc_round_math(self):
        calculator = SimpleCalc()
        calculator.input('+ 5.4')
        self.assertEqual(calculator.input('round_math'), 5.0)

    def test_calc_round_up(self):
        calculator = SimpleCalc()
        calculator.input('+ 5.4')
        self.assertEqual(calculator.input('round_up'), 6.0)

    def test_calc_round_down(self):
        calculator = SimpleCalc()
        calculator.input('+ 5.6')
        self.assertEqual(calculator.input('round_down'), 5.0)

    def test_calc_gcd(self):
        calculator = SimpleCalc()
        calculator.input('+ 5')
        self.assertEqual(calculator.input('gcd 25'), 5)


if __name__ == '__main__':
    unittest.main()
