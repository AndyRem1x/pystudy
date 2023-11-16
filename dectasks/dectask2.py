def stop_words(words: list):

    def wrapper(func):
        def second_wrapper(name):
            slogan = func(name)
            for word in words:
                slogan = slogan.replace(word, "*")
            return slogan
        return second_wrapper
    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"