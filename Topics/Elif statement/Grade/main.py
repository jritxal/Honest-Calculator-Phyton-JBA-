score = int(input())
max_ = int(input())
percentage = (score / max_) * 100
ranks = (90, 80, 70, 60)
if percentage >= ranks[0]:
    print("A")
elif percentage >= ranks[1]:
    print("B")
elif percentage >= ranks[2]:
    print("C")
elif percentage >= ranks[3]:
    print("D")
else:
    print("F")
