# write a program to greet all the person name in the list whoes name starts with s 
names = ["harry", "Sohan", "Sachin", "Rahul"]

for name in names:
    if name.startswith("S"):
        print(f"Hello, {name}!")