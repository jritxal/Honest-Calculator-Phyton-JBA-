word = input()
counter = -1
for letter in word:
    if letter != word[counter]:
        print("Not palindrome")
        break
    counter -= 1
else:
    print("Palindrome")
