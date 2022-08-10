height = int(input())
counter = 1
while height > 0:
    print(" " * (height - 1) + "#" * counter)
    height -= 1
    counter += 2
