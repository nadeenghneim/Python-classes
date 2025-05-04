num_donuts=int(input("enter the amount of donuts here:"))
if num_donuts>0:
    print("get back on your diet!")
else:
    print("good job!")

max_donut_intake=int(input("enter the max number of donuts:"))
if max_donut_intake<3:
    print("good job")
elif max_donut_intake==3:
    print("slow down")
elif max_donut_intake>3:
    print("get back on your diet")
else:
    print("ok cool")

name=str(input("enter your name:"))

favfood=str(input("enter your favorite food:"))
if name.lower()=="homer" and favfood=="donuts":
    print("welcome home!")
else:
    print(name,",go home!")