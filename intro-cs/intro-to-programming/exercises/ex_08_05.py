"""
Exercise 5: Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.c
"""

f = open('mbox-short.txt')

count = 0

for line in f:
    if line.startswith('From '):
        print(line.split()[1])
        count += 1

print('There were {} lines in the file with From as the first word'.format(count))
