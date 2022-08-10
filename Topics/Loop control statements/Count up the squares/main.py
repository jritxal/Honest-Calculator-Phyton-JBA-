# put your python code here
n = int(input())
numbers = [n]
squares_sum = 0
squares_sum += n ** 2
while sum(numbers) != 0:
    n = int(input())
    squares_sum += n ** 2
    numbers.append(n)
print(squares_sum)
