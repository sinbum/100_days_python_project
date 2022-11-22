# TODO 1. '*args' 를 사용해 여러 인자값을 받을 수 있도록 설정하기.
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# TODO 2. '**kwargs' 를 사용해 딕셔너리 형태로 데이터를 받아오기. ## **kwargs: Many Keyworded Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)
