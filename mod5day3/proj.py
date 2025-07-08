
class vehicles():
    def __init__(self):
        pass
class bus(vehicles):
    def __init__(self):
        pass
    def pricing(self):
        max_cap= int(input("enter the maximum capacity of the bus you wish to take:"))
        base_price=max_cap*100
        maintenance_price=(max_cap*100)*0.1
        total_price=base_price+maintenance_price
        print("the price for riding a bus with this capacity is",total_price)
        print("this is including a maintenance charge of 10% the original fee which is:",maintenance_price)
bus1=bus()
bus1.pricing()
