# dictionary and sets both uses curly brackets {}
# sets are used to store unique items in an unordered way
# sets are mutable  
# sets are defined by using curly braces {}
# to create an empty set we have to use set() function because {} creates an empty dictionary
s = {1, 2, 3, 4, 5}
print(type(s))

e = set() # to create an empty set
print(type(e))

# elemnts in a set dont repeat 
# yes set can have diffrent data types
s= {1, 2, 3, 4, 5, 1, 2, "hello", 3.14, True}
print(s) # to print the set, the order of the items may change and duplicate items will be removed

s.add(6)
print(s) # to add an item to the set

a= {1, 2, 3}
b= {3, 4, 5}    
print(a.union(b)) # to get the union of two sets
print(a.intersection(b)) # to get the intersection of two sets      
