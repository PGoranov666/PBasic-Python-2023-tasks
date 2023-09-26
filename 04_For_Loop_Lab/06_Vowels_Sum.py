text = input()
vowels = 0
for characters in text:
    if characters == "a":
        vowels += 1
    elif characters == "e":
        vowels += 2
    elif characters == "i":
        vowels += 3
    elif characters == "o":
        vowels += 4
    elif characters == "u":
        vowels += 5
print(vowels)