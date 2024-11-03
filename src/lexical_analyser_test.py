import unittest
from equation_calculator.analyser import lexical_analyser


class TestLexemeReturner(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(lexical_analyser.lexeme_returner("2+3"), ["2", "+", "3"])

    def test_minus(self):
        self.assertEqual(lexical_analyser.lexeme_returner("2-3"), ["2", "-", "3"])

    def test_multiply(self):
        self.assertEqual(lexical_analyser.lexeme_returner("2*3"), ["2", "*", "3"])

    def test_divide(self):
        self.assertEqual(lexical_analyser.lexeme_returner("2/3"), ["2", "/", "3"])

    def test_power(self):
        self.assertEqual(lexical_analyser.lexeme_returner("2^3"), ["2", "^", "3"])

    def test_brackets(self):
        self.assertEqual(
            lexical_analyser.lexeme_returner("(2+3)^(2*3)"),
            ["(", "2", "+", "3", ")", "^", "(", "2", "*", "3", ")"],
        )


class TestTokenReturner(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(
            lexical_analyser.token_returner(["2", "+", "3"]),
            ["INTEGER", "ADDITION", "INTEGER"],
        )

    def test_minus(self):
        self.assertEqual(
            lexical_analyser.token_returner(["2", "-", "3"]),
            ["INTEGER", "SUBTRACT", "INTEGER"],
        )

    def test_multiply(self):
        self.assertEqual(
            lexical_analyser.token_returner(["2", "*", "3"]),
            ["INTEGER", "MULTIPLY", "INTEGER"],
        )

    def test_divide(self):
        self.assertEqual(
            lexical_analyser.token_returner(["2", "/", "3"]),
            ["INTEGER", "DIVISION", "INTEGER"],
        )

    def test_power(self):
        self.assertEqual(
            lexical_analyser.token_returner(["2", "^", "3"]),
            ["INTEGER", "POWER", "INTEGER"],
        )

    def test_brackets(self):
        self.assertEqual(
            lexical_analyser.token_returner(
                ["(", "2", "+", "3", ")", "^", "(", "2", "*", "3", ")"]
            ),
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
        )


class TestLexicalAnalyser(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(
            lexical_analyser.lexical_analyser("2+3"),
            [["2", "+", "3"], ["INTEGER", "ADDITION", "INTEGER"]],
        )

    def test_minus(self):
        self.assertEqual(
            lexical_analyser.lexical_analyser("2-3"),
            [["2", "-", "3"], ["INTEGER", "SUBTRACT", "INTEGER"]],
        )

    def test_multiply(self):
        self.assertEqual(
            lexical_analyser.lexical_analyser("2*3"),
            [["2", "*", "3"], ["INTEGER", "MULTIPLY", "INTEGER"]],
        )

    def test_divide(self):
        self.assertEqual(
            lexical_analyser.lexical_analyser("2/3"),
            [["2", "/", "3"], ["INTEGER", "DIVISION", "INTEGER"]],
        )

    def test_power(self):
        self.assertEqual(
            lexical_analyser.lexical_analyser("2^3"),
            [["2", "^", "3"], ["INTEGER", "POWER", "INTEGER"]],
        )

    def test_brackets(self):
        self.assertEqual(
            lexical_analyser.lexical_analyser("(2+3)^(2*3)"),
            [
                ["(", "2", "+", "3", ")", "^", "(", "2", "*", "3", ")"],
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
            ],
        )


if __name__ == "__main__":
    unittest.main()
