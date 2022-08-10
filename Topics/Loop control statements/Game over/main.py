scores = input().split()
# put your python code here
fails = 0
score = 0
for answer in scores:
    if answer == "C":
        score += 1
    else:
        fails += 1

    if fails == 3:
        print("Game over")
        break
else:
    print("You won")
print(score)
