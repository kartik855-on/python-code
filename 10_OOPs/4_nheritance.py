# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Child class inheriting from Animal
class Dog(Animal):
    
    def speak(self):
        print(f"{self.name} barks")

# Create objects
a = Animal("Animal")
a.speak()

d = Dog("Tommy")
d.speak()



# 2 exampls____________

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# child class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id

    def show_student_info(self):
        self.show_info()  # Call parent method
        print(f"Student ID: {self.student_id}")

# Using the classes
s1 = Student("Kartik", 20, "ST123")
s1.show_student_info()
