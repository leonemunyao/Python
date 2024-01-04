# Class and Object Variables

"""The data part(i.e fields) are ordinary vaiables that are bound to the namespaces of the classes and objects. This means these names
are valid within the context of these classes and objects only. Thats why they are called name spaces. There are two types of fields: 
class variables and object variables which are classified depending on whether the class or objects owns the variables respectively.
Class variables are shared, they can be accessed by all instances of that class. Object variables are owned by each individual object/
instance of the class. Each object has its own copy of the field."""

#!/usr/bin/python3
class My_code:
    intensity = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))

        My_code.intensity += 1

    def code(self):
        print("{} is being programmed".format(self.name))

        My_code.intensity -= 1

        if My_code.intensity == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There is still {:d} something to be programmed".format(My_code.intensity))

    def say_hello(self):
        print("Greeting, my masters call me {}.".format(self.name))

    @classmethod
    def number_codes(cls):
        print("We have {:d} programs".format(cls.intensity))


code1 = My_code("C_code")
code1.say_hello()
My_code.number_codes()

code2 = My_code("Python_code")
code2.say_hello()
My_code.number_codes()

print("\nPrograms can do some work here.\n")

print("Programs have finished there work. So lets destroy them.")
code1.code()
code2.code()

My_code.number_codes()