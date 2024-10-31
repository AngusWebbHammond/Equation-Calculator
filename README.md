# Mathematical Equation Compiler

Uses Python to convert a mathematical equation from string to calculated value

## Equation Calculator

Takes as an input the equation string, and returns the calculated value using .get_value() of the Expression class

## Lexical Analyser

The lexical analyser is comprised of two different functions, lexeme_returner and token_returner.
The input is an equation string, which returns both the lexeme list and the token list, which can then be further interpretated by the Syntax analyser and then be converted to a tree to be calculated.

### Lexeme Returner

This takes in a string and returns a list of strings.

#### Current Valid Lexemes

- Any Natural Number
- Basic Operators: +, -, /, \*
- Left and Right Brackets

### Token Returner

This takes in a list of strings from the Lexeme Returner and returns a list of Tokens.

## Syntax Analyser

This takes in a list of Tokens and returns if true or false, if false, then it will return the index of the token list, for any error messages.

## Tree Representer

Takes the lexeme and token lists and returns an expression which is of class Expression, that can be have get_value() called to calculate the equation
