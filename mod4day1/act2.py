#checking if the first and last letterof a word are the same 
def word(words):
    chr=0
    word_list=[]
    for item in words:
        if len(item)>1 and item[0]==item[-1]:
            chr+=1
            word_list.append(item)
    print(word_list)
    return chr
result=word(["aaa","b","alpa","aaa"])
print(result)
