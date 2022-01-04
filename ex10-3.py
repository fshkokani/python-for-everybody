d=dict()
file=input('Enter file name: ')
file=open(file)
import string
for line in file:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    line=line.rstrip()
    words=line.split()
    for word in words:
        for letter in word:
            try:
                float(letter)
                continue
            except:
                if letter not in d:
                    d[letter]=1
                else:
                    d[letter]=d[letter]+1
k=list()
for key,val in list(d.items()):
    k.append((val,key))
k.sort()
for val, key in k:
    print(key)
