amount=int(input('enter the amount you wish to withdraw: '))
hundreds= amount//100
fifties= (amount%100)//50
tens=((amount%100)%50)//10

print("the amount of hundreds are:",hundreds)
print("the amount of fifties are:",fifties)
print("the amount of tens are:",tens)