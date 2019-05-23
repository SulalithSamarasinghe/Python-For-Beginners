print('For loops for arrays ==>')
print('')
#
Array = ['a','b','c','d']
#
print('Array = ',Array)
print('')
#
for item in Array:
    print(item)
#
print('')
print('For loops with range ==>')
#
for i in range(0,10):
    print('')
    print('i ==> ',i)
#
print('')
print('For loops with increment ==>')
#
for i in range(0,10,2):
    print('')
    print('i ==> ',i)
#
print('')
print('For loops with break ==>')
#
for i in range(0,10):
    print('')
    if i == 5:
        print('i ==> ',i)
        break
    else:
        print('i is not equal to ==> ',i)
#
