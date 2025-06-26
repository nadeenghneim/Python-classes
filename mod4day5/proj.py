#list comprehension 
my_list=[85,95,99,40,45,51,42,31]
result= [mark for mark in my_list if mark<50]
print(result)
names=["nadeen",'bob','lyn','sara','dan']
checking=[x for x in names if len(x)==3]
print("the names containing only three letters are ",checking)
fruits=["apples",'oranges','mangos','pineapple']
capital=[y.capitalize() for y in fruits if type(y)==str]
print("your list of fruits capitalized:",capital)