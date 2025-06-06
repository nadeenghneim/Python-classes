#checking the frequency
dict={"Sara":12,"Olivia":15,"Sam":15,"Bob":12,"Gilbert":5}
x=12
result=0
for i in dict:
    if dict[i]==x:
        result+=1
print("the amount of times x is repeated is",result)
y=int(input("enter the number of which you want to check the frequency:"))
result_user=0
for i in dict:
    if dict[i]==y:
        result_user+=1
print("the amount of times your number is repeated is",result_user)
