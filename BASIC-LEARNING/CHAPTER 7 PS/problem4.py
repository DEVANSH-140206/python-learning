# program to find sum of first n natural number using while loop

num=int(input("enter the number : "))

i=1
Sum=0

while(i<=num):
    Sum+=i
    i+=1
print(Sum)


# doing this with for loop
num=int(input("enter the number : "))   
Sum=0
for i in range (1,num+1):
    Sum+=i
print(Sum)
