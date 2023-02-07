list = []
x = 100
y = 0
z = 0
while x <= 1000:
    z = x // 100
    y = x % 10
    if z == y:
        list.append(x)
    x += 1
print(*list, sep= "\n")
