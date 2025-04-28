#calculator

def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
print("please select any operation:")
print("1.addition, \n 2.subtraction,\n 3.multiplication, \n 4.division")
choice=input("enter your chosen number: ")
num1=float(input("enter the first number you want to calculate:"))
num2=float(input("enter the second number you want to calculate:"))
if choice=="1":
    print("the addition of the numbers is:",addition(num1,num2))
elif choice=="2":
    print("the difference of the numbers is:",subtraction(num1,num2))
elif choice=="3":
    print("the product of the numbers is:",multiplication(num1,num2))
elif choice=="4":
    print("the quotient of the numbers is:",division(num1,num2))
else:
    print("invalid input, choose one of the four options!")
    