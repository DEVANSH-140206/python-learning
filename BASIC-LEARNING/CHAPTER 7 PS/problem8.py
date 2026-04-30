# make a star pattern like this 
# ***
# * *
# ***

rows= int(input("enter the number of rows :"))
for i in range (1,rows+1):
    if i==1 or i==rows:
        print("*"*rows)
    else:
        print("*"+" "*(rows-2)+"*")