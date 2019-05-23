def power(value,p):
    #
    powerV =  value**p
    #
    return powerV
#
calList = []
#
print('Enter Value and Power, ')
print('')
value = float(input('Enter Value : '))
p = int(input('Enter Power : '))
calList.append(value)
calList.append(p)
print('')
#
print('Result ==> ',power(*calList))
