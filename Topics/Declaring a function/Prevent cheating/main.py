import math


# your code here
def override_factorial():
    print("Don't cheat!")


math.factorial = override_factorial

# don't delete this line, please
math.factorial(23)
