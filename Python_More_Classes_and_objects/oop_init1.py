#!/usr/bin/python3

class A:
    def __init__(self):
        print("__init__ has been executed successfully")
x = A()

class My_Code:
    def __init__(self, name=None):
        self.name = name
    def hello_init(self):
        if self.name:
            print("Hello Developers, I am " + self.name)
        else:
            print("Hello Developers, I am missing out")

i = My_Code()
i.hello_init()
j = My_Code("Leone")
j.hello_init