def power(value = 2.0 ,p = 2):
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
print('Result for the input values ==> ',power(value,p))
print('Result without the input values ==> ',power())
print('Result without the input values, by only changing the base ==> ',power(value = 8.0))
