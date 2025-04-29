def fact(x):
    '''i am learning about factorials and docstrings. 
    this is why i am using three single quotations.'''
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
print(fact.__doc__)
print("the factorial of 0: ",fact(0))
print("the factorial of 2: ",fact(2))
print("the factorial of 6: ",fact(6))
