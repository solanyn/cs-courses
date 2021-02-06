"""
Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.


"""

fname = input('Enter a file name: ')
d = {}
with open(fname, 'r') as f:
    for line in f:
        if line.startswith('From '):
            h = line.split()[-2].split(':')[0] 
            d[h] = d.get(h, 0) + 1

for k, v in sorted(d.items()):
    print(k, v)
