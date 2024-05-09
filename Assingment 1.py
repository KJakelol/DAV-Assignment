import logging

# Configure logging
logging.basicConfig(filename='../book_management.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Book:
    def __init__(self, title, isbn, publisher, language, num_copies, availability, author=None, genre=None):
        self.title = title
        self.isbn = isbn
        self.publisher = publisher
        self.language = language
        self.num_copies = num_copies
        self.availability = availability
        self.author = author  # Additional feature: Capability to store additional book data types
        self.genre = genre    # Additional feature: Capability to store additional book data types

    def __str__(self):
        return f"Title: {self.title}, ISBN: {self.isbn}, Publisher: {self.publisher}, Language: {self.language}, Number of Copies: {self.num_copies}, Availability: {self.availability}, Author: {self.author}, Genre: {self.genre}"

class BookManagementSystem:
    def __init__(self):
        self.books = []
        self.logged_in = False

    def display_all_books(self):
        for book in self.books:
            print(book)

    def add_book(self, new_book):
        if self.logged_in:
            self.books.append(new_book)
            logging.info(f"Book added: {new_book.title}")  # Additional feature: Logging functionality to track actions performed on book records
            print("Book record added successfully!")
        else:
            print("Access denied. Please log in to add books.")
            self.prompt_login()

    def update_book(self, isbn, updated_book):
        if self.logged_in:
            for i, book in enumerate(self.books):
                if book.isbn == isbn:
                    self.books[i] = updated_book
                    logging.info(f"Book updated: {updated_book.title}")  # Additional feature: Logging functionality to track actions performed on book records
                    print("Book record updated successfully!")
                    return
            print("Book with the provided ISBN not found.")
        else:
            print("Access denied. Please log in to update books.")
            self.prompt_login()

    def delete_book(self, isbn):
        if self.logged_in:
            for i, book in enumerate(self.books):
                if book.isbn == isbn:
                    del self.books[i]
                    logging.info(f"Book deleted: {book.title}")  # Additional feature: Logging functionality to track actions performed on book records
                    print("Book record deleted successfully!")
                    return
            print("Book with the provided ISBN not found.")
        else:
            print("Access denied. Please log in to delete books.")
            self.prompt_login()

    def sort_books_by_publisher(self):
        if self.logged_in:
            self.books.sort(key=lambda x: x.publisher)
            logging.info("Books sorted by publisher")  # Additional feature: Logging functionality to track actions performed on book records
        else:
            print("Access denied. Please log in to sort books.")
            self.prompt_login()

    def sort_books_by_num_copies(self):
        if self.logged_in:
            self.books.sort(key=lambda x: x.num_copies, reverse=True)
            logging.info("Books sorted by number of copies")  # Additional feature: Logging functionality to track actions performed on book records
        else:
            print("Access denied. Please log in to sort books.")
            self.prompt_login()

    def login(self, username, password):
        # Simple authentication, hardcoded username and password for demonstration purposes
        if username == "admin" and password == "admin":
            self.logged_in = True
            logging.info("Admin logged in")  # Additional feature: Logging functionality to track actions performed on book records
            print("Login successful!")
        else:
            print("Invalid username or password.")

    def prompt_login(self):
        choice = input("Would you like to log in now? (yes/no): ")
        if choice.lower() == "yes":
            self.login_user()
        elif choice.lower() == "no":
            print("Operation canceled.")
        else:
            print("Invalid choice.")

    def login_user(self):
        print("\nLogin:")
        if not self.logged_in:
            username = input("Enter username: ")
            password = input("Enter password: ")
            self.login(username, password)
        else:
            print("You are already logged in.")

def display_menu():
    print("\nMenu:")
    print("1. Display all book records")
    print("2. Add new book record")
    print("3. Update a book record")
    print("4. Delete a book record")
    print("5. Sort books by Publisher in ascending order")
    print("6. Sort books by Number of Copies in descending order")
    print("7. Login")
    print("8. Exit")

def display_all_books(book_system):
    print("\nDisplaying all book records:")
    book_system.display_all_books()

def add_new_book(book_system):
    print("\nAdding a new book record:")
    if book_system.logged_in:
        title = input("Enter title: ")
        isbn = int(input("Enter ISBN: "))
        publisher = input("Enter publisher: ")
        language = input("Enter language: ")
        num_copies = int(input("Enter number of copies: "))
        availability = input("Enter availability (True/False): ").lower() == "true"
        author = input("Enter author: ")
        genre = input("Enter genre: ")
        new_book = Book(title, isbn, publisher, language, num_copies, availability, author, genre)
        book_system.add_book(new_book)
    else:
        print("Access denied. Please log in to add books.")

def update_book_record(book_system):
    print("\nUpdating a book record:")
    if book_system.logged_in:
        isbn = int(input("Enter ISBN of the book to update: "))
        # Get updated book information
        title = input("Enter updated title: ")
        publisher = input("Enter updated publisher: ")
        language = input("Enter updated language: ")
        num_copies = int(input("Enter updated number of copies: "))
        availability = input("Enter updated availability (True/False): ").lower() == "true"
        author = input("Enter updated author: ")
        genre = input("Enter updated genre: ")
        updated_book = Book(title, isbn, publisher, language, num_copies, availability, author, genre)
        book_system.update_book(isbn, updated_book)
    else:
        print("Access denied. Please log in to update books.")

def delete_book_record(book_system):
    print("\nDeleting a book record:")
    if book_system.logged_in:
        isbn = int(input("Enter ISBN of the book to delete: "))
        book_system.delete_book(isbn)
    else:
        print("Access denied. Please log in to delete books.")

def login_user(book_system):
    print("\nLogin:")
    if not book_system.logged_in:
        username = input("Enter username: ")
        password = input("Enter password: ")
        book_system.login(username, password)
    else:
        print("You are already logged in.")

def main():
    book_system = BookManagementSystem()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_all_books(book_system)
        elif choice == "2":
            add_new_book(book_system)
        elif choice == "3":
            update_book_record(book_system)
        elif choice == "4":
            delete_book_record(book_system)
        elif choice == "5":
            book_system.sort_books_by_publisher()
        elif choice == "6":
            book_system.sort_books_by_num_copies()
        elif choice == "7":
            login_user(book_system)
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()


