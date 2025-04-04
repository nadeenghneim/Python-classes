units=int(input("enter the amount of units you have used:"))
if (units<=50):
    amount = units*2
    sercharge=10
elif (units<=100):
    amount= 100+(units-100)*3
    sercharge=20
elif (units<=150):
    amount= 100+150+(units-150)*5
    sercharge=35
else:
    amount= 100+150+250+(units-150)*10
    sercharge= 50
total=amount+sercharge
print("your electricity bill is: ",total)