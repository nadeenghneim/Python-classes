try:
    num=int(input("enter a nondecimal number:"))
    print("the number is", num)
except ValueError as ex:
    print("Exception:",ex)