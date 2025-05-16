try:
    num1,num2=eval(input("enter two numbers seperated by a comma:"))
    div=num1/num2
    print(div)
except ZeroDivisionError:
    print("exception,cannot divide by zero")
except SyntaxError:
    print("make sure to seperate your numbers with a comma.")
except NameError:
    print("make sure you enter two integers.")
else:
    print("no exceptions detected..")
finally:
    print("this will print at the end...")
