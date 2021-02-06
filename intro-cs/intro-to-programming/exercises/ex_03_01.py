"""
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
"""

hrs = float(input('Enter Hours'))
rate = float(input('Rate'))

if hrs > 40:
    pay = rate * 40 + 1.5 * rate * (hrs - 40)
else:
    pay = rate * hrs

print('Pay:', pay)
