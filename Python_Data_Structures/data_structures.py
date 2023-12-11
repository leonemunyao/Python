#!/usr/bin/python3

# Data Structures
# The list data type has some methods, here are some of the methods used 
list.append() # add an item in the list
list.extend() # Extend the list by appending all the items from the iterable
list.insert() # Insert an item at a given position. 
list.remove() # remove the first item from the list. It raises a ValueError if there is no such value in the list
list.pop([]) # Removes an item at the given position in the list and return it. 
list.clear() # Removes all the items from the list 


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'pineapple']
fruits.count('apple') # returns the number of times apple appears in the list

fruits.index('banana') # Returns the index of the first banana