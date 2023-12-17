import os
import time


class MyFileContextManager:
    __counter = 0
    __log_name = "my_file_context_manager_log.txt"

    @classmethod
    def get_counter(cls):
        return cls.__counter

    @classmethod
    def get_log_name(cls):
        return cls.__log_name

    @classmethod
    def set_counter(cls):
        cls.__counter += 1

    @classmethod
    def reset_counter(cls):
        cls.__counter = 0

    @classmethod
    def create_log(cls):
        if not os.path.exists(cls.__log_name):
            with open(cls.__log_name, "w", encoding="UTF-8") as file_object:
                file_object.write("")

    @classmethod
    def update_log(cls, text):
        if os.path.exists(cls.__log_name):
            with open(cls.__log_name, "a", encoding="UTF-8") as file_object:
                log_time = time.strftime("%D %H:%M:%S")
                file_object.write(f"{log_time}: {text}\n")

    @classmethod
    def remove_file(cls, file_name=None):
        if file_name and os.path.exists(file_name):
            os.remove(file_name)

    def __init__(self, file_name, mode=None, encoding=None):
        self.file = file_name
        self.mode = mode or "r"
        self.encoding = encoding or "UTF-8"
        self.file_obj = None
        MyFileContextManager.create_log()

    def __enter__(self):
        MyFileContextManager.set_counter()
        if not os.path.exists(self.file) and self.mode not in ("w", "a"):
            MyFileContextManager.update_log(
                f'Trying to open a non-existent file "{self.file}" with mode "{self.mode}"'
            )
            raise FileNotFoundError
        self.file_obj = open(self.file, self.mode, encoding=self.encoding)
        MyFileContextManager.update_log(
            f'Open file "{self.file}" with mode "{self.mode}"'
        )
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        if exc_type is None:
            MyFileContextManager.update_log(
                f"Close file: File '{self.file}' was successfully processed."
            )
        else:
            MyFileContextManager.update_log(
                f"Close file: An error occurred while processing file '{self.file}': {exc_val}"
            )


if __name__ == "__main__":
    try:
        with MyFileContextManager("task1_1.txt", "r") as file:
            file.read()
    except FileNotFoundError:
        print("File not found!")

    with MyFileContextManager("task1_1.txt", "w") as file:
        file.write("Hello world!")

    with MyFileContextManager("task1_1.txt", "r") as file:
        print(file.read())

    with MyFileContextManager("task1_2.txt", "w") as file:
        file.write("Hello test world!")

    with MyFileContextManager("task1_2.txt", "r") as file:
        print(file.read())

    MyFileContextManager.remove_file("task1_1.txt")
    MyFileContextManager.remove_file("task1_2.txt")
    MyFileContextManager.reset_counter()
