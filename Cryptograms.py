# Miles Woollacott, methods of scrambling strings

import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

scrambletype = ["augmenting", "declining", "harmonic", "a", "d", "h"]

fulltypes = ["None (0 or n)", "Base (b)", "Increment (i)", "No Punctuation (p)", "Random Spacing (s)", "Upper (u)",
             "Zero Value (z)", "Reverse (r)"]
types = ["0", "n", "b", "i", "p", "s", "u", "z", "r"]

nonnatural = 1
base = True
increment = False
cipher = ''
punctuation = 0
default = "hello"
randomspace = 3
counter = 1
intg = False
lowered = 3
zerovalue = "."
apply = False
reverse = False

print()

text = input("Text: ")
text = text.upper()
while default not in scrambletype:
    default = input("Type? ")
    default = default.lower()
    if default not in scrambletype:
        print("Acceptable values are:", str(scrambletype))
while counter != 0:
    counter = 0
    nonnatural = input("Input any nonnatural criteria: ")
    nonnatural = nonnatural.lower()
    nonnatural = list(nonnatural)
    for i in nonnatural:
        if i not in types:
            print(str(i), "is not recognized. Values can be:", str(fulltypes))
            counter += 1
if nonnatural == "n" or nonnatural == "none" or nonnatural == "0":
    if default == "a" or default == "augmenting" or default == "h" or default == "harmonic":
        base = 1
        increment = 1
        punctuation = True
        randomspace = False
    else:
        base = -1
        increment = -1
        punctuation = True
        randomspace = False
else:
    while not intg:
        intg = True
        if "b" in nonnatural:
            trial = input("Base? ")
            try:
                base = int(trial)
            except:
                print("Must be an integer.")
                intg = False
        else:
            if default == "d" or default == "declining":
                base = -1
            else:
                base = 1
    intg = False
    while not intg:
        intg = True
        if "i" in nonnatural:
            trial = input("Increment? ")
            try:
                increment = int(trial)
            except:
                print("Must be an integer.")
                intg = False
        else:
            if default == "d" or default == "declining":
                increment = -1
            else:
                increment = 1
    intg = False
    while not intg:
        intg = True
        if "s" in nonnatural:
            randomspace = True
        else:
            randomspace = False
    intg = False
    while not intg:
        intg = True
        if "p" in nonnatural:
            punctuation = False
        else:
            punctuation = True
    intg = False
    while not intg:
        intg = True
        if "u" in nonnatural:
            apply = True
    intg = False
    while not intg:
        intg = True
        if "z" in nonnatural:
            zerovalue = str(input("Zero Value? "))
            while len(zerovalue) != 1:
                print("Can only be one character length.")
                zerovalue = str(input("Zero Value? "))
    intg = False
    while not intg:
        intg = True
        if "r" in nonnatural:
            reverse = True

delta = base

length = random.randrange(2, 10)

word = 0

def modifier(coded, change):
    value_coded = alphabet.find(coded)
    new_letter = (value_coded + change) % 26
    return alphabet[new_letter]


for i in range(0, len(text)):
    letter = text[i:i + 1]
    if randomspace:
        word += 1
        if word == length:
            word = 0
            length = random.randrange(1, 10)
            cipher += " "
    if letter == " " and not randomspace:
        cipher += " "
        if letter == zerovalue:
            delta = base
    elif letter == zerovalue.upper():
        if zerovalue in alphabet.lower():
            cipher += modifier(letter, delta)
        else:
            cipher += zerovalue
        delta = base
    elif letter in alphabet:
        cipher += modifier(letter, delta)
        if lowered:
            cipher = cipher.lower()
        if letter == zerovalue.upper():
            delta = base
        if default == "harmonic" or default == "h":
            if delta < 0:
                delta -= increment
            else:
                delta += increment
            delta *= -1
        else:
            delta += increment
    else:
        if default == "harmonic" or default == "h":
            if delta < 0:
                delta -= increment
            else:
                delta += increment
            delta *= -1
        else:
            delta += increment
        if punctuation:
            cipher += letter
            if letter == zerovalue.upper():
                delta = base
if apply:
    cipher = cipher.upper()

if reverse:
    cipherlist = list(cipher)
    cipher = ""
    for i in range(len(cipherlist) + 1):
        if i != 0:
            cipher += cipherlist[-i]


print()
print(cipher)
