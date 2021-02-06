"""
Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).


"""

f = open('mbox-short.txt')
d = dict()

for line in f:
    if line.startswith('From '):
        day = line.split()[2]
        d[day] = d.get(day, 0) + 1

print(d)
