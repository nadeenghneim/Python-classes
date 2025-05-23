#trip expenses
#hotel,carrental,planaticket,spending
def hotelcost(nights):
    return 200*nights
def planeticket(city):
    if city=="Bethlehem":
        return 500
    elif city=="New York":
        return 1000
    elif city=="Paris":
        return 800
    elif city=="Barcelona":
        return 1500
    else:
        return 0
def carrental(days):
    cost=40*days
    if days>6:
        cost=cost-60
    elif days>10:
        cost=cost-100
    return cost
def total(city,nights,days):
    return hotelcost(nights)+planeticket(city)+carrental(days)
print("we will calculate your trip's costs")
city=input("enter the city you are flying to:")
days=int(input("enter the amount of days you are staying"))
nights=int(input("enter the amount of nights you are staying"))
print("your total expenses are",total(city,nights,days))