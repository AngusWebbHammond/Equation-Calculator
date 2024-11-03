import unittest
import equation_calculator.equation_expression_calculator as eq


class TestEquationExpressionCalcuator(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(eq.equation_expression_calculator("2+3"), 5)

    def test_minus(self):
        self.assertEqual(eq.equation_expression_calculator("2-3"), -1)

    def test_multiply(self):
        self.assertEqual(eq.equation_expression_calculator("2*3"), 6)

    def test_divide(self):
        self.assertEqual(eq.equation_expression_calculator("2/3"), 2 / 3)

    def test_power(self):
        self.assertEqual(eq.equation_expression_calculator("2^3"), 8)

    def test_brackets(self):
        self.assertEqual(eq.equation_expression_calculator("(2+3)^(2*3)"), 15625)


if __name__ == "__main__":
    unittest.main()
