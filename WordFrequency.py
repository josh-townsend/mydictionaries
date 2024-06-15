import os

with open('sometext-1.txt' , 'r') as text:
    lines = text.readlines()

words_freq= {}

text = ''.join(lines)

words = text.split()

for word in words:
    if word in words_freq:
        words_freq[word] +=1
    else:
        words_freq[word] = 1

    print(f"The word {word} appears {words_freq[word]} times.")