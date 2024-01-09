Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class. Variables that belong to an object or class are referred to as fields. Objects can also have functionality by using functions that belong to a class. Such functions are called methods of the class. 

The __init__ method

We want to define the attributes of an instance right after its creation. __init__is a method which immediately and automatically called after an instance is created. This name is fixed and it is not possible to choose anther name. __init__ is one of the magic methods. Its used to initialize an instance. It follows right after the class header.

Data Abstraction, Data Encapsulation and InformatiON Hiding

Encapsulation is seen as the building of data. Information hiding is the principle that some internal information or data is hidden. Data Abstraction is both.

Data Abtraction =  Data Encapsulation + Data Hiding

__str__ and __repr__ methods

If you apply str and repr to an object, Python is looking for a corresponding methos __str__ or __repr__ in the class definition of the object. If the methos does not exist, it will be called 