operator = input("enter an operator (+, -, *, /): ")

while operator == "":
    print("operator cannot be empty")
    operator = input("enter an operator (+, -, *, /): ")

while operator not in ["+", "-", "*", "/"]:
    print("operator cannot be this, enter an operator (+, -, *, /): ")
    operator = input("enter an operator (+, -, *, /): ")

num1= (input("enter the first number: "))
num2= (input("enter the second number: "))
while(num1=="" or num2==""):
    print("numbers cannot be empty")
    num1= (input("enter the first number: "))
    num2= (input("enter the second number: "))

if operator=="+":
    result= float(num1)+float(num2)
elif operator=="-":
    result= float(num1)-float(num2)   
elif operator=="*":
    result= float(num1)*float(num2)
elif operator =="/":
    if num2==0:
        print("division by zero is not allowed")
        result= "undefined"
    else:
        result= float(num1)/float(num2)
print("the result is",result)



