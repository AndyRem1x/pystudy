from mystack import MyStack


def is_brackets_balanced(string):
    new_stack = MyStack()
    open_braces = ["(", "[", "{"]
    close_braces = [")", "]", "}"]
    for characters in string:
        if characters in open_braces:
            new_stack.push((open_braces.index(characters), characters))
        if characters in close_braces:
            index_last_brace, _ = new_stack.peek() or (None, None)
            if index_last_brace == close_braces.index(characters):
                new_stack.pop()
    if new_stack.empty():
        return True
    return False


if __name__ == "__main__":
    assert is_brackets_balanced("(string) {with} [brackets]") is True
    assert is_brackets_balanced("(string {with}) [brackets]") is True
    assert is_brackets_balanced("{string [with]} (brackets)") is True
    assert is_brackets_balanced("({[string with brackets]})") is True
    assert is_brackets_balanced("(string {with)} [brackets]") is False
    assert is_brackets_balanced("[string {with} [brackets]") is False
    assert is_brackets_balanced("(string {[with)} [brackets]") is False
    assert is_brackets_balanced("(string {(with)} [[brackets]") is False
