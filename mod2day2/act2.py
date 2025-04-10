sentence= str(input("please enter any word or sentence: "))

revsentence=""
for i in sentence:
    revsentence=i+revsentence
print("your original sentence is:",sentence)
print("your reversed sentence is:",revsentence)