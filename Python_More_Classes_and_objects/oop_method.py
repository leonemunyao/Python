#!/usr/bin/python3
class Person:
    def say_hi(self):
        print("Hello Leone, You must be a Software Engineer")


p = Person()
p.say_hi()

"""How it works. Here we see self in action. Note that the say.hi method takes no parameters but still has the self in the function definition
"""

class My_name:
    def say_hello(self):
        print("Leone Munyao")


i = My_name()
i.say_hello()