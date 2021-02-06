"""
Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.


"""

fname = input('Enter a file name: ')
d = {}
with open(fname, 'r') as f:
    for line in f:
        if line.startswith('From '):
            email = line.split()[1]
            d[email] = d.get(email, 0) + 1

print(d)


