import numpy as np
x=np.array([[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]])
x1=[]
x1=x.transpose()
print("Original list:",*x, sep="\n")
print("")
print("Revesed list: ",*x1, sep="\n")
