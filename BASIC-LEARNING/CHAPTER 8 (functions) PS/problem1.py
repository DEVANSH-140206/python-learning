# write a program to find the greatest of three numbers using function

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

# Example usage
    # print(greatest(10, 20, 30))  # Output: 30
    # print(greatest(30, 20, 10))  # Output: 30
    # print(greatest(10, 30, 20))  # Output: 30

# Taking input from the user

num1 =(input("Enter the first number: "))
num2 =(input("Enter the second number: "))
num3 =(input("Enter the third number: "))

while(num1 == "" or num2 == "" or num3 == ""):
    print("Please enter all three numbers.")
    num1 =(input("Enter the first number: "))
    num2 =(input("Enter the second number: "))
    num3 =(input("Enter the third number: "))

    num1 = float(num1)
    num2 = float(num2)      
    num3 = float(num3)

# Calling the function and displaying the result
print("The greatest number is:", greatest(num1, num2, num3))
