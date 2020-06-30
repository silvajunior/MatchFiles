from datetime import datetime

dateTime = datetime.now()
now = dateTime.strftime("%d%b%Y%H%M%S%f")

namefileError = "output/fileError"+now+".txt"

base = input("Enter the base file: ")
error = input("Enter the error file: ")

fileBase = open(base,'r')
fileError = open(error,'r')
newFile = open(namefileError, "a")

err = {}
newFileRows = []

for row in fileError:
  n = row.split(']')[0]
  n = n.lstrip('[')
  row = row.split(']')[1]
  n = int(n)
  err[n] = row

i=1

for row in fileBase:
  if(err.get(i, False) == False):
    newFileRows.append(row)
  else:
    newFileRows.append(row.rstrip("\n")+' '+err[i])
  i+=1

newFile.writelines(newFileRows) 

fileBase.close()
fileError.close()
newFile.close()