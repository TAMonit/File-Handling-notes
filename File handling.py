import os

#prints file content
print('1.')
file = open('example file for file handling.txt', 'r')
print(file.read())
file.close()

print('\n','\n')

#prints only 5 characters of file from start including spaces
print('2.')
file = open('example file for file handling.txt', 'r')
print(file.read(5))
file.close()

print("\n","\n")

#prints the 1st line of the file
print('3.')
file = open("E:\Python Projects\example file for file handling.txt", 'r')
print(file.readline())
file.close()

print("\n","\n")

#prints every line detailed using \n and symbols  
print('4.')
file = open('example file for file handling.txt', 'r')
print(file.readlines())
file.close()

print("\n","\n")

#prints all the lines of file using For loop
print('5.')
file = open('example file for file handling.txt', 'r')
for line in file:
   print(file.readlines())
file.close()

print("\n","\n")

#Creates a new file in the same folder as the python file and writes in it
print('6.')
file = open('i am TAM.txt', 'w')
file.write('Hello world')
file.write('Hello world again')
file.close()

print("\n","\n")

#Overwites the file content if the file exist
print('7.')
file = open('i am TAM.txt', 'w')
file.write('oops overwritten')
file.close()

print("\n","\n")

#Creates a new file and writes content in it, on duplicacy shows error
print('8.')
file = open('hello everyone.txt', 'x')
file.write("New File - TAM")
file.close()

print("\n","\n")

#Deletion of File
print('9.')
os.remove('hello everyone.txt')

print("\n","\n")

#Creates a new folder
print('10')
os.mkdir('created new folder for deletion')

print("\n","\n")

#Deletion of Folder
print('11.')
os.rmdir('created new folder for deletion')

print("\n","\n")

#Using if else to check if file exist if yes then delete it
print('12.')
if os.path.exists('i am TAM.txt'):
   os.remove('i am TAM.txt')
   print("File Deleted successfully")
else:
   print("The file does not exist")












