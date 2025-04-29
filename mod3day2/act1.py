
def calc(amnt,perc):
    tip=amnt*perc/100
    total=amnt+tip
    return tip, total
amnt=float(input("enter the bill amount:"))
perc=float(input("enter the percentage amount you tipped with:"))
tip,total =calc(amnt,perc)
print(f"the tip is {tip:.2f}")
print(f"the total is {total:.2f}")
