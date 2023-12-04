#!/usr/bin/python3

# Lists might contain items of different types but usually all the items usually have the same type.

squares = [16, 25, 36, 49, 64, 81]
squares
# Like strings, lists can be indexed and sliced
squares[0] # prints 16
squares[-1] # prints 81
squares[-3] # prints 49, 64, 81

# Lists also support operations like concatenation 
squares + [100, 121, 144, 169, 196, 225]

# Unlike strings which are immutable, lists are a mutable type i.e its possible to change their content
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64 # changes 65 to 64
cubes
['']

# You can also add new items at the end of the list using the list.append() method
cubes.append(216)
cubes

# Assignment to slices is also possible and can even change the size of the list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters

# Replace some values
letters[2:5] = ['C', 'D', 'E']

