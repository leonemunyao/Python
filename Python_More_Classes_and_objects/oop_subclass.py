"""Inheritance. One of the major benefits of object oriented programming is reuse of code and one of the ways this is achieved is through
inheritance """

#!/usr/bin/python3

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print("(Initialized SchoolMember: {})".format(self.name))

    def details(self):
        print("Name: {} Age: {}".format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

        print("(Initialized Teacher: {})".format(self.name))

    def details(self):
        SchoolMember.details(self)

        print("Salary: {:d}".format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

        print("(Initialized Student: {})".format(self.marks))

    def details(self):
        SchoolMember.details(self)

        print("Marks: {:d}".format(self.marks))


t = Teacher("Mrs Mutuku", 56, 33000)
s = Student("James", 22, 140)

# Prints a blank line
print()

members = [t, s]
for member in members:
    member.details()