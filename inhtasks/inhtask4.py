class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.log_error(msg)

    def log_error(self, msg):
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Error: {msg}\n")


try:
    raise CustomException("This is a custom error message.")
except CustomException as ce:
    print(f"Caught CustomException: {ce}")
