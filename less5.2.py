x=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]
x1=[]
for i in range(len(x)):
    x1.append(x[i][::-1])
x1.reverse()
print("Original list:",*x, sep="\n")
print("")
print("Revesed list: ",*x1, sep="\n")
