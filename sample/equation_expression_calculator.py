from lexical_analyser import lexical_analyser
from syntax_analyser import syntax_analyser
from tree_representer import return_tree_representation
import sys


def equation_expression_calculator(
    input_equation: str,
) -> int | float | None | SyntaxError:
    if type(input_equation) != str:
        return None
    lexeme_list, token_list = lexical_analyser(input_equation)
    is_syntax_valid = syntax_analyser(token_list)

    print(lexeme_list, token_list, is_syntax_valid)

    if is_syntax_valid[0] == False:
        sys.exit(
            "Syntax Error with the equation provided, this may be found at index "
            + str(is_syntax_valid[1])
        )
    tree_representation = return_tree_representation(lexeme_list, token_list)
    return tree_representation.get_value()


print(equation_expression_calculator("345344+ 212433-2314324*3"))
