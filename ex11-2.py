count=0
sum=0
import re
file=input('Enter file: ')
file=open(file)
for line in file:
    x=re.findall('^New Revision: (.*)',line)
    if len(x)>0:
        sum=sum+int(x[0])
        count=count+1
print(int(sum/count))
