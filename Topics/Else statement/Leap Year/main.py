# put your python code here
n = int(input())
a = 4
b = 100
c = 400
print("Leap" if n % a == 0 and n % b != 0 or n % c == 0 else "Ordinary")
