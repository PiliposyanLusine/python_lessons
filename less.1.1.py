string=input("Enter word: ")
ls=[]
word=string
for i in range(len(word)):
    if i == 0:
        word= word[i].upper()+word[i+1:]
    elif i == len(word)-1:
        word = word[0:i] + word[i].upper()
    else:
        word=word[0:i]+word[i].upper()+ word[i+1:]
    ls.append(word)
    word=word.lower()
print(ls)
