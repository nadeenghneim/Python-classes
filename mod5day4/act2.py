class computer():
    def __init__(self):
        self.__maxprice=2000
    def selling(self):
        print("selling price is ",self.__maxprice)
    def newprice(self,price):
        self.__maxprice=price
comp=computer()
comp.selling()
comp.newprice(5000)
comp.selling()