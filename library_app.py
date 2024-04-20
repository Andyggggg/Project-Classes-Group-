import os

class libraryApp:
    def __init__(self, isbn, title, author, genre):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = False
#insert load_books below
    def load_books(book_list, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    isbn, title, author, genre = line.strip().split(',')
                    book_list.append(libraryApp(isbn, title, author, genre))
            return len(book_list)
        else:
            print("File not found.")
            return 0

#insert print_menu below
    def print_menu(heading, options):
        print(heading)
        for key, value in options.items():
            print(f"{key}. {value}")
        choice = input("Enter your choice: ")
        while choice not in options:
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")
        return choice

#insert search_books below
    def search_books(book_list, search_string):
        search_results = []
        for book in book_list:
            if search_string.lower() in (book.isbn.lower(), book.title.lower(), book.author.lower(), book.genre.lower()):
                search_results.append(book)
        return search_results

#insert borrow_book below
    def borrow_book(book_list):
        isbn = input("Enter the ISBN of the book you want to borrow: ")
        index = libraryApp.find_book_by_isbn(book_list, isbn)
        if index != -1:
            if book_list[index].borrowed == False:
                book_list[index].borrow_it()
            else:
                print("This book is already borrowed.")
        else:
            print("Book not found.")


#insert below
    def find_book_by_isbn(book_list, isbn):
        for index in range(len(book_list)):
            book = book_list[index]
            if book.isbn == isbn:
                return index
        return -1


#insert return_book below
    def return_book(book_list):
        isbn = input("Enter the ISBN of the book you want to return: ")
        index = libraryApp.find_book_by_isbn(book_list, isbn)
        if index != -1:
            if book_list[index].borrowed:
                book_list[index].return_it()
            else:
                print("This book is not currently borrowed.")
        else:
            print("Book not found.")

#insert add_book below
    def add_book(book_list):
        isbn = input("Enter ISBN: ")
        title = input("Enter title: ")
        author = input("Enter author: ")
        genre = input("Enter genre: ")
    #insert genre based on part 1
        genres = ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery", "Thriller", "Horror"]
        if genre not in genres:
            print("Invalid genre.")
            return
        book_list.append(libraryApp(isbn, title, author, genre))
        print("Book added successfully.")

#insert remove_book below
    def remove_book(book_list):
        isbn = input("Enter the ISBN of the book you want to remove: ")
        index = libraryApp.find_book_by_isbn(book_list, isbn)
        if index != -1:
            del book_list[index]
            print("Book removed successfully.")
        else:
            print("Book not found.")

#insert print_book below
    def print_books(book_list):
        print("\nBook Information:")
        for book in book_list:
            print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}")

#insert save_book below
    def save_books(book_list, file_path):
        try:
            with open(file_path, 'w') as file:
                for book in book_list:
                    file.write(f"{book.isbn},{book.title},{book.author},{book.genre}\n")
            return len(book_list)
        except:
            print("Error occurred while saving books.")
            return 0

#insert below
    def main():
        book_list = []
        file_path = input("Enter the path to the CSV data file: ")
        num_books = libraryApp.load_books(book_list, file_path)
        print(f"{num_books} books loaded successfully.")

        menu_heading = "Library Management System Menu"
        menu_options = {
            '1': 'Search Books',
            '2': 'Borrow Book',
            '3': 'Return Book',
            '4': 'Add Book',
            '5': 'Remove Book',
            '6': 'Print All Books',
            'Q': 'Quit'
        }

        while True:
            choice = libraryApp.print_menu(menu_heading, menu_options)
            if choice == '1':
                search_string = input("Enter search string: ")
                search_result = libraryApp.search_books(book_list, search_string)
                libraryApp.print_books(search_result)
            elif choice == '2':
                libraryApp.borrow_book(book_list)
            elif choice == '3':
                libraryApp.return_book(book_list)
            elif choice == '4':
                libraryApp.add_book(book_list)
            elif choice == '5':
                libraryApp.remove_book(book_list)
            elif choice == '6':
                libraryApp.print_books(book_list)
            elif choice.upper() == 'Q':
                libraryApp.save_books(book_list, file_path)
                print("Exiting the program.")
                break
