# write a program to create a tuple with only one element
a= (1,)
print(type(a))

#write a tuple
b = (1, 2, 3, 4, 5)
print(b)    

count = a.count(1)
print(count)

count2 = b.count(4)
print(count2)   
# count tells kitne baar aaya hai element tuple me

i= b.index(4)
print(i)
# index btata hai ki tuple ya list ya string me element kaha par hai, agar element nahi hai to error aayega
