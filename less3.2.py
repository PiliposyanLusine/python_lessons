str=input('Enter telephone number: ')
length = len(str)
if length==14 :
    if str[1]=="-" and str[5]=="-" and str[9]=="-" :
        print('Valid')
    if str[3]=="-" and str[7]=="-" :
        print ('Valid')
    if str[3]=="-" and str[8]=="-" :
        print('Valid')
else :
    print ('Invalid')

