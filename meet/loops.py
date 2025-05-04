text=str(input("enter what you want to say:"))
while text!="BYE":
    if text.isupper():
        print("NO,THINGS WERE BETTER IN OUR DAYS.")
        text=str(input("enter what you want to say:"))
    else:
        print("HUH,SPEAK UP SONNY!")
        text=str(input("enter what you want to say:"))

my_item=str(input("enter the item you are looking for:"))
my_closet = [
 "running shoes",
 "dress shoes",
 "red shirt",
 "blue shirt",
 "brown pants",
 "bagel",
 "book",
]
item_found=False
for item in my_closet:
    if my_item in my_closet:
        print("I found my",my_item)
        item_found=True
        break
else:
    print("I cant find",my_item)

for num in range(1,101):
    if num%3==0 and num%5==0:
        print("fizzbuzz")
    elif num%5==0:
        print("buzz")
    elif num%3==0:
        print("fizz")
    else:
        print(num)