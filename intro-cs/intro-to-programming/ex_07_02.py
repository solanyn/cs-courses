fname = input('Enter the file name')
try:
    f = open(fname)
except:
    print('The file could not be opened')
    quit()

total = 0
count = 0

for line in f:
    if 'X-DSPAM-Confidence: 0.8475' in line:
        print(line)
        i = line.find(': ') + 1
        total += float(line[i:len(line)])
        count += 1

print('Average spam confidence:', total / count)
