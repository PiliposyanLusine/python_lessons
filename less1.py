num = int(input('Enter number:'))
n = 2
first = 0
second = 1
fib_n = 1
if num == 0:
    print(first)
elif num == 1:
    print(second)
else:
    while n != num + 1:
        fib_n = first + second
        first = second
        second = fib_n
        n += 1
    print(fib_n)
