class Book:
    genres = {
        0: "Romance",
        1: "Mystery",
        2: "Science Fiction",
        3: "Thriller",
        4: "Young Adult",
        5: "Children’s Fiction",
        6: "Self-help",
        7: "Fantasy",
        8: "Historical Fiction",
        9: "Poetry"
    }

    def __init__(self, isbn, title, author, genre, available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = available

#insert get_isbn below
    def get_isbn(self):
        return self.__isbn
#insert get_title below
    def get_title(self):
        return self.__title
#insert get_author below
    def get_author(self):
        return self.__author
#insert get_genre below
    def get_genre(self):
        return self.__genre
#insert get_genre_name below
    def get_genre_name(self):
        return Book.genres.get(self.__genre, "Unknown")
#insert get_availability below
    def get_availability(self):
        if self.__available:
            return "Available"
        else:
            return "Borrowed"
#insert set_isbn below
    def set_isbn(self, isbn):
        self.__isbn = isbn
#insert set_title below
    def set_title(self, title):
        self.__title = title
#insert set_author below
    def set_author(self, author):
        self.__author = author
#insert set_genre below
    def set_genre(self, genre):
        self.__genre = genre
#insert borrow_it below
    def borrow_it(self):
        self.__available = False
#insert return_it below
    def return_it(self):
        self.__available = True
#insert set_below
    def __str__(self):
        return f"{self.__isbn} {self.__title:>20} {self.__author:>25} {self.get_genre_name():>30} {self.get_availability():>15}"