import re


class Email:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        correct = r'^[a-zA-Z0-9]+(?:[._-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(correct, self.email):
            raise ValueError("Invalid email address")


valid_email_1 = Email("abcd@gmail.com")
valid_email_2 = Email("abc-d@mail.com")
valid_email_3 = Email("abc.def@mail.cc")

try:
    invalid_email = Email("abcd.efgh@mail")
except ValueError as e:
    print(e)

try:
    invalid_email_2 = Email("abcd#efgh@mail.com")
except ValueError as e:
    print(e)

try:
    invalid_email_3 = Email("abcd-@mail.com")
except ValueError as e:
    print(e)
