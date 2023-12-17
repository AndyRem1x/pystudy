def make_operation(operator, *args):
    if not args:
        return "No arguments provided"
    result = args[0]
    if operator == "+":
        for i in range(1, len(args)):
            result += args[i]
    elif operator == "-":
        for i in range(1, len(args)):
            result -= args[i]
    elif operator == "*":
        for i in range(1, len(args)):
            result *= args[i]
    else:
        return "This operator is unsupported"
    return result


#  passing test arguments
print(make_operation('+', 1, 23, 4, 5))
print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
