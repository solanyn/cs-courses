"""
Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.


"""

fname = input('Enter a file name: ')
d = {}
with open(fname, 'r') as f:
    for line in f:
        if line.startswith('From '):
            email = line.split()[1]
            d[email] = d.get(email, 0) + 1


most = None
count = None
for email in d.keys():
    if most is None or d[email] > count:
        most = email
        count = d[email]

print(most, count)
    

