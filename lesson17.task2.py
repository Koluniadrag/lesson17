class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author):
        books_by_author = []
        for book in self.books:
            if book.author == author:
                books_by_author.append(book)
        return books_by_author

    def group_by_year(self, year):
        books_by_year = []
        for book in self.books:
            if book.year == year:
                books_by_year.append(book)
        return books_by_year

    def __str__(self):
        return f"Библиотека {self.name} вмищае {len(self.books)} книг и {len(self.authors)} авторив."

    def __repr__(self):
        return f"Бибилиотека({self.name})"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)
        Book.total_books += 1

    def __str__(self):
        return f"{self.name}, {self.year}, від {self.author.name}"

    def __repr__(self):
        return f"Книга({self.name}, {self.year}, {self.author})"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []




