# write a program to find the greatest of tw5 numbers entered by the user 

num1 = int(input("enter the 1st number : "))
num2 = int(input("enter the 2nd number : "))
num3 = int(input("enter the 3rd number : "))
num4 = int(input("enter the 4th number : "))

if ((num1>num2) and (num1>num3) and (num1>num4)):
    print("the greatest of 4 number is: ",num1)
elif((num2>num1) and (num2>num3) and ( num2>num4)):
    print("the greatest of 4 number is: ",num2)
elif((num3>num1) and (num3>num2) and (num3>num4)):
    print("the greatest of 4 number is: ",num3)
else:
    print("the greatest of 4 number is: ",num4)
    
    
print("PLAY AGAIN TO RESTART")