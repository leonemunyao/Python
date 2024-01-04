"""There are many method names which have special significance in python classes. The __init__ method is run as soon an object of
a class is instantieted(created) The method is useful to do any initialization(passing initial value to your object) you want to do
 with your object. Notice the double underscores both at the beginning and at the end"""

#!/usr/bin/python3
class My_name:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is ", self.name)

i = My_name("Leone Munyao")
i.say_hello()

# The previous two lines can also be written as My_name("Leone Munyao").say_hello()