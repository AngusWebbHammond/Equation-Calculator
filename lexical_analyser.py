def lexical_analyser (input_equation: str) -> list:
    lexeme_list = lexeme_returner(input_equation)
    token_list = token_returner(lexeme_list)
    return [lexeme_list, token_list]

def lexeme_returner (input_equation: str) -> list:
    lexeme_list: list = []
    currently_checked_value: str = ""
    previous_type = str
    for value in input_equation:
        try:
            if type(int(value)) == int:
                if previous_type == int:
                    currently_checked_value = currently_checked_value + value
                else:
                    currently_checked_value = value
                previous_type = int
        except:
            if previous_type == int:
                lexeme_list.append(currently_checked_value)
                lexeme_list.append(value)
                previous_type = ""
                currently_checked_value = ""
            else:
                lexeme_list.append(value)
                previous_type = ""
                currently_checked_value = ""

    if previous_type == int:
        lexeme_list.append(currently_checked_value)
    
    return lexeme_list

def token_returner(lexeme_list: list) -> list:
    token_list: list = []
    for lexeme in lexeme_list:
        try:
            if type(int(lexeme)) == int:
                token_list.append("INTEGER")
        except:
            if lexeme == "+":
                token_list.append("ADDITION")
            elif lexeme == "-":
                token_list.append("SUBTRACT")
            elif lexeme == "/":
                token_list.append("DIVIDE")
            elif lexeme == "*":
                token_list.append("MULTIPLY")
            elif lexeme == "(":
                token_list.append("LPAREN")
            elif lexeme == ")":
                token_list.append("RPAREN")
            else:
                print("Not a valid lexeme, either add a new lexeme to the token list, or retype the equation.")
            
    return token_list

print(lexical_analyser("(32+432)*(3234325+322-3432/234)"))
