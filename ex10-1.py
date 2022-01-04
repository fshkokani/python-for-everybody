file=input('Enter file name: ')
file=open(file)
d=dict()
for line in file:
    line=line.rstrip()
    words=line.split()
    if len(words)==0 or words[0]!='From':
        continue
    else:
        if words[1] not in d:
            d[words[1]]=1
        else:
            d[words[1]]=d[words[1]]+1
emails=list()
for key,value in list(d.items()):
    emails.append((value,key))
emails.sort()
x,y=emails[-1]
print(y, x)
