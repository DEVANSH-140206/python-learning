# make a spam detectror 

a = "make a lot of money"
b = "buy now"
c = "subscribe"
d= "click"

comment = input("enter your comment : ")
if((a in comment) or ( b in comment) or (c in  comment) or (d in comment)):
    print("your comment is a spam")
    print("COMMENT NOT POSTED")
else:
    print("thanks for commenting")

print("\nCLICK PLAY TO COMMENT AGAIN")