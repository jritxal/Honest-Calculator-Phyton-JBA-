from string import ascii_letters

word = input()
vowels = ["a", "e", "i", "o", "u"]
for letter in word:
    if letter in vowels:
        print("vowel")
    elif letter in ascii_letters:
        print("consonant")
    else:
        break
