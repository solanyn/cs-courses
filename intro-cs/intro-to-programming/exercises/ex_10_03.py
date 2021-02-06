"""
Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

"""

fname = input('Enter a file name: ')
d = {}
with open(fname, 'r') as f:
    text = f.read()

for ch in text.lower():
    if ch.isalpha():
        d[ch] = d.get(ch, 0) + 1

sorted_d = sorted([(v, k) for k, v in d.items()], reverse=True)

for v, k in sorted_d:
    print(k, v)
