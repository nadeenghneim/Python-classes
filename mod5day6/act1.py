class X:
    def __init__(self,a):
        self.a=a
    def __gt__(self,b):
        if self.a>b.a:
            print("object 1 is greater than 2")
        else:
            print("object 2 is greater than object 1 ")
    def __lt__(self,b):
        if self.a<b.a:
            print("object 1 is lesser than object 2")
        else:
            print("object 2 is lesser than object 1")
obj1=X(3)
obj2=X(13)

obj1>obj2
obj1<obj2