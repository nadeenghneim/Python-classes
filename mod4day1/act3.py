my_list=[1,3,7,10,6.8,5.5]
print("the length of my list is",len(my_list))
x=0
for item in my_list:
    x+=item
print("the sum is ",x)
average= x/(len(my_list))
print("the average is", average)

my_list.sort()
print("smallest value:",my_list[0])
print("largest value:",my_list[-1])
my_list.reverse()
print("smallest value:",my_list[-1])
print("largest value:",my_list[0])