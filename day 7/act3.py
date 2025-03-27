name= input("enter your name: ")
math= int(input("enter your math grade: "))
chem= int(input("enter your chem grade: "))
bio= int(input("enter your bio grade: "))
eng= int(input("enter your eng grade: "))
physics= int(input("enter your physics grade: "))

total= math+chem+bio+eng+physics
average= total/5
print(" total :", total)
print("average:", average)
if average >=91 and average <=100:
    print("your grade is an A")
elif average >=81 and average <=89:
    print("your grade is a B")
elif average >=71 and average <=79:
    print("your grade is a C")
else:
    print("you are failing!")