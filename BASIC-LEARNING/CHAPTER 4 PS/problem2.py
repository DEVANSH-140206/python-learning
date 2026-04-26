# write a program to accept marks of 6 students and display them in a sorted manner
marks = []
m1 = float(input("enter marks of student 1: "))
marks.append(m1)
m2 = float(input("enter marks of student 2: "))     
marks.append(m2)
m3 = float(input("enter marks of student 3: "))
marks.append(m3)
m4 = float(input("enter marks of student 4: "))
marks.append(m4)
m5 = float(input("enter marks of student 5: "))
marks.append(m5)
m6 = float(input("enter marks of student 6: "))
marks.append(m6)
marks.sort()
print("the marks of students in sorted manner are:", marks)
# we need to convert them to float to sort them correctly otherwise they will be sorted as strings and 10 will come before 2 because 1 comes before 2 in string sorting.
