import time
current_time = time.time()

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()


# # Python Decorator Function playground - wraps another function & gives additional functionality 
# import time
# def delay_decorator(function):
#     def wrapper_function():
#         # do something before
#         time.sleep(2)
#         function()
#         # do something after
#     return wrapper_function

# # using the decorator to execute any function with additional functionality 

# @delay_decorator  # same as: decorated function = delay_decorator(say_hello)
# def say_hello():
#     print("Hello")

# @delay_decorator
# def say_bye():
#     print("Bye")

# say_hello()