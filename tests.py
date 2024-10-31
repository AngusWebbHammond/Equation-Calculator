from equation_expression_calculator import equation_expression_calculator
from lexical_analyser import *

print(equation_expression_calculator("32+5"))  # Expect output of 37
print(equation_expression_calculator("32*5"))  # Expect output of 160
print(equation_expression_calculator("32/5"))  # Expect output of 6.4
print(equation_expression_calculator("32-5"))  # Expect output of 25

print(
    lexical_analyser("32+5")
)  # Expect output of [['32', '+', '5'], ['INTEGER', 'ADDITION', 'INTEGER']]

print(
    token_returner(["32", "+", "5"])
)  # Expect output of ['INTEGER', 'ADDITION', 'INTEGER']

print(lexeme_returner("32+5"))  # Expect output of ['32', '+', '5']
