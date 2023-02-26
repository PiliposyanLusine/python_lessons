ls1=input("Enter word1: ")
ls2=input("Enter word2: ")
ls3=""
if ls1 == ls2:
    print("0")
if len(ls1) != len(ls2):
    print("-1")
if len(ls1) == len(ls2):
    for char in ls1:
        if char not in ls2:
            ls3=ls3+char
print(ls3)
