from utils.database import Book, BookStore

# Create an instance of the BookStore
bookstore = BookStore()

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'f' to find a book by author or title
- 's' to save the list to a csv file
- 'u' to upload the last csv file saved
- 'c' to check if you have read a book
- 'q' to quit

Your choice:"""


while True:
    user_choice = input(USER_CHOICE)

    if user_choice == 'a':
        # Prompt the user to add a new book
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        new_book = Book(title, author)
        bookstore.add_book(new_book)

    elif user_choice == 'l':
        # List all the books
        bookstore.list_books()

    elif user_choice == 'r':
        # Prompt the user to mark a book as read
        title = input("Enter the title of the book to mark as read: ")
        if not title:
            print("Invalid title. Please enter a valid title.")
            continue
        if not bookstore.has_book(title):
            print("The book with the given title does not exist.")
            continue
        bookstore.mark_book_as_read(title)

    elif user_choice == 'd':
        # Prompt the user to delete a book
        title = input("Enter the title of the book to delete: ")
        if not title:
            print("Invalid title. Please enter a valid title.")
            continue
        if not bookstore.has_book(title):
            print("The book with the given title does not exist.")
            continue
        bookstore.delete_book(title)

    elif user_choice == 'f':
        # Prompt the user to search for a book
        search_by = input("Search by 'title', 'author', or 'read': ")
        search_term = input("Enter what you are looking for: ")
        search_results = bookstore.search_books(search_by, search_term)
        if search_results:
            print("Search results:")
            for book in search_results:
                print(f"Title: {book.title}, Author: {book.author}, Read: {book.read}")
        else:
            print("No books found.")

    elif user_choice == 'c':
        # Prompt the user to check if read
        title = input("Enter the title of the book: ")
        if bookstore.has_read_book(title):
            print("You have read this book.")
        else:
            print("You have not read this book.")

    elif user_choice == 's':
        bookstore.save_books_to_csv("books.csv")

    elif user_choice == 'u':
        bookstore.load_books_from_csv("books.csv")

    elif user_choice == 'q':
        break

    else:
        print("Invalid choice. Please try again.")
