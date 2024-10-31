from lexical_analyser import lexical_analyser

def syntax_analyser (token_list: list) -> tuple[bool, int] | bool:
    print(token_list)
    number_paren_open: int = 0
    is_previous_token_operator: bool = False
    
    for index, token in enumerate(token_list):
        if token == "LPAREN":
            is_previous_token_operator = False
            number_paren_open += 1
            continue
        if token == "RPAREN":
            is_previous_token_operator = False
            number_paren_open -= 1
            if number_paren_open < 0:
                return (False, index)
            continue
        if token == "INTEGER":
            is_previous_token_operator = False
            continue
        if token in ["ADDITION", "SUBTRACT", "MULTIPLY", "DIVISION"]:
            if index == 0:
                return (False, index)
            if is_previous_token_operator == True:
                return (False, index)
            is_previous_token_operator = True
            
    if number_paren_open == 0:
        return True
    else:
        return False

print(syntax_analyser(lexical_analyser("(32+432)*(3234325+322-3432/234)*234324+234234-23423542")[1]))