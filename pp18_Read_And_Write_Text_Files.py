#
#Write a text file
#
creatFile = open('test.txt','w')
creatFile.write('File No.01 ==>\n')
creatFile.write('Write a text file by python!')
creatFile.close()
#
#Read a text file
#
readFile = open('test.txt','r')
content = readFile.read()
print(content)
readFile.close()
