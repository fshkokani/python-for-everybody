#Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received.
#Remember that recv receives characters (newlines and all), not lines.



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
    count=0
    while True:
        data = mysock.recv(512).decode()
        if len(data) < 1:
            break
        count=len(data)+count
        if count<3000:
            x=data.rsplit('\r\n\r\n')
            print(x[-1])
    mysock.close()

except:
    print('improperly formatted or non-existent URL')
