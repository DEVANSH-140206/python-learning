# lists are set of items in a particular order
# lists are mutable
# lists are defined by using square brackets []
# list can have items of different data types
# list can have duplicate items 

lst1 = [1, "hello", 3.14, True, None]
print(lst1[1]) # to access the item at index 1
lst1[0] = 10 # to change the item at index 0
print(lst1) 
print(lst1[0:3]) # to access the items from index 0 to 2
print(lst1[-1]) # to access the last item of the list
print(lst1[-3:]) # to access the last 3 items of the list

lst1.append("SHADOW") # to add an item at the end of the list
print(lst1)

# lst1.sort() # Error: cannot sort mixed data types (int, str, float, bool, None)
# To sort, use a list with homogeneous types:
lst2 = [3, 1, 4, 1, 5, 9, 2, 6]
lst2.sort()
print(lst2) 