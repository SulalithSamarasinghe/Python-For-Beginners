#Create an array
newArray = [1,2,3,4,5]
#
#print array
print('print array ==>')
print('newArray = ',newArray)
#
#Select a specific item from the array
print('')
print('Select a specific item from the array ==>')
print('newArray[0] = ', newArray[0])
#
#Select a specific section from the array
print('')
print('Select a specific section from the array ==>')
print('newArray[0:3] = ', newArray[0:3])
#
#Replace item from the array
print('')
print('Replace item from the array ==>')
newArray[4] = 6
print('newArray = ', newArray)
#
#Delete items from the array
print('')
print('Delete items from the array ==>')
newArray[4:5] = []
print('newArray = ', newArray)
#
#Add items to the array
print('')
print('Add items to the array ==>')
newArray = newArray + [5]
print('newArray = ', newArray)
#Add items to the array by a method
print('')
print('Add items to the array by a method==>')
newArray.append(6)
print('newArray = ', newArray)
