# put your python code here
a = int(input())
b = int(input())
numbers = []
for n in range(a, b + 1):
    if n % 3 == 0:
        numbers.append(n)
print(sum(numbers) / len(numbers))
