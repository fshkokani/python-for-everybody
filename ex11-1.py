#simulate the operation of the grep command on Unix
import re
count=0
print('$ python grep.py')
x=input('Enter a regular expression: ')
file=open('mbox.txt')
for line in file:
    line=line.rstrip()
    if re.search(x,line):

        count=count+1
print(type(re.search(x,line)))
print('mbox.txt had', count , 'lines that matched', x)
