"""
Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
"""

min = float('inf')
max = float('-inf')
done = False
while not done:
    x = input('Enter a number: ')
    if x == 'done':
        done = True
    else:
        try:
            x = float(x)
            if x > max:
                max = x
            if x < min:
                min = x
        except:
            print('Invalid input')

print(max, min)
