x=9
y=24
z=71
if x>z and y>z:
    print("variable z has the smallest number.")
elif y>x or y>z:
    print("variable y could be the largest number")
elif z>x and z>y:
    print("variable z has the largest number.")
else:
    print("unclear which is greater.")