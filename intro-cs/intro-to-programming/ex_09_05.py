"""
Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.


"""

f = input('Enter a file name: ')
d = {}
with open(f, 'r') as f:
    for line in f:
        if line.startswith('From '):
            words = line.split()
            domain = words[1].split('@')[1]
            d[domain] = d.get(domain, 0) + 1

print(d)

