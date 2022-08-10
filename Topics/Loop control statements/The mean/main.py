n = input()
numbers = []
while n != ".":
    numbers.append(int(n))
    n = input()
print(sum(numbers) / len(numbers))
