done = False
li = []
while not done:
    try:
        x = input('Enter a number: ')
        if x == 'done':
            done = True
        else:
            li.append(float(x))
    except:
        print('Invalid input.')

print('Maximum:', max(li))
print('Minimum:', min(li))
