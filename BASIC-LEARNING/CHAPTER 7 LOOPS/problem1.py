# Write a program to print the content of the list using while loops
list= [1,"shadoew",3.14,True]
i=0
while(i< len(list)):
    print(list[i])
    i+=1


    # same thing with for loop 
    # anything can be done by both loops but for loop is more efficient and easier to read and write
    # while is generall used for infinite repetition and for is used for finite repetition
for c in range (0,len(list)):
    print(list[c])
