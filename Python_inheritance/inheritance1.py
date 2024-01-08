#!/usr/bin/python3
"""A python program that demostrates inheritance"""

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
