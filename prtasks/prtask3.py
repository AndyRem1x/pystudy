class TypeDecorators:

    @staticmethod
    def to_int(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return int(result)

        return wrapper

    @staticmethod
    def to_str(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)
        return wrapper

    @staticmethod
    def to_bool(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return bool(result)
        return wrapper

    @staticmethod
    def to_float(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return float(result)
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_str
def do_something1(string: int):
    return string


@TypeDecorators.to_float
def do_something2(string: int):
    return string


assert do_nothing('100500') == 100500
assert do_something1(100) == "100"
assert do_something2(500) == 500.0
assert do_something('True') is True
