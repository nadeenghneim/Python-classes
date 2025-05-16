def calc(age):
    try:
        age=int(age)
        if age<0:
            raise ValueError ("your age cannot be negative")
        if age%2==0:
            print("your age is an even number")
        else:
            print("your age is an odd number")
    except ValueError:
        print("exception:age is not valid")
    except NameError:
        print("exception: age must be an integer")
userage=input("enter your age")
calc(userage)
    