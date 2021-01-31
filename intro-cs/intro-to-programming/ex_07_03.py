fname = input('Enter the file name: ')
try:
    f = open(fname)
except:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        quit()
    print('The file could not be opened')
    quit()

count = 0

for line in f:
    if 'subject' in line:
        count += 1

print('There were {} subject lines in {}'.format(count, fname))
