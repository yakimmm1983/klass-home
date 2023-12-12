from classLibrary.Book import Book
from peewee import *

def GetAllBook() -> list:
    books = Book.select().dicts()
    rezBooks = []
    for book in books:
        rezBooks.append(Book(id = Book["id"],name = Book["name"],author = Book["author"],description = Book["description"]))
    return rezBooks
def GetBookById(Id:int)->Book:
    book = Book.select().where(Book.id == Id).get()
    return book