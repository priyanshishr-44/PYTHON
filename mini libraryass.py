# mini_library.py
# Mini Project – Mini Library System
# Course: Foundations of Programming using Python (ETCCFP103)
# Name: Priyanshi Sharma
# Section: BSc Computer Science(A)

# --------------------------------------------------------------
# Book Class Definition
# --------------------------------------------------------------

class Book:
    def _init_(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display_details(self):
        print(f"{self.title:<25} {self.author:<20} {self.isbn:<15} {self.status:<10}")


# --------------------------------------------------------------
# Library Utility Functions
# --------------------------------------------------------------

books = []     # list to store Book objects


# Add Book
def add_book():
    print("\n--- Add New Book ---")
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")

    # prevent duplicate ISBN
    for b in books:
        if b.isbn == isbn:
            print("Book with this ISBN already exists!")
            return

    new_book = Book(title, author, isbn)
    books.append(new_book)
    print("Book added successfully.\n")


# Search Book by title or ISBN
def search_book():
    print("\n--- Search Book ---")
    key = input("Enter Title or ISBN: ")

    found = False
    for b in books:
        if b.title.lower() == key.lower() or b.isbn == key:
            print("\nBook Found:")
            print(f"{'Title':<25} {'Author':<20} {'ISBN':<15} Status")
            print("-" * 70)
            b.display_details()
            found = True
            break

    if not found:
        print("No matching book found.\n")


# Remove Book using ISBN
def remove_book():
    print("\n--- Remove Book ---")
    isbn = input("Enter ISBN to remove: ")

    for b in books:
        if b.isbn == isbn:
            books.remove(b)
            print("Book removed successfully.\n")
            return

    print("Book not found!\n")


# Save books to text file
def save_to_file():
    print("\nSaving records to library.txt ...")
    try:
        with open("library.txt", "w") as f:
            for b in books:
                line = f"{b.title},{b.author},{b.isbn},{b.status}\n"
                f.write(line)
        print("Records saved successfully.\n")
    except Exception as e:
        print("Error while saving file:", e)


# Load books from text file
def load_from_file():
    print("\nLoading records from library.txt ...")
    try:
        with open("library.txt", "r") as f:
            books.clear()
            for line in f:
                data = line.strip().split(",")
                if len(data) == 4:
                    t, a, i, s = data
                    books.append(Book(t, a, i, s))
        print("Records loaded successfully.\n")
    except FileNotFoundError:
        print("library.txt not found.\n")
    except Exception as e:
        print("Error while loading file:", e)


# Display All Books
def display_books():
    if not books:
        print("\nNo books to display.\n")
        return

    print("\n--- All Books ---")
    print(f"{'Title':<25} {'Author':<20} {'ISBN':<15} Status")
    print("-" * 70)

    for b in books:
        b.display_details()

    print()


# Optional: Issue / Return Book
def issue_book():
    print("\n--- Issue Book ---")
    isbn = input("Enter ISBN: ")

    for b in books:
        if b.isbn == isbn:
            if b.status == "Issued":
                print("Book already issued.\n")
            else:
                b.status = "Issued"
                print("Book issued successfully.\n")
            return
    print("Book not found!\n")


def return_book():
    print("\n--- Return Book ---")
    isbn = input("Enter ISBN: ")

    for b in books:
        if b.isbn == isbn:
            if b.status == "Available":
                print("Book is already available.\n")
            else:
                b.status = "Available"
                print("Book returned successfully.\n")
            return
    print("Book not found!\n")


# --------------------------------------------------------------
# Menu Driven Program
# --------------------------------------------------------------

def main():
    while True:
        print("\n========== Mini Library System ==========")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Remove Book")
        print("4. Display All Books")
        print("5. Save Records")
        print("6. Load Records")
        print("7. Issue Book (Optional)")
        print("8. Return Book (Optional)")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            load_from_file()
        elif choice == "7":
            issue_book()
        elif choice == "8":
            return_book()
        elif choice == "9":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.\n")


# Run program
if __name__ == "_main_":
    main()