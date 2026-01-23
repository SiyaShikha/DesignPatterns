class UppercaseDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        return result.upper()

@UppercaseDecorator
def greet(name):
    return f"hello {name}"

print(greet("Shikha"))