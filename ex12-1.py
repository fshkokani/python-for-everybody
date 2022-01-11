#Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
#You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call.
#Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    URL= input('Enter URL: ')
    host=URL.split('/')
    mysock.connect((host[2], 80)) # make a connection to port 80 on the server www.py4e.com.
    cmd = 'GET ' + URL + ' HTTP/1.0\r\n\r\n' # Since our program is playing the role of the “web browser”,
    # the HTTP protocol says we must send the GET command followed by a blank line.
    #\r\n signifies an EOL (end of line), so \r\n\r\n signifies nothing between two EOL sequences.
    #That is the equivalent of a blank line.
    mysock.send(cmd.encode())
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')
    mysock.close()
except:
    print('improperly formatted or non-existent URL')
