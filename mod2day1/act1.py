medcondition= input("do you have a medical condition?(enter yes or no): ")
attendance= int(input("enter the amount of times you have been absent: "))
totalschldays= 200

if attendance/totalschldays*100<75:
    if medcondition=="yes":
        print("you are excused")
    else:
        print("you are not excused!")
else:
    print("you have exceeded the required attendance!")