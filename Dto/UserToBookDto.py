from classLibrary.UserToBook import UserToBook
from classLibrary.Book import Book
from classLibrary.User import User
from peewee import *
import datetime

def GetAllUserToBook():
    books = UserToBook.select().dicts()
    returnBooks = []
    for book in books:
        returnBooks.append(UserToBook(id = UserToBook["id"],name = UserToBook["name"],author = UserToBook["author"],description = Book["description"]))
    return GetAllUserToBook()
def GetUserToBookById(Id:int):
    book = UserToBook().select().where(UserToBook.id == Id).get()
    return GetUserToBookById