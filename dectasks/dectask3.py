def arg_rules(type_: type, max_length: int, contains: list):
    def wrapper(func):
        def second_wrapper(name):
            if not (type(name) is type_):
                return False
            if not (len(name) <= 15):
                return False
            for elem in contains:
                if not (elem in name):
                    return False
            return func(name)
        return second_wrapper
    return wrapper


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('05years') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

