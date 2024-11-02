# Mathematical Equation Calculator

Uses Python 3.12 or later to convert an equation as a string to a value.

## Equation Calculator

### How to Use

```python
import equation_expression_calculator from equation_expression_calculator

print(equation_expression_calculator("INPUT YOUR EQUATION HERE"))
```

This returns the value of the equation you inputed as a number.

### Allowed Operations

| Operation   | Allowed Value | Expected Use |
| ----------- | ------------- | ------------ |
| Multiply    | \*            | a \* b       |
| Addition    | +             | a + b        |
| Subtraction | -             | a - b        |
| Division    | /             | a / b        |
| Powers      | ^             | a ^ b        |

### Example Inputs

```python
print(equation_expression_calculator("(2+3)^(2*3)"))

# Output: 15625

print(equation_expression_calculator("34*23/(2+279)"))

# Output: 2.7829181494661923
```
