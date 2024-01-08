#!/usr/bin/python3

"""In this example the child class is inheriting the properties of its parent class. In this case Person is the parent class and Employee
is its child class"""

# Base or Super class. Note object in brackets. Generally object is made ancetor of its parent classes

class Person(object):

    """Constructor"""
    def __init__(self, name, id):
        self.name = name
        self.id = id

    """To get name"""
    def get_name(self):
        return self.name
    
    """To get id"""
    def get_id(self):
        return self.id
    
    """To know if this person is an employee"""
    def isEmployee(self):
        return False
    

# Lets know write the subclass

class Employee(Person):  # Employee inherits from Person
    def isEmployee(self):
        return True
    
# Driver code
emp = Person("John Doe", 123)
print(emp.get_name(), emp.get_id(), emp.isEmployee()) # Output: John Doe

emp = Employee("Software Engineer Leone", 124)
print(emp.get_name(), emp.get_id(), emp.isEmployee())
# Output: Software Engineer Leone 124 True