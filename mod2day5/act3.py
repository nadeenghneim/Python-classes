rows=int(input("enter the amount of rows"))
half=rows//2+(rows%2)
for i in range(1,half+1):
    print(" ",half-1, end="")
    num=1
    for j in range(2*i-1):
        print(num,end="")
        num=num+1
    print()

for i in range(half-1,0,-1):
    print(" ",half-1, end="")
    num=1
    for j in range(2*i-1):
        print(num,end="")
        num=num+1
    print()