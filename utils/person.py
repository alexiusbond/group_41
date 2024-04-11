class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'{self.__name} is {self.__age} years old.'


# print(__name__)
if __name__ == '__main__':
    p1 = Person('John', 23)
    print(p1)
