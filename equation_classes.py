class Number:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return (str(self.value))
    
    def get_value(self):
        return (self.value)

class Integer(Number):
    def __init__(self, value: int):
        if int(value) == value:
            super().__init__(value)

class Operator:
    def __init__(self, left, right, operator: str):
        self.left = left
        self.right = right
        self.operator = operator
    
    def __str__(self):
        return (str(self.left) + str(self.operator) + str(self.right))
    
class Addition(Operator):
    def __init__(self, left, right):
        operator = "+"
        super().__init__(left, right, operator)
    
    def get_value(self):
        return (self.left.get_value() + self.right.get_value())
    
class Subtraction(Operator):
    def __init__(self, left, right):
        operator = "-"
        super().__init__(left, right, operator)
        
    def get_value(self):
        return (self.left.get_value() - self.right.get_value())

class Multiply(Operator):
    def __init__(self, left, right):
        operator = "*"
        super().__init__(left, right, operator)
    
    def get_value(self):
        return (self.left.get_value() * self.right.get_value())
        
class Division(Operator):
    def __init__(self, left, right):
        operator = "/"
        super().__init__(left, right, operator)
    
    def get_value(self):
        return (self.left.get_value() / self.right.get_value())
        
# a = Multiply(Addition(Integer(23), Integer(34)), Integer(27))

# print(a.get_value())