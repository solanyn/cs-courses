fname = input('Enter file: ')
try:
    f = open(fname, 'r')
except:
    print('File not found. ')
    quit()
    
dictionary = list()

for line in f:
    words = line.split()
    for word in words:
        if word not in dictionary:
            dictionary.append(word)

dictionary.sort()
print(dictionary)
