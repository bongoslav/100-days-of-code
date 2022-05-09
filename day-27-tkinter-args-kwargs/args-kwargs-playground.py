# *(args) - unlimited positional arguments
def add(*args):
    return sum(args)


print(add(3, 5, 6))


# **(kwargs) - unlimited key-word arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# using kw in a class
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # get() method - if a kw argument hasn't been passed it returns None
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)