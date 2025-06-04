def checking(nums):
    e=len(nums) -1
    s=0
    while(s<e):
        if (nums[s]==nums[e]):
            e-=1
            s+=1
            return True 
        else:
            return False
nums=(1,2,3,3,2,1)
if checking(nums):
    print("flip flop tuple")
else:
    print("not a flip flop tuple")
