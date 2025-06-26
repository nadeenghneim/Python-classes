#frozen set:immutable set
x=frozenset([1,2,4,6,8,10])
y=frozenset([1,3,6,10,12])

if x.isdisjoint(y)== True:
    print("set x has no common values with any other set.")
else:
    print("set x has common values with other sets")
    print("the unique values in the set are",x.difference(y))

user_input= input("do you want to see a set of all the values in both set?(type yes or no)")
if user_input=="yes":
    print("the combined set is",x|y)
else:
    print("ok no problem.")