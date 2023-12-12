from classLibrary.Lend_Out import Lend_Out
from classLibrary.Book import Book
from classLibrary.User import User
from peewee import *
import datetime

def GetAllLend_Out():
    Lend_Outs = Lend_Out.select().dicts()
    returnLend_Outs = []
    for book in Lend_Outs:
        returnLend_Outs.append(Lend_Out(id = Lend_Out["id"],user = Lend_Out["user"],book = Lend_Out["book"]))
    return returnLend_Outs
def GetBookById(Id:int):
    book = Lend_Out.select().where(Lend_Out.id == Id).get()
    return book

def Setlend_Out():
    date = datetime.datetime.now().strftime("%Y-%m-%d")

