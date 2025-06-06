dict={"Name":"Nadeen","age":17,"hobby":"Basketball","nationality":"Palestinian","Name":"NadeenGhneim"}
x={}
for i,y in dict.items():
    if y not in x.values():
        x[i]=y
print(x)
