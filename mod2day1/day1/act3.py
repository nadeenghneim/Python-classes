print("choose what you want to ride:")
print("1.car \n 2.bike")
ridechoice=int(input("enter your choice: "))
if ridechoice==1:
    print("what type of car do you prefer?")
    print("1.lambo \n 2. ferrari")
    carchoice=int(input("enter your car choice"))
    if carchoice==1:
        print("you have selected the lambo.")
    else:
        print("you have selected the ferrari.")
elif ridechoice==2:
    print("what type of bike do you prefer?")
    print("1.bmx \n 2. scooter")
    bikechoice=int(input("enter your car choice"))
    if carchoice==1:
        print("you have selected the bmx.")
    else:
        print("you have selected the scooter.")