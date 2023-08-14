
def add(*args):
    result = 0
    for n in args:
        result += n

    return result


final = add(98, 2, 5, -10, 15)
print(final)

print(add(3, 5, 4))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # Using .get() allows the argument to be optional
        self.model = kw.get("model")

my_car = Car(make="nissan", model="GT-R")
print(my_car.make)


tuply = (1, 3, 5)
print(tuply)
