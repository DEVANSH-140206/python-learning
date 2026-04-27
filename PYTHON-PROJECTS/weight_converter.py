# PYTHON WEIGHT CONVERTER
weight = (input("enter the weight: "))
while(weight==""):
    print("weight cannot be empty")
    weight = (input("enter the weight: "))

unit = input("is your weight in kg or grams? (k for kg and g for grams): ")
while unit not in ("k", "g"):
    if unit == "l" or unit == "p":
        print("sorry we can only convert between grams and kilograms")
    else:
        print("unit invalid")
    unit = input("enter the correct unit (k for kg and g for grams): ")

if(unit == "k"):
    result = (float(weight)*1000)
    print(f" THE WEIGHT IS {result} GRAMS")
else:
    result = (float(weight)/1000)
    print(f"THE WEIGHT IS {result} KILOGRAMS")

print("THANKS FOR USING")
    