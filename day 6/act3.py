weight=float(input("enter your weight in kilograms: "))
height= float(input("enter your height in meters: "))

bmi= weight/(height)**2
print("your bmi is ", bmi)

if bmi<= 18.5:
    print("you are underweight")
elif bmi<=24.9:
    print("your weight is healthy")
elif bmi<= 30:
    print("you are overweight")
elif bmi<= 40:
    print("you are very overweight.")
else:
    print("you should take care of your health better.")
