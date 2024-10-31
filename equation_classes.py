class Operator:
    def __init__(self, left, right, operator_token: str):
        self.left = left
        self.right = right
        if operator_token == "ADDITION":
            self.operator = "+"
        elif operator_token == "SUBSTRACT":
            self.operator = "-"
        elif operator_token == "MULTIPLY":
            self.operator = "*"
        elif operator_token == "DIVISION":
            self.operator = "/"
        else:
            self.operator = "+"
    
    def __str__(self):
        return (str(self.left) + str(self.operator) + str(self.right))
    
    def get_value(self):
        if self.operator == "+":
            return (self.left.get_value() + self.right.get_value())
        elif self.operator == "-":
            return (self.left.get_value() - self.right.get_value())
        elif self.operator == "*":
            return (self.left.get_value() * self.right.get_value())
        elif self.operator == "/":
            return (self.left.get_value() / self.right.get_value())
        else:
            return (self.left.get_value() + self.right.get_value())

class Number:
    def __init__(self, value: str):
        self.value = value
    
    def __str__(self):
        return (str(self.value))
    
    def get_value(self):
        if type(self.value) == int:
            return (self.value)
        else:
            return (self.value.get_value())

class Integer(Number):
    def __init__(self, value):
        super().__init__(int(value))

class Expression:
    def __init__(self, input_class: Operator | Number):
        self.input_class = input_class
    
    def get_value(self):
        return self.input_class.get_value()
