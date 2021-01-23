try:
    hrs = float(input('Enter Hours: '))
except:
    print('Error, please enter numeric input')

try:
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input')

print('Pay:', hrs*rate)
