n = input()
floats = []
while n != ".":
    floats.append(float(n))
    n = input()
print(min(floats))
