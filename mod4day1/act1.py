#lists
groceries=["milk","eggs","cereal"]
groceries.append("chocolate")
print(groceries)
groceries.insert(0,"cheese")
print(groceries)
print(groceries.count("milk"))
groceries.remove("eggs")
print(groceries)
groceries.reverse()
print(groceries)

numbers=[[1,3,5,7,9],[2,4,6,8,10]]#nested loop
print(numbers[0][4])#0 accesses first list and 4 is 4 within the fdirst list