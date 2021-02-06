"""
Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter URL: ')

host = url.split('//')[1].split('/')[0]

try:
    mysock.connect((host, 80))
    cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(url).encode()
    mysock.send(cmd)
    count = 0
    text = ''
    while True:
        data = mysock.recv(5120)
        if len(data) < 1:
            break
        text += data.decode()
        count += len(data)

    mysock.close()
    print(text[:3000])
    print(count)

except:
    print('Invalid URL!')
