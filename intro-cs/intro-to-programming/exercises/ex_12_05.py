"""
Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv receives characters (newlines and all), not lines.

"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter URL: ')
if len(url) < 1:
    url = 'http://data.pr4e.org/romeo.txt'
host = url.split('//')[1].split('/')[0]
text = ''
try:
    mysock.connect((host, 80))
    cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(url).encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        text += data.decode()

    mysock.close()

except:
    print('Invalid URL!')

content = text.split('\r\n')[-1]
for line in content.split('\n'):
    print(line)
