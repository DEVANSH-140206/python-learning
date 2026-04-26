# write a program to find weather a username comntains lesss than 10 characters or not

username= input("enter your username :")
if username == "":
    print("invalid")
elif (len(username)<10):
    print("the username contains less than 10 characters")
elif (len(username)>10):
    print("the username contains more than 10 characters")
else:
    print("the username contains exactly 10 characters")
