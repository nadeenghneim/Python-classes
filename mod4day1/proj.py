def square():
    start=int(input("enter a starting range: "))
    end=int(input("enter an ending range: "))
    sqr_list=[]
    even=[]
    odd=[]

    for i in range(start,end):
        sqr_list.append(i**2)
        if(i**2)%2==0:
            even.append(i**2)
        else:
            odd.append(i**2)
    print("the square list of your range:",sqr_list)
    print("the even numbers in your range are:",even)
    print("the odd numbers in your range are:",odd)

    
square()
