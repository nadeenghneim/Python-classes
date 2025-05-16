x=False
while not x:
    try:
        num1=int(input("enter any number:"))
        while num1%2==0:
            print("it is divisible by 2...")
            
        x=True
    except ValueError:
        print("invalid input..")
