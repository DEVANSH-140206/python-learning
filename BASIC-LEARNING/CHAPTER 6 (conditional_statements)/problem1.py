# a program to see if the age is enterred is above 18 or not

age= int(input("please, enter your age: "))

if(age>=18):
    print("you are above the age of consent")
    print("permission granted , welcome sir")
elif(age==0):
    print("you are not born yet")
    print("permission denied , get out ngga ")
elif(age<0):
    print("bkchdoi mt kr lawde")
    print("permission denied")
elif(age < 18):
    print("you are below the age of consent")
    print("permission denied")
else:
    print("invalid")


    