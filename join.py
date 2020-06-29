from datetime import datetime

dateTime = datetime.now()
now = dateTime.strftime("%d%b%Y%H%M%S%f")

namefileError = "fileError"+now+".txt"

fileBase = open('base.txt','r')
fileError = open('error.txt','r')
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