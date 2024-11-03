import unittest
from equation_calculator.analyser import syntax_analyser


class TestLexemeReturner(unittest.TestCase):

    def test_plus_true(self):
        self.assertTrue(
            syntax_analyser.syntax_analyser(["INTEGER", "ADDITION", "INTEGER"])[0]
        )

    def test_minus_true(self):
        self.assertTrue(
            syntax_analyser.syntax_analyser(["INTEGER", "SUBTRACT", "INTEGER"])[0]
        )

    def test_multiply_true(self):
        self.assertTrue(
            syntax_analyser.syntax_analyser(["INTEGER", "MULTIPLY", "INTEGER"])[0]
        )

    def test_divide_true(self):
        self.assertTrue(
            syntax_analyser.syntax_analyser(["INTEGER", "DIVISON", "INTEGER"])[0]
        )

    def test_power_true(self):
        self.assertTrue(
            syntax_analyser.syntax_analyser(["INTEGER", "POWER", "INTEGER"])[0]
        )

    def test_brackets_true(self):
        self.assertTrue(
            syntax_analyser.syntax_analyser(
                [
                    "LPAREN",
                    "INTEGER",
                    "ADDITION",
                    "INTEGER",
                    "RPAREN",
                    "POWER",
                    "LPAREN",
                    "INTEGER",
                    "MULTIPLY",
                    "INTEGER",
                    "RPAREN",
                ],
            )[0]
        )

    def test_brackets_false1(self):
        self.assertFalse(
            syntax_analyser.syntax_analyser(
                [
                    "INTEGER",
                    "ADDITION",
                    "INTEGER",
                    "RPAREN",
                    "POWER",
                    "LPAREN",
                    "INTEGER",
                    "MULTIPLY",
                    "INTEGER",
                    "RPAREN",
                ],
            )[0]
        )

    def test_brackets_false2(self):
        self.assertFalse(
            syntax_analyser.syntax_analyser(
                [
                    "INTEGER",
                    "ADDITION",
                    "INTEGER",
                    "RPAREN",
                    "POWER",
                    "LPAREN",
                    "INTEGER",
                    "MULTIPLY",
                    "INTEGER",
                ],
            )[0]
        )

    def test_brackets_false3(self):
        self.assertFalse(
            syntax_analyser.syntax_analyser(
                [
                    "LPAREN",
                    "INTEGER",
                    "ADDITION",
                    "INTEGER",
                    "RPAREN",
                    "POWER",
                    "LPAREN",
                    "INTEGER",
                    "MULTIPLY",
                    "INTEGER",
                    "RPAREN",
                    "RPAREN",
                ],
            )[0]
        )


if __name__ == "__main__":
    unittest.main()
