# Exercise 2: Change your socket program so that it counts the number
#of characters it has received and stops displaying any text after it has
#shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count
#of the number of characters at the end of the document.

import socket
import re

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    URL=input('Enter URL: ')
    server=re.findall('.+//(.+)/',URL)
    print(server)
    mysock.connect((server[0],80))
    cmd = ('GET ' + URL + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    count=0
    while True:
        data=mysock.recv(512).decode()
        count=len(data)+count
        if count<3000:
            print(data)
        if len(data) < 1:
            break
    mysock.close()
except:
    print('improperly formatted or non-existent URL')

print('the count of the number of characters at the end of the document', count)
