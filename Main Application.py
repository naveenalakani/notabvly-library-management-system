from models import Book
from utils import create_account, login

def main():
    print("Welcome to the Library Management System!")
    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            if login():
                while True:
                    print("\n1. Add Book\n2. List Books\n3. Borrow Book\n4. Return Book\n5. Logout")
                    user_choice = input("Choose an option: ")

                    if user_choice == '1':
                        title = input("Enter book title: ")
                        author = input("Enter book author: ")
                        book = Book(title, author)
                        book.save()
                        print("Book added successfully!")
                    elif user_choice == '2':
                        books = Book.list_all()
                        for book in books:
                            status = "Available" if book['available'] else "Borrowed"
                            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {status}")
                    elif user_choice == '3':
                        book_id = int(input("Enter book ID to borrow: "))
                        Book.borrow_book(book_id)
                        print("Book borrowed successfully!")
                    elif user_choice == '4':
                        book_id = int(input("Enter book ID to return: "))
                        Book.return_book(book_id)
                        print("Book returned successfully!")
                    elif user_choice == '5':
                        break
                    else:
                        print("Invalid option. Please try again.")
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
