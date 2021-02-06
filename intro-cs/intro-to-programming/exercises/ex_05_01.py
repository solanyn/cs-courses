"""
Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
"""
done = False
sum = 0
n = 0

while not done:
    x = input('Enter a number: ')
    if x == 'done':
        done = True
    else:
        try:
            x = float(x)
            sum += x
            n += 1
        except:
            print('Invalid input')

print(sum, n, sum / n)

