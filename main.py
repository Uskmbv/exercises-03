#1
def count_vowels(text):
    if not isinstance(text, str):
        return 42
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count

input_str = "Hello, World!"
result = count_vowels(input_str)
print("Number of vowels:", result)


#2
def hamming_distance(text1, text2):
    if len(text1) != len(text2):
        return 0
    distance = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance += 1
    return distance

input_str1 = "hello"
input_str2 = "hullo"
result = hamming_distance(input_str1, input_str2)
print("Hamming distance:", result)

#3

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

    @abstractmethod
    def __str__(self):
        pass


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Doors: {self.doors}"


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Passengers: {self.passengers}"


car_obj = Car("red", "petrol", 4)
bus_obj = Bus("blue", "diesel", 30)

print(car_obj)
print(bus_obj)

#4

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"{self.name}, {self.author}"


my_book = Book("The Da Vinci Code", "Dan Brown")
print(my_book)

#5

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"{self.name}, {self.author}"

class BookShelf:
    def __init__(self):
        self.books = []

    def add_book_list(self, books):
        for book in books:
            if isinstance(book, Book):
                self.books.append(book)

    def books_by_author(self, author):
        books_by_author = []
        for book in self.books:
            if book.author == author:
                books_by_author.append(book.name)
        return books_by_author

    def get_books(self):
        book_names = []
        for book in self.books:
            book_names.append(book.name)
        return book_names

    def clear_shelf(self):
        self.books = []

book1 = Book("The Da Vinci Code", "Dan Brown")
book2 = Book("Angels and Demons", "Dan Brown")
book3 = "Not a Book Object"

shelf = BookShelf()
shelf.add_book_list([book1, book2, book3])

print(shelf.get_books())
print(shelf.books_by_author("Dan Brown"))

shelf.clear_shelf()
print(shelf.get_books())




