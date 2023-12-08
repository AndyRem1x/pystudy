class Animal:
    def talk(self):
        return "Hello, I'm animal!"


class Dog(Animal):
    greeting = "Woof woof"

    def __init__(self, name):
        self.name = name

    def talk(self):
        return Dog.greeting


class Cat(Animal):
    greeting = "Meow"

    def __init__(self, name):
        self.name = name

    def talk(self):
        return Cat.greeting


def print_greeting(animal):
    print(animal.talk())


dog1 = Dog("George")
cat1 = Cat("Komaru")

print_greeting(dog1)
print_greeting(cat1)
