s=list()
while True:
    x=input('Enter a number: ')
    if x=='done': break
    s=s+[x]
print('Maximum: ', max(s))
print('Minimum: ', min(s))
