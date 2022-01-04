file=input('Enter file name: ')
file=open(file)
d=dict()
for line in file:
    line=line.rstrip()
    words=line.split()
    if len(words)==0 or words[0]!='From': continue
    else:
        clock=words[5].split(':')
    if clock[0] not in d:
        d[clock[0]]=1
    else:
        d[clock[0]]=d[clock[0]]+1
pairs=list(d.items())
pairs.sort()
for key,value in pairs:
    print(key,value)
