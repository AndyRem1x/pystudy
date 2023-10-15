def func1():
    def func2():
        return "This is func2"
    return func2


print(func1()())
