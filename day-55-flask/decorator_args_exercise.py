# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        result = function(*args)
        print(f"It returned: {result}")
    return wrapper

# Use the decorator 👇

@logging_decorator
def multiply_function(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

multiply_function(1, 2, 3)