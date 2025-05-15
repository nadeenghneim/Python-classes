given=float(input("enter the amount you gave the shopkeeper:"))
owed=float(input("enter the amount you owe:"))

if (given==owed):
    print("there is no change, go home.")
elif(given-owed>0):
    change=given-owed
    print("your change is", change)
elif(given<owed):
    print("please pay what you owe")
else:
    print("invalid input")


#alternative way:
price=87.5
def change(amountgiven):
    return amountgiven-price
x= change(100)
print(x)