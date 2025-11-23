# SUPER EASY MINI LIBRARY SYSTEM
# Only lists, very simple code, beginner-friendly

library = []   # each book = [title, author, isbn, status]


# -------------------------------
# ADD BOOK (Bonus: No duplicate ISBN)
# -------------------------------
def add_book():
    print("\n--- Add Book ---")
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")

    # Bonus: Check duplicate
    for book in library:
        if book[2] == isbn:
            print("Book with this ISBN already exists!")
            return

    status = "Available"
    library.append([title, author, isbn, status])
    print("Book added successfully!")


# -------------------------------
# SEARCH BOOK
# -------------------------------
def search_book():
    print("\n--- Search Book ---")
    key = input("Enter title or ISBN: ")

    for b in library:
        if key == b[0] or key == b[2]:
            print("Book Found:")
            print("Title:", b[0])
            print("Author:", b[1])
            print("ISBN:", b[2])
            print("Status:", b[3])
            return

    print("Book not found.")


# -------------------------------
# REMOVE BOOK
# -------------------------------
def remove_book():
    print("\n--- Remove Book ---")
    isbn = input("Enter ISBN to remove: ")

    for b in library:
        if isbn == b[2]:
            library.remove(b)
            print("Book removed!")
            return

    print("Book not found.")


# -------------------------------
# DISPLAY ALL BOOKS
# -------------------------------
def display_books():
    print("\n--- List of Books ---")
    if len(library) == 0:
        print("No books available.")
        return

    for b in library:
        print(b[0], "|", b[1], "|", b[2], "|", b[3])


# -------------------------------
# SAVE TO FILE
# -------------------------------
def save_books():
    try:
        file = open("library.txt", "w")
        for b in library:
            file.write(",".join(b) + "\n")
        file.close()
        print("Books saved to library.txt")
    except:
        print("Error saving file!")


# -------------------------------
# LOAD FROM FILE
# -------------------------------
def load_books():
    try:
        file = open("library.txt", "r")
        library.clear()

        for line in file:
            data = line.strip().split(",")
            library.append(data)

        file.close()
        print("Books loaded!")
    except:
        print("File not found!")


# -------------------------------
# BONUS FEATURE: ISSUE BOOK
# -------------------------------
def issue_book():
    print("\n--- Issue Book ---")
    isbn = input("Enter ISBN to issue: ")

    for b in library:
        if isbn == b[2]:
            if b[3] == "Available":
                b[3] = "Issued"
                print("Book issued!")
            else:
                print("Book already issued!")
            return

    print("Book not found.")


# -------------------------------
# BONUS FEATURE: RETURN BOOK
# -------------------------------
def return_book():
    print("\n--- Return Book ---")
    isbn = input("Enter ISBN to return: ")

    for b in library:
        if isbn == b[2]:
            if b[3] == "Issued":
                b[3] = "Available"
                print("Book returned!")
            else:
                print("Book is not issued!")
            return

    print("Book not found.")


# -------------------------------
# MENU
# -------------------------------
while True:
    print("\n===== MINI LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display Books")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Issue Book (Bonus)")
    print("8. Return Book (Bonus)")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        remove_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        save_books()
    elif choice == "6":
        load_books()
    elif choice == "7":
        issue_book()
    elif choice == "8":
        return_book()
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
