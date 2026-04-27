# write a program to find if a given number is prime or not

num= int(input("enter a number: "))
while num==0:
    print("number cannot be zero")
    num= int(input("enter a number: ")) 
while  num<0:
    print("number cannot be negative")
    num= int(input("enter a number: "))
if num>1:
    for i in range (2,num):
        if num%i==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")