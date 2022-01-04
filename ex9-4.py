d=dict()
file=input('Enter file name: ')
file=open(file)
for line in file:
    line=line.rstrip()
    line=line.split()
    if len(line)==0 or line[0]!= 'From':
        continue
    else:
        d[line[1]]=d.get(line[1],0)+1
x=0
y=None
for key in d:
    if d[key]>x:
        x=d[key]
        y=key


print(y,x)
