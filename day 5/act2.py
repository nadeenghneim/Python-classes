cost=float(input('Enter your exact cost:'))
sold= float(input('Enter the amount you sold: '))
if (sold > cost):
    profit= sold - cost
    print(f"the profit is {profit}")
else:
    print("There is no profit.")