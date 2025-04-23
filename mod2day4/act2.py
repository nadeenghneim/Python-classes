low=int(input("enter your lower limit:"))
up=int(input('enter your upper limit:'))

for num in range(low,up+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
