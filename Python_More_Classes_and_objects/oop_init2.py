#!/usr/bin/python3

class My_Code:
    def __init__(self, name=None):
        self.name = name
    def hello_devs(self):
        if self.name:
            print("Consistency is the key to programming and " + self.name)
        else:
            print("Without discipline you can't become a successful Software Developer")
    
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    
i = My_Code()
i.set_name("Discipline")
i.hello_devs()
j = My_Code()
j.set_name(i.get_name())
print(j.get_name())
