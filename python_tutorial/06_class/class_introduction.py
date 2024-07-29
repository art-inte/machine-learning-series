class MyClass:
    x = 5

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'

    def say_hello(self):
        print('Hello my name is', self.name)

if __name__ == '__main__':
    a = MyClass()
    print('The property of MyClass is', a.x)

    b = Person('John', 36)
    print('Name', b.name)
    print('Age', b.age)
    print('Person', b)
    print(b.say_hello())
    b.age = 40
    print('Modify age', b.age)
    del b
