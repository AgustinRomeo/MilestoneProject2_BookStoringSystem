from utils.database import Book, BookStore

# Create an instance of the BookStore
bookstore = BookStore()

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 's' to save the list to a csv file
- 'u' to upload the las csv file saved
- 'c' to check if you have rad a book
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
        bookstore.mark_book_as_read(title)

    elif user_choice == 'd':
        # Prompt the user to delete a book
        title = input("Enter the title of the book to delete: ")
        bookstore.delete_book(title)

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
