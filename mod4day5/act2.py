#map

def cube(n):
    return n**3

num=[2,4,6,8,10,12]
answer=map(cube,num)#function,iterable thing(the list)
print(list(answer))

#second way:
nums = [2,4,6,8,10,12]

cubes = list(map(lambda x: x**3, nums))#lambda for one line functions

print("Cubes of numbers:", cubes)