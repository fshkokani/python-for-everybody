count=0
file=input('Enter a file name: ')
file=open(file)
for line in file:
    line=line.rstrip()
    words=line.split()
    if len(words)==0 or words[0] != 'From' :
        continue
    print(words[1])
    count=count+1
print('There were', count, 'lines in the file with From as the first word')
