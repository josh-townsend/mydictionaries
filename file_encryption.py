import os

encryption = {
    'A': "!", 'B': "@", 'C': '#', 'D': '$', 'E': '%', 'F': '^', 'G': '&', 'H': '*', 'I': '(', 'J': ')', 'K': '_', 'L': '-', 'M': '=',
    'N': '+', 'O': '`', 'P': '~', 'Q': '[', 'R': ']', 'S': '{', 'T': '}', 'U': '|', 'V': '1', 'W': '2', 'X': '3', 'Y': '4', 'Z': '5',
    'a': '6', 'b': '8', 'c': '9', 'd': '0', 'e': '>', 'f': '!', 'g': '&', 'h': '-', 'i': '$', 'j': '!', 'k': "'", 'l': '?', 'm': '_',
    'n': '/', 'o': '.', 'p': ';', 'q': ',', 'r': ':', 's': ';', 't': ']', 'u': '{', 'v': '<', 'w': '*', 'x': '"', 'y': '+', 'z': ')'
}


with open('info_security-1.txt' , 'r') as text:
    lines = text.readlines()

encrypted_lines = []

for line in lines:
    encrypted_words = []
    for word in line.split():
        encrypted_word = ''.join(encryption.get(char, char) for char in word)
        encrypted_words.append(encrypted_word)
    encrypted_lines.append(' '.join(encrypted_words))

encrypted_text = '\n'.join(encrypted_lines)
outfile = open('encrypted.txt' , 'w')
outfile.write(encrypted_text)
