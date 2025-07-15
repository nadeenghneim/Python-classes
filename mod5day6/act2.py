class Flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word +"-"+self.meaning

meanings=[]
while True:
    word=input("enter a word:")
    meaning=input("enter its definition:")
    meanings.append(Flashcard(word,meaning))
    continuation=input("do you want to add a word?(yes/no):")
    if continuation!='yes':
        break

for i in meanings:
    print(i)

