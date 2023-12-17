def logger(func):
    def wrapper(*args):
        all_args = [str(arg) for arg in args]
        print(f"{func.__name__} called with " + ", ".join(all_args))
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(5, 6, 7, 8, 9)
