from abc import ABC, abstractmethod

# Abstract Base Class
class LibraryItem(ABC):
    total_items = 0  # Static/Class counter

    def __init__(self, title, year):
        self.title = title
        self.year = year
        LibraryItem.total_items += 1

    @abstractmethod
    def displayInfo(self):
        pass


# Subclass: Book
class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def displayInfo(self):
        print(f"[Book] Title: {self.title}, Year: {self.year}, Author: {self.author}")


# Subclass: DVD
class DVD(LibraryItem):
    def __init__(self, title, year, duration, genre):
        super().__init__(title, year)
        self.duration = duration
        self.genre = genre

    def displayInfo(self):
        print(f"[DVD] Title: {self.title}, Year: {self.year}, Duration: {self.duration} mins, Genre: {self.genre}")


# Polymorphism demonstration
def show_library(items):
    for item in items:
        item.displayInfo()   # Polymorphic call


# Main Execution
if __name__ == "__main__":
    item1 = Book("The Alchemist", 1988, "Paulo Coelho")
    item2 = DVD("Inception", 2010, 148, "Sci-Fi")
    item3 = Book("Clean Code", 2008, "Robert C. Martin")

    library_items = [item1, item2, item3]

    print("Library Items:\n")
    show_library(library_items)

    print("\nTotal Library Items:", LibraryItem.total_items)