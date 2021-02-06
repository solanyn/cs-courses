"""
Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.


"""

fname = input('Enter a file name: ')
d = dict()
with open(fname, 'r') as f:
    for line in f:
        if line.startswith('From '):
            e = line.split()[1]
            d[e] = d.get(e, 0) + 1

count, email = sorted([(v, k) for k, v in d.items()], reverse=True)[0]
print(email, count)
            
