class Person:
    """A class to represent a person."""

    def __init__(self, name, age):
        """The constructor method."""
        self.name = name
        self.age = age

    def greet(self):
        """Prints a greeting from the person."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object of the Person class
person1 = Person("Ashish", 20)

# Call the greet method on the object
person1.greet()