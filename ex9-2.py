d=dict()
file=input('Enter file name: ')
file=open(file)
count=0
for line in file:
    line=line.rstrip()
    words=line.split()
    if len(words)==0 or words[0] != 'From':
        continue
    else:
        d[words[2]]=d.get(words[2],0)+1
print(d)
