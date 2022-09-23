
import math

class VariableSingleInput():

    all_variables = []

    @classmethod
    def empty_list(cls):
        cls.all_variables.clear()


    def __init__(self, inputs = [], evaluate=None, grad=None):

        VariableSingleInput.all_variables.append(self)

        if grad == None:
            self.grad = lambda value: 1
        else:
            self.grad = grad

        if evaluate == None:
            self.evaluate = lambda value: value
        else:
            self.evaluate = evaluate

    def __call__(self, value):
        return self.evaluate(value)
    
    def gradient(self, value):
        return self.grad(value)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return VariableSingleInput(inputs = [self],
                                evaluate = lambda value: other + self.evaluate(value), 
                                grad = lambda value: self.grad(value)
                            )
        elif isinstance(other, VariableSingleInput):
            return VariableSingleInput(inputs = [self, other],
                                evaluate = lambda value: self.evaluate(value) + other.evaluate(value),
                                grad = lambda value: self.grad(value) + other.grad(value)
                           )
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return VariableSingleInput(inputs = [self],
                                evaluate = lambda value: other + self.evaluate(value), 
                                grad = lambda value: self.grad(value)
                            )
        elif isinstance(other, VariableSingleInput):
            return VariableSingleInput(inputs = [self, other],
                                evaluate = lambda value: self.evaluate(value) + other.evaluate(value),
                                grad = lambda value: self.grad(value) + other.grad(value)
                           )
        else:
            return NotImplemented


    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return VariableSingleInput(inputs = [self],
                                evaluate = lambda value: other * self.evaluate(value), 
                                grad = lambda value: other * self.grad(value)
                            )
        elif isinstance(other, VariableSingleInput):
            return VariableSingleInput(inputs = [self, other],
                                evaluate = lambda value: self.evaluate(value) * other.evaluate(value),
                                grad = lambda value: self.evaluate(value) * other.grad(value) + self.grad(value) * other.evaluate(value)
                           )
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return VariableSingleInput(inputs = [self],
                                evaluate = lambda value: other * self.evaluate(value), 
                                grad = lambda value: other * self.grad(value)
                            )
        elif isinstance(other, VariableSingleInput):
            return VariableSingleInput(inputs = [self, other],
                                evaluate = lambda value: self.evaluate(value) * other.evaluate(value),
                                grad = lambda value: self.evaluate(value) * other.grad(value) + self.grad(value) * other.evaluate(value)
                           )
        else:
            return NotImplemented

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return VariableSingleInput(inputs = [self],
                                evaluate = lambda value: self.evaluate(value) ** other, 
                                grad = lambda value: other * self.evaluate(value) ** (other-1) * self.grad(value)
                            )
        else:
            return NotImplemented
    
    def epow(self):
        return VariableSingleInput(inputs = [self],
                                evaluate = lambda value: math.e ** self.evaluate(value), 
                                grad = lambda value: math.e ** self.evaluate(value) * self.grad(value)
                            )

    def ln(self):
        return VariableSingleInput(inputs = [self],
                                evaluate = lambda value: math.log(self.evaluate(value)), 
                                grad = lambda value: 1/self.evaluate(value) * self.grad(value)
                            )

    def __sub__(self, other):
        return self.__add__(other.__mul__(-1))


    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__mul__(other.__pow__(-1))
        else:
            return NotImplemented


        


 


x = VariableSingleInput()
y = 2-x
print(y.evaluate(1))
print(y.grad(1))
