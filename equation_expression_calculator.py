from lexical_analyser import lexical_analyser
from syntax_analyser import syntax_analyser
from tree_representer import return_tree_representation

def equation_expression_calculator(input_equation: str) -> int | float | None | SyntaxError:
    if type(input_equation) != str:
        return None
    lexeme_list, token_list = lexical_analyser(input_equation)
    is_syntax_valid = syntax_analyser(token_list)
    
    print(lexeme_list, token_list, is_syntax_valid)
    
    try:
        if not is_syntax_valid[0]:
            return SyntaxError
    except:
        tree_representation = return_tree_representation(lexeme_list, token_list)
    return tree_representation.get_value()
