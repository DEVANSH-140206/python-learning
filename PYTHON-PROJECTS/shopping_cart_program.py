# shopping cart program

items= []
price=[]
total=0

while True:
    food = input("Enter the name of the food item (or 'q' to quit): ")
    if food.lower() == "q":
        break
    else:
        items.append(food)
        p = float(input(f"Enter the price of {food}: "))
        price.append(p)

print("\n----- YOUR CART -----")
for food in items:
    print(food)