from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass
class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def print_info(self):
        print(f"Book: {self.title} by {self.author}, {self.year}")

book = Book("The Great Gatsby", "F Scott FitzGerald", "1700")
book.print_info()
