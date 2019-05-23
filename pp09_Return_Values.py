def power(value,p):
    #
    powerV =  value**p
    #
    return powerV
#
print('Enter Value and Power, ')
print('')
value = float(input('Enter Value : '))
p = int(input('Enter Power : '))
print('')
#
print('Result ==> ',power(value,p))
