# CONCESSION STAND PROBLEM

menu= {"samosa": 5,
       "pizza":100,
       "burger": 50,
       "fries": 20,
       "coke": 10,
       "cold coffee": 5000,
       "water": 15,
       "ice cream": 30,}

cart=[]
total=0


print("--------------------- MENU ------------------------")
for key,value in menu.items():
    print(f"{key:10}: ₹{value}", end=" | ")

print("\n--------------------------------------------------")

while True:
    food = input("Enter the name of the food item you want to order (or 'q' to quit): ")
    if food.lower() == "q":
        break   
    elif food.lower() not in menu:
        print("Sorry, we don't have that food on the menu. Please choose from the menu.")
    else:
        cart.append(food)
        total += menu[food.lower()]

print("\n----- YOUR CART -----")
for food in cart:
    print(food)
print(f"Total: ₹{total}")   

print("\nThank you for your order! Please proceed to payment.")