times = int(input())
seven = 7
two = 2
for _ in range(times):
    n = int(input())
    if n % seven == 0:
        print(n ** two)
