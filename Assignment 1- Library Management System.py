class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book.title)

    def return_book(self, book):
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book.title)

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron, book):
        if book.is_borrowed == False:
            book.borrow()
            patron.borrow_book(book)
            print("Book borrowed successfully!")
        else:
            print("Book is already borrowed.")

    def return_book(self, patron, book):
        if book.is_borrowed == True:
            book.return_book()
            patron.return_book(book)
            print("Book returned successfully!")
        else:
            print("Book is already available.")


library = Library()
print("--------------------------------------------------")
print("        LIBRARY MANAGEMENT SYSTEM")
print("--------------------------------------------------")

# Adding Books
number_of_books = int(input("Enter number of books: "))
for i in range(number_of_books):
    print("\nEnter Book Details")
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    book = Book(title, author, isbn)
    library.add_book(book)
print("--------------------------------------------------")

# Registering Patrons
number_of_patrons = int(input("Enter number of patrons: "))
for i in range(number_of_patrons):
    print("\nEnter Patron Details")
    name = input("Enter patron name: ")
    patron_id = input("Enter patron ID: ")
    patron = Patron(name, patron_id)
    library.register_patron(patron)
print("--------------------------------------------------")

# Borrow Books
number_of_borrowing = int(input("How many books are being borrowed? "))
for i in range(number_of_borrowing):
    print("\nBORROW BOOK")
    print("--------------------------------------------------")

    patron_id = input("Enter patron ID: ")
    book_title = input("Enter book title: ")
    selected_patron = None
    selected_book = None

    for patron in library.patrons:
        if patron.patron_id == patron_id:
            selected_patron = patron

    for book in library.books:
        if book.title == book_title:
            selected_book = book

    if selected_patron != None and selected_book != None:
        library.borrow_book(selected_patron, selected_book)
    else:
        print("Patron or book not found.")
print("--------------------------------------------------")

# Return Book
choice = input("Do you want to return a book? (yes/no): ")
if choice == "yes":
    print("\nRETURN BOOK")
    print("--------------------------------------------------")

    patron_id = input("Enter patron ID: ").strip()
    book_title = input("Enter book title: ").strip()
    selected_patron = None
    selected_book = None

    for patron in library.patrons:
        if patron.patron_id == patron_id:
            selected_patron = patron

    for book in library.books:
        if book.title == book_title:
            selected_book = book

    if selected_patron != None and selected_book != None:
        library.return_book(selected_patron, selected_book)
    else:
        print("Patron or book not found.")
print("--------------------------------------------------")

# Display Books
print("BOOK DETAILS")
print("--------------------------------------------------")

for book in library.books:
    print("Title:", book.title)
    print("Author:", book.author)
    print("ISBN:", book.isbn)

    if book.is_borrowed == True:
        print("Status: Borrowed")
    else:
        print("Status: Available")
    print("--------------------------------------------------")

# Display Patrons
print("PATRON DETAILS")
print("--------------------------------------------------")

for patron in library.patrons:
    print("Name:", patron.name)
    print("Patron ID:", patron.patron_id)
    print("Borrowed Books:", patron.borrowed_books)
    print("--------------------------------------------------")