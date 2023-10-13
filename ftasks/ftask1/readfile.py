import os

current_dir = os.path.dirname(os.path.realpath(__file__))


def read_file():
    with open(os.path.join(current_dir, "myfile.txt"), 'r') as file_object:
        content = file_object.read()
    print(content)


read_file()
