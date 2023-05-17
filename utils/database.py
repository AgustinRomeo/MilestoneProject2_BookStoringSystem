import csv

books = []


class Book:
    def __init__(self, title, author, read=False):
        self.title = title
        self.author = author
        self.read = read

    def to_dict(self):
        return {
            "Title": self.title,
            "Author": self.author,
            "Read": str(self.read)
        }

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author


def search_books(search_term, search_by="title"):
    result = []
    search_term = search_term.lower()

    with open("books.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if search_by.lower() == "title" and row["Title"].lower() == search_term:
                book = Book(row["Title"], row["Author"], bool(row["Read"]))
                result.append(book)
            elif search_by.lower() == "author" and row["Author"].lower() == search_term:
                book = Book(row["Title"], row["Author"], bool(row["Read"]))
                result.append(book)
            elif search_by.lower() == "read" and row["Read"].lower() == search_term:
                book = Book(row["Title"], row["Author"], bool(row["Read"]))
                result.append(book)

    if not result:
        print("No books found.")

    return result


class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        with open("books.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([book.get_title(), book.get_author(), str(book.read)])
        print("Book added successfully.")

    def remove_book(self, book):
        with open("books.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            books_data = list(reader)

        # Find the index of the book in the CSV data
        index = None
        for i, row in enumerate(books_data):
            if row[0].lower() == book.get_title().lower() and row[1].lower() == book.get_author().lower():
                index = i
                break

        if index is None:
            print("The book is not in your collection.")
            return

        # Remove the book from the CSV data
        books_data.pop(index)

        with open("books.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "Read"])
            writer.writerows(books_data)

        print("Book removed successfully.")

    def list_books(self):
        with open("books.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            books_data = list(reader)

        if len(books_data) <= 1:
            print("Your collection is empty.")
            return

        for row in books_data[1:]:
            title, author, read = row
            print(f"Title: {title}, Author: {author}, Read: {read}")

    def mark_book_as_read(self, title):
        with open("books.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            books_data = list(reader)

        found = False
        for row in books_data[1:]:
            if row[0].lower() == title.lower():
                row[2] = "True"
                found = True
                break

        if not found:
            print("The book is not in your collection.")
            return

        with open("books.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(books_data)

        print("Book marked as read.")

    @staticmethod
    def has_read_book(title):
        with open("books.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Title"].lower() == title.lower() and row["Read"].lower() == "true":
                    return True
        return False

    @staticmethod
    def has_book(title):
        with open("books.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Title"].lower() == title.lower():
                    return True
        return False

    @staticmethod
    def delete_book(title):
        with open("books.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        found = False
        with open("books.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Read"])
            writer.writeheader()
            for row in rows:
                if row["Title"].lower() == title.lower():
                    found = True
                else:
                    writer.writerow(row)

        if found:
            print("Book deleted successfully.")
        else:
            print("The book is not in your collection.")

    @staticmethod
    def search_books(search_by, search_term):
        result = []
        search_term = search_term.lower()

        with open("books.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if search_by.lower() == "title" and row["Title"].lower() == search_term:
                    book = Book(row["Title"], row["Author"], bool(row["Read"]))
                    result.append(book)
                elif search_by.lower() == "author" and row["Author"].lower() == search_term:
                    book = Book(row["Title"], row["Author"], bool(row["Read"]))
                    result.append(book)
                elif search_by.lower() == "read" and row["Read"].lower() == search_term:
                    book = Book(row["Title"], row["Author"], bool(row["Read"]))
                    result.append(book)

        if not result:
            print("No books found.")

        return result
