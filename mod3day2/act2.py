def cube(x):
    return x**3
def cube2(x):
    cube1=cube(x)
    cubef=cube(cube1)
    return cubef
x=int(input("enter the number:"))
result=cube2(x)
print("the result is", result)