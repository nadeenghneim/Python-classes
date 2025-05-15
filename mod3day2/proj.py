cond1= input("do you want to shut down the system?:")
cond2=input("do you have admin approval?:")
def shut(cond1,cond2):
    if cond1=="yes" and cond2=="yes":
        return "shutting down"
    elif cond1=="no" or cond2=="no":
        return "you cannot shut down at the moment"
    else:
        return "sorry, incorrect input."
print(shut(cond1,cond2))