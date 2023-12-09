class MyMeta(type):
    def __new__(cls, name, bases, dct):
        new_name = "Meta_" + name
        return super(MyMeta, cls).__new__(cls, new_name, bases, dct)

class HiClass(metaclass=MyMeta):
    def hi(self):
        return f"Hi from {self.__class__.__name__}"

first_class = HiClass()
print(first_class.hi())
