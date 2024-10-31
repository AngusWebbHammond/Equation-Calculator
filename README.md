# Mathematical Equation Compiler

Uses Python to convert a mathematical equation from string to calculated value

## Functions

### Lexical Analyser

The lexical analyser is comprised of two different functions, lexeme_returner and token_returner.
The input is an equation string, which returns both the lexeme list and the token list, which can then be further interpretated by the Syntax analyser and then be converted to a tree to be calculated.

### Lexeme Returner

This takes in a string and returns a list of strings.

#### Current Valid Lexemes

- Any Integer Value
- Basic Operators: +, -, /, \*
- Left and Right Brackets

### Token Returner

This takes in a list of strings from the Lexeme Returner and returns a list of Tokens.
