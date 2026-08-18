# Book Class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False


# Patron Class
class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []


# Library Class
class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add Book
    def add_book(self, book):
        self.books[book.book_id] = book

    # Register Patron
    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron

    # Remove Book
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book removed successfully.")
        else:
            print("Book not found.")

    # Borrow Book
    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print("Book is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book)
            print(f"{patron.name} borrowed '{book.title}'.")

    # Return Book
    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        patron = self.patrons[patron_id]

        for book in patron.borrowed_books:
            if book.book_id == book_id:
                book.is_borrowed = False
                patron.borrowed_books.remove(book)
                print(f"{patron.name} returned '{book.title}'.")
                return

        print("This patron did not borrow that book.")

    # Display Books
    def display_books(self):
        print("\nLibrary Books:")
        if not self.books:
            print("No books available.")
            return

        for book in self.books.values():
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.book_id} - {book.title} by {book.author} ({status})")

    # Display Patrons
    def display_patrons(self):
        print("\nRegistered Patrons:")
        if not self.patrons:
            print("No patrons registered.")
            return

        for patron in self.patrons.values():
            print(f"{patron.patron_id} - {patron.name}")


# ---------------- Main Program ----------------

library = Library()

# Register Patrons
num_patron = int(input("How many patrons do you want to register? "))
for i in range(num_patron):
    print(f"\nEnter details for Patron {i+1}")
    pid = int(input("Patron ID: "))
    name = input("Patron Name: ")
    library.register_patron(Patron(pid, name))

# Add Books
n = int(input("\nHow many books do you want to add? "))
for i in range(n):
    print(f"\nEnter details for Book {i+1}")
    book_id = int(input("Book ID: "))
    title = input("Book Title: ")
    author = input("Author: ")
    library.add_book(Book(book_id, title, author))

# Menu
while True:
    print("\n===== Library Management System =====")
    print("1. Display Books")
    print("2. Display Patrons")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Remove Book")
    print("6. Add More Books")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        library.display_patrons()

    elif choice == "3":
        count = int(input("How many books do you want to borrow? "))
        patron_id = int(input("Enter Patron ID: "))
        for _ in range(count):
            book_id = int(input("Enter Book ID: "))
            library.borrow_book(patron_id, book_id)

    elif choice == "4":
        count = int(input("How many books do you want to return? "))
        patron_id = int(input("Enter Patron ID: "))
        for _ in range(count):
            book_id = int(input("Enter Book ID: "))
            library.return_book(patron_id, book_id)

    elif choice == "5":
        count = int(input("How many books do you want to remove? "))
        for _ in range(count):
            book_id = int(input("Enter Book ID to remove: "))
            library.remove_book(book_id)

    elif choice == "6":
        count = int(input("How many books do you want to add? "))
        for _ in range(count):
            book_id = int(input("Book ID: "))
            title = input("Book Title: ")
            author = input("Author: ")
            library.add_book(Book(book_id, title, author))

    elif choice == "7":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
