import csv

books = []


class Book:
    def __init__(self, title, author, read=False):
        self.title = title
        self.author = author
        self.read = read

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "read": self.read
        }

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author


class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.get_title().lower() == book.get_title().lower() and existing_book.get_author().lower() == book.get_author().lower():
                print("You already own this book.")
                return
        self.books.append(book)
        print("Book added successfully.")

    def remove_book(self, book):
        if book not in self.books:
            print("The book is not in your collection.")
            return
        self.books.remove(book)
        print("Book removed successfully.")

    def list_books(self):
        if not self.books:
            print("Your collection is empty.")
            return
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Read: {book.read}")

    def mark_book_as_read(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.read = True
                print("Book marked as read.")
                return
        print("The book is not in your collection.")

    def search_books(self, search_term, search_by="title"):
        result = []
        search_term = search_term.lower()

        for book in self.books:
            if search_by.lower() == "title" and book.get_title().lower() == search_term:
                result.append(book)
            elif search_by.lower() == "author" and book.get_author().lower() == search_term:
                result.append(book)
            elif search_by.lower() == "read" and book.read == (search_term == "read"):
                result.append(book)

        if not result:
            print("No books found.")
            return
        for book in result:
            print(f"Title: {book.title}, Author: {book.author}, Read: {book.read}")

    def has_read_book(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower() and book.read:
                return True
        return False

    def has_book(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                return True
        return False

    def delete_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Book deleted successfully.")
                return
        print("The book is not in your collection.")

    def save_books_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "Read"])
            for book in self.books:
                writer.writerow([book.get_title(), book.get_author(), str(book.read)])
        print("Books saved to CSV successfully.")

    def load_books_from_csv(self, filename):
        self.books = []
        with open(filename, "r") as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header row
            for row in reader:
                title, author, read = row
                book = Book(title, author)
                book.read = bool(read)  # Convert the read value to boolean
                self.add_book(book)
        print("Books loaded from CSV successfully.")
