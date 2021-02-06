"""
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
"""

def computepay(hours, rate):
    if hours < 40:
        return hours * rate
    else:
        return (hours - 40) * rate * 1.5 + 40 * rate


try:
    hours = float(input("Enter Hours: "))
except:
    print('Invalid hours')

try:
    rate = float(input("Enter Rate: "))
except:
    print('Invalid rate')

print(computepay(hours, rate))
        
