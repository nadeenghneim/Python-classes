letter= input("enter any letter of the alphabet: ")

if len(letter)==1:
    code=ord(letter)
    print("the asci code for this letter is:", code)
else:
    print("invalid input, enter only one character!")