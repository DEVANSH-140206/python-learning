# write a program to print multiplication table of a given number usiing functions

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}") 

# Taking input from the user
number = int(input("Enter the number for which you want the multiplication table: "))
multiplication_table(number)