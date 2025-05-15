#hey, i was only able to figure out the code for converting integers into binary
#the decimal part didnt work
num=float(input("enter any decimal number:"))
def conv(num):
    if num==0:
        return
    elif num%2==0:
        print(0)
        num=(num//2)
        conv(num)
    else:
        print(1)
        num=(num//2)
        conv(num)

#print(".")
#def dec(num - int(num)):
    #while num.isinteger()==False:
        #if num.is_integer():
            #print(0)
        #elif type(num) == float:
            #num=num-(int(num))
            #if (num*2).is_integer():
                #print(int(num*2))
            #else:
                #num=(num*2)%2
                
        #else:
            #print("")
conv(num)
#dec(num - int(num))
