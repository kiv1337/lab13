import random

class S(type):
    def __new__(cls, name, bases, dct):
        dct['a'] = random.randint(10, 50)
        dct['b'] = random.randint(50, 100)

        return super().__new__(cls, name, bases, dct)


class_list = [S(f"Класс {i}", (), {}) for i in range(10, 101)]

for item in class_list:
    print(f"{item.__name__}: Площадь прямоугольника со сторонами: a = {item.a}; b = {item.b} равна {item.a * item.b}")
    
    
print(type(S))