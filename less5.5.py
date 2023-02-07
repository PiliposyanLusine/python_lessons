x=int(input("Enter a number: "))
def  countSetBits(x):
    count = 0
    while (x):
        count += x & 1
        x >>= 1
    return count
print(countSetBits(x))
