import random 

print("HI, we will be generating a random password for you!!")

def password():
    for i in range(1,5):
        print(random.choice('abcdefghijklmnopqrstuvwxyz'),end='')
        print(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),end='')
        print(random.randint(0,9),end='')
password()
