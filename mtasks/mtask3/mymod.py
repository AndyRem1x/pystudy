def count_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return f"File {filename} not found"


def count_chars(filename):
    try:
        with open(filename, "r") as file:
            chars = file.read()
            return len(chars)
    except FileNotFoundError:
        return f"File {filename} not found"


def test(filename):
    num_of_lines = count_lines(filename)
    num_of_chars = count_chars(filename)
    return f"Number of lines: {num_of_lines}. Number of chars: {num_of_chars}."


if __name__ == "__main__":
    test1 = test("file1.txt")
    print(test1)

    test2 = test("file2.txt")
    print(test2)
