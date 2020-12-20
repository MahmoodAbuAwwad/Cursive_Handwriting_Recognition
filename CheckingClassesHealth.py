i=0
names=[]
file1 = open('annotations.txt', 'r') 
Lines = file1.readlines()


#checking health of Test Classes
import os.path
for line in Lines:
  if (len(line.split(',')[5].strip())>1):
      print((line.split(',')[0]))

print("---------------------------------------------------")
# Strips the newline character 
for line in Lines:
  if os.path.isfile(line.split(',')[0]):
      i=i+1
  else:
      names.append(line.split(',')[0])
print(i)
print(len(names))
print(names)