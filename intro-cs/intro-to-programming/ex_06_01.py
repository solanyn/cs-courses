"""
Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
"""

fruit = 'banana'
i = len(fruit) - 1

while i >= 0:
    print(fruit[i])
    i -= 1

# for ch in fruit[::-1]:
#     print(ch)
