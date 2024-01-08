#!/usr/bin/python3

class Person(object):
    
    """The constructor"""
    def __init__(self, name, id):
        self.name = name
        self.id = id

    """To check if he person is an employer"""
    def Display(self):
        print(self.name, self.id)

"""Driver code"""
emp = Person("Software Engineer Leone", 150)
emp.Display()

"""Creating a Child class. This is a class that drives the properties from its parent class. Here Emp is another class that is
going to inherit the properties."""

class Emp(Person):
    def Print(self):
        print("Emp class has been called")

Emp_details = Emp("Software Engineer Leone", 150)

# Calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()