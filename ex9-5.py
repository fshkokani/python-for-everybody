d=dict()
file=input('Enter file name: ')
file=open(file)
for line in file:
    line=line.rstrip()
    line=line.split()
    if len(line)==0 or line[0]!= 'From':
        continue
    else:
        x=line[1]
        index=x.find('@')
        x=x[index+1:]
        d[x]=d.get(x,0)+1

print(d)
