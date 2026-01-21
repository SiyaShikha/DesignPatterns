def square_decorator(func):
    def wrapper(self):
        print("the square is ")
        value = func(self)
        return value * value
    return wrapper    
        
class Number:
    def __init__(self, num):
        self.num = num
        
    @square_decorator
    def calculations(self):
        return self.num