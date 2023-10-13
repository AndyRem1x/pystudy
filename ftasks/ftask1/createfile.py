import os

current_dir = os.path.dirname(os.path.realpath(__file__))


def create_file():
    with open(os.path.join(current_dir, "myfile.txt"), 'w') as file_object:
        file_object.write("Hello file world!")


create_file()
