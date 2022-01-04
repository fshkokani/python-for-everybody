name=input('Enter the file name: ')
file=open(name)
counter=0
number=0
for line in file:
    line=line.rstrip()
    if line.startswith('X-DSPAM-Confidence:') == True:
        counter=counter+1
        number=float(line[21:])+number
print('Average spam confidence: ',number/counter)
