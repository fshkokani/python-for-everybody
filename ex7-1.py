name=input('Enter a file name: ')
file=open(name)
for line in file:
    line = line.rstrip()
    line=line.upper()
    print(line)
