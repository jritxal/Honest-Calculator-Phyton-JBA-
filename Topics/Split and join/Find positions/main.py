# put your python code here
numbers = input().split()
key_number = input()
founded = []
count = 0
while count < len(numbers):
    if numbers[count] == key_number:
        founded.append(str(count))
    count += 1
print(" ".join(founded) or "not found")
