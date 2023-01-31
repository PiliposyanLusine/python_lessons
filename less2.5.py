input_string = input('Enter elements of a list ')
def largest(input_string):
    large= input_string[0]
    for i in input_string:
        if i>large:
            large=i
    return large
print("largest in ",input_string,"is",largest(input_string))
