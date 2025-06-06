#add a value, remove a value, same and different datatypes, duplications
myset={2,4,5,6,6,7,8,}
print(myset)
myset.add(10)
print(myset)
myset.pop()
print(myset)

set2={1,'a',2,'b',3,'c',1}
print(set2)
set2.remove('c') #use remove with mixed datatype sets cause their order isnt fixed
print(set2)
set2.discard(1)
print(set2)
