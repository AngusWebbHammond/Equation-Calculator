from equation_classes import Expression, Integer, Operator

def return_tree_representation(lexeme_list: list, token_list: list) -> Expression:
    compressed_lists: list[list, list] = [lexeme_list, token_list]
    for index, [lexeme, token] in enumerate(zip(lexeme_list, token_list)):
        if token in ["ADDITION", "SUBTRACT", "MULTIPLY", "DIVISION"]:
            expression = Operator(Integer(lexeme_list[index-1]), Integer(lexeme_list[index+1]), token)
        else:
            pass
    return expression
