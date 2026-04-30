# write a python program using functions to covert temperature from fahrenheit to celsius and celsius to fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9.0/5.0) + 32
    return fahrenheit

# Taking input from the user
temp = float(input("Enter the temperature: "))
scale = input("Enter the scale (F for Fahrenheit, C for Celsius): ")

if scale == "F":
    print("The temperature in Celsius is:", fahrenheit_to_celsius(temp))
elif scale == "C":
    print("The temperature in Fahrenheit is:", celsius_to_fahrenheit(temp))
else:
    print("Invalid scale. Please enter F or C.")