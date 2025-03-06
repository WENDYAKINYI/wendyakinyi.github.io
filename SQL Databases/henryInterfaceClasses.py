

class Author:
    def __init__(self, author_num, last_name, first_name):
        self.author_num = author_num
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book:
    def __init__(self, book_code, title, price):
        self.book_code = book_code
        self.title = title
        self.price = price

    def __str__(self):
        return self.title
