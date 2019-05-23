import pp16_Modules_02 as M2
import random as r
#
value = float(input('Enter value : '))
p = int(input('Enter power : '))
#
print(value,' to the power',p,' ==> ',M2.power(value,p))
print('')
print('Random number between 1 to 200 ==> ',r.randrange(1,200))
