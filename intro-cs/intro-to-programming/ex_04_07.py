"""
Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
"""

def computegrade(score):
    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'

try:
    score = float(input("Enter score: "))
    if score > 1 or score < 0:
        raise ValueError('Bad score')
    print(computegrade(score))
except:
    print('Bad score')

