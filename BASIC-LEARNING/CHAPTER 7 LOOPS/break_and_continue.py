# break means sab bhula kr loop exit krjao
# continue means uss iteration ko skip krdo aur next iteration pe jao
# pass means kuch nai krna hai bas loop ko chalate rehna hai

for i in range (10):
    if i==5:
        break
    print(i)


for i in range (10):
    if i==5:
        continue
    print(i)


for i in range (10):
    if i==5:
        pass
    print(i)

    