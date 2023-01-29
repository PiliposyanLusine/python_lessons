z=0
y=0
x=input()
k=int(x)
while k>0:
    z=k%10
    y=z+y
    k/=10
print (y)
