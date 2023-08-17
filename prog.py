class Greeting:
    def __init__(self, text):
        self.text = text
    def print_greeting(self):
        print(self.text)

quote = Greeting("Hello! Study python!")
quote.print_greeting()