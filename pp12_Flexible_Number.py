def flexNumber(*args):
    Tnumber = 0
    for i in args:
        Tnumber += i
    return Tnumber
#
print('Flexible Numbers ==> 2, 4, 12, 23 ')
print('Answer           ==> ', flexNumber(2,4,12,23))
#
print('')
#
print('Flexible Numbers ==> 2, 4 ')
print('Answer           ==> ', flexNumber(2,4))
