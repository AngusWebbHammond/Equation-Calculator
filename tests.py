from equation_expression_calculator import equation_expression_calculator
from lexical_analyser import *

print(equation_expression_calculator("32+5"))  # Expect output of 37 (Addition)
print(equation_expression_calculator("32*5"))  # Expect output of 160 (Multiplication)
print(equation_expression_calculator("32/5"))  # Expect output of 6.4 (Divison)
print(equation_expression_calculator("32-5"))  # Expect output of 25 (Subtraction)
print(equation_expression_calculator("4^3"))  # Expect output of 64 (Power)
print(
    equation_expression_calculator("(2+(324*3/43+32)^2)+34")
)  # Expect output of 3017.66792861006 (Brackets)


print(
    lexical_analyser("32+5")
)  # Expect output of [['32', '+', '5'], ['INTEGER', 'ADDITION', 'INTEGER']]

print(
    token_returner(["32", "+", "5"])
)  # Expect output of ['INTEGER', 'ADDITION', 'INTEGER']

print(lexeme_returner("32+5"))  # Expect output of ['32', '+', '5']
