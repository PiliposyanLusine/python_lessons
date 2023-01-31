input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
numsum=0
for i in user_list:
    numsum+=int(i)
print('Sum of List: ',numsum)
