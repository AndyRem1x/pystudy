class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        print(f"{self.age} dog's years is {self.age * self.age_factor} years in human equivalent")


first_dog = Dog(7)
first_dog.human_age()
second_dog = Dog(5)
second_dog.human_age()
