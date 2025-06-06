dict={'codingal':3,'is':2,'best':2,'for':2,'coding':1}
value=int(input("enter the number you want to check the frequency of: "))
frequency=0
for i in dict:
    if dict[i]==value:
        frequency+=1
print("the frequency of your number is:",frequency)