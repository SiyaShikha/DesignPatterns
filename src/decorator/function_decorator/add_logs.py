from functools import wraps

def uppercase_decorator(function):
    @wraps(function)
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


def split_string(function):
    @wraps(function)
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper 

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())
print(say_hi.__name__)