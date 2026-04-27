
# write a program to calculate the factoruial of a given number using for loop and while loop

n= int(input("enter the number : "))
factorial=1

for i in range (1,n+1):
    factorial= factorial*i
print(factorial)

# doing this with while loop
n= int(input("enter the number : "))
factorial=1 
i=1
while i<=n:
    factorial= factorial*i
    i+=1
print(factorial)    