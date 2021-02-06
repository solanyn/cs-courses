fname = input('Enter a file name: ')

try:
    f = open(fname)
except:
    print('File could not be opened:', fname)
    quit()

for line in f:
    print(line.rstrip().upper())
