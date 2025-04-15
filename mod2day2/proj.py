base=int(input("enter your base number: "))
power=int(input("enter the power you want to raise it to: "))
result=1

for i in range(power):
    result*=base
print("the result of", base,"raised to the power of",power,"is",result )