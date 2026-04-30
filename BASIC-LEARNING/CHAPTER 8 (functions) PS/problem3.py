# program to convert inch to cms 

def inch_to_cm(inches):
    cm = inches * 2.54
    return cm

# Taking input from the user
inches = float(input("Enter the length in inches: "))
print("The length in centimeters is:", inch_to_cm(inches))
while(inches == ""):
    print("Please enter a valid number.")
    inches = float(input("Enter the length in inches: "))