class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"The {self.name} says:")

class Dog(Animal):
    def bark(self):
        print("Woof")

class Cat(Animal):
    def meow(self):
        print("Meow")

dog = Dog("Chop")

dog.speak()

dog.bark()

cat = Cat("Garfield")

cat.speak()

cat.meow()