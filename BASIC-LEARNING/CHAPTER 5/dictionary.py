# dictionaries are used to store data in key value pairs
# dictionaries are mutable
# dictionaries are defined by using curly braces {}
# dictionary can have items of different data types
# dictionary can have duplicate values but not duplicate keys
marks = { "devansh": 90, "shadow": 95, "ayush": 85 }
print(marks["devansh"]) # to access the value of key "devansh"

print(marks.items()) # to get all the key value pairs in the dictionary in form of a tuple
# print(marks.keys()) # to get all the keys in the dictionary in form of a list
# print(marks.values()) # to get all the values in the dictionary in form of a list 
print(marks.update({"devansh": 100})) # to update the value of key "devansh" to 100
print(marks)