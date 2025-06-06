#arrays
import array as arr
x=arr.array('i',[10,20,30,40,40,50,50,50])

print("original array:",x)
print("the number of times 50 is frequent:",x.count(50))
x.reverse()
print("the reversed array:",x)