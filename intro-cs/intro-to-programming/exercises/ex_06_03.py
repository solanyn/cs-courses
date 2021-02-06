"""Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments."""

def count(string, letter):
    count = 0
    for ch in string:
        if letter == ch:
            count += 1
    return count

word = 'banana'
print(count('banana', 'a'))

