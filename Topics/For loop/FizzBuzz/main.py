max_ = 100 + 1

for i in range(1, max_):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        if i % 5 == 0:
            print("Buzz")
        else:
            print(i)
