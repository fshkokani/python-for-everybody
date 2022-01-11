#Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL,
# (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request, urllib.parse, urllib.error
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    URL=input('Enter URL: ')
    file=urllib.request.urlopen(URL,context=ctx)
    count=0
    for line in file:
        line=line.decode()
        line=line.strip()
        count=count+len(line)
        if count<3000:
            print(line)
except:
    print('improperly formatted or non-existent URL')
print('the count of the number of characters at the end of the document', count)
