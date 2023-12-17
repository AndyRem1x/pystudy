class Library:

    def __init__(self):
        self.library = {}

    def __repr__(self):
        return f"{self.library}"

    def __str__(self):
        return f"My library: {self.library}."

    def new_book(self, name: str, year: int, author):
        if name in self.library:
            print(f'Book named "{name}" is already in the library. \n')
            return None
        new_book = Book(author, name, year)
        self.library[name] = new_book
        if name not in author.books:
            author.books.append(name)
        return new_book

    def group_by_author(self, author):
        return [book_name for book_name, info in self.library.items() if info.author == author]

    def group_by_year(self, year: int):
        return [info for _, info in self.library.items() if info.year == year]


class Book:

    def __init__(self, author, name, year):
        self.author = author
        self.name = name
        self.year = int(year)

    def __repr__(self):
        return f"'{self.author}', {self.year}"

    def __str__(self):
        return f'Book "{self.name}", written by {self.author} in {self.year} year'


class Author:

    def __init__(self, name, birthday, books, country):
        self.name = name
        self.birthday = birthday
        self.books = books or []
        self.country = country

    def __repr__(self):
        return (
            f"'Name': {self.name}. 'Birthday': {self.birthday}. "
            f"'Books': {self.books}. 'Country': {self.country}")

    def __str__(self):
        return f"{self.name}"


author1 = Author("Jack London", "12.01.1876", ["White Fang", "Martin Eden"], "USA",)
author2 = Author("Charles Dickens", "07.02.1812", ["Oliver Twist", "Bleak House"], "Great Britain",)
author3 = Author("Arthur Conan Doyle", "22.05.1859", ["The Sign of Four", "A False Start"], "Great Britain")

my_library = Library()
my_library.new_book("The Game", 1905, author1)
my_library.new_book("The Life", 1910, author1)
my_library.new_book("Hard Times", 1854, author2)
my_library.new_book("Little Dorrit", 1855, author2)
my_library.new_book("The Abbot", 1873, author3)
my_library.new_book("Pennarby Mine", 1893, author3)

print("Books in my library:", my_library, sep="\n")

print(f"\nBooks written by {author1}:")
print("In library:", my_library.group_by_author(author1))
print("In author object: ", author1.books)

print(f"\nBooks written by {author2}:")
print("In library:", my_library.group_by_author(author2))
print("In author object: ", author2.books)

print(f"\nBooks written by {author3}:")
print("In library:", my_library.group_by_author(author3))
print("In author object: ", author3.books)

print("\nBooks published in 1910:", my_library.group_by_year(1910))
print("\nBooks published in 1893:", my_library.group_by_year(1893))
print("\nBooks published in 1855:", my_library.group_by_year(1855))
