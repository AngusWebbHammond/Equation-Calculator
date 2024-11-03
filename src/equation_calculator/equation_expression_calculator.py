from equation_calculator.analyser.lexical_analyser import lexical_analyser
from equation_calculator.analyser.syntax_analyser import syntax_analyser
from equation_calculator.representer.tree_representer import (
    return_tree_representation,
    no_bracket_representation,
)
import sys


def equation_expression_calculator(
    input_equation: str,
) -> int | float | None | str:
    if type(input_equation) != str:
        return None
    lexeme_list, token_list = lexical_analyser(input_equation)
    is_syntax_valid = syntax_analyser(token_list)
    if is_syntax_valid[0] == False:
        sys.exit(
            "Syntax Error with the equation provided, this may be found at index "
            + str(is_syntax_valid[1])
        )
    tree_representation = return_tree_representation(
        *no_bracket_representation(lexeme_list, token_list)
    )
    return tree_representation.get_value()
