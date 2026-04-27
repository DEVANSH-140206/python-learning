# write a priogram to write multiplication table of a given number using for loop

num= int(input("enter a number: "))
while num==0:
    print("number cannot be zero")
    num= int(input("enter a number: ")) 

while  num<0:
    print("number cannot be negative")
    num= int(input("enter a number: "))


for i in range (1,11):
    print(num,"x",i,"=",num*i)



# using while loop
num= int(input("enter a number: "))
while num==0:
    print("number cannot be zero")
    num= int(input("enter a number: "))

while  num<0:
    print("number cannot be negative")
    num= int(input("enter a number: "))
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i+=1    
    
