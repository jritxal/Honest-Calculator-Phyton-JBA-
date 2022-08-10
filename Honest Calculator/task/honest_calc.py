# write your code here
def is_one_digit(v):
    try:
        if not float(v).is_integer():
            return False
    except ValueError:
        return False
    else:
        if -10 < v < 10:
            return True
        else:
            return False


def check(v_1, v_2, v_3):
    msg = ""
    if is_one_digit(v_1) and is_one_digit(v_2):
        msg += " ... lazy"
    if (v_1 == 1 or v_2 == 1) and v_3 == "*":
        msg += " ... very lazy"
    if (v_1 == 0 or v_2 == 0) and (v_3 in ["*", "+", "-"]):
        msg += " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
        print(msg)


numbers_correct = False
operation_correct = False
division_by_zero = True
memory = 0
result = 0
while not numbers_correct and not operation_correct and division_by_zero:
    print("Enter an equation")
    calc = input()
    x, operation, y = calc.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
    else:
        try:
            y = float(y)
        except ValueError:
            print("Do you even know what numbers are? Stay focused!")
        else:
            numbers_correct = True
    if numbers_correct:
        if operation != "+" and operation != "-" and operation != "*" and operation != "/":
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            numbers_correct = False
        else:
            operation_correct = True
    if operation_correct:
        check(x, y, operation)
        if operation == "+":
            result = x + y
            division_by_zero = False
        elif operation == "-":
            result = x - y
            division_by_zero = False
        elif operation == "*":
            result = x * y
            division_by_zero = False
        elif operation == "/" and y != 0:
            result = x / y
            division_by_zero = False
        else:
            print("Yeah... division by zero. Smart move...")
            numbers_correct = False
            operation_correct = False
    ask_memory = True
    if not (not numbers_correct and not operation_correct and division_by_zero):
        while ask_memory:
            print(result)
            print("Do you want to store the result? (y / n):")
            answer = input()
            if answer == "y":
                if is_one_digit(result):
                    msg_index = 10
                    print("Are you sure? It is only one digit! (y / n)")
                    reply = input()
                    while reply not in ["y", "n"]:
                        print("Are you sure? It is only one digit! (y / n)")
                        reply = input()
                    if reply == "y":
                        print("Don't be silly! It's just one number! Add to the memory? (y / n)")
                        reply = input()
                        while reply not in ["y", "n"]:
                            print("Don't be silly! It's just one number! Add to the memory? (y / n)")
                            reply = input()
                        if reply == "y":
                            print("Last chance! Do you really want to embarrass yourself? (y / n)")
                            reply = input()
                            while reply not in ["y", "n"]:
                                print("Last chance! Do you really want to embarrass yourself? (y / n)")
                                reply = input()
                            memory = result
                else:
                    memory = result
                ask_memory = False
            else:
                if answer == "n":
                    ask_memory = False
        proper_answer = False
        while not proper_answer:
            print("Do you want to continue calculations? (y / n):")
            continue_calcs = input()
            if continue_calcs == "y":
                proper_answer = True
                numbers_correct = False
                operation_correct = False
                division_by_zero = True
            elif continue_calcs == "n":
                proper_answer = True
