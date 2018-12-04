"""
CP1404/CP5632 Practical
Program to count the occurrences of words in a string
"""

text = str(input("Text: "))
words = text.split()
words.sort()

counts = dict()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for word in counts:
    print (str(word) + ": " + str(counts[word]))