class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        # Print the introduction message
        print(f"Hello! My name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Create an instance of the Person class
person = Person("Alice", 30, "female")

# Call the introduce method
person.introduce()
