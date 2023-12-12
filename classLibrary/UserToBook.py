from classLibrary.BaseModel import BaseModel
from classLibrary.Book import Book
from classLibrary.User import User
from peewee import *

class UserToBook(BaseModel):
    id = PrimaryKeyField(column_name="id", unique=True)
    user = ForeignKeyField(User,related_name="book_id_user_to_book",to_field="id")
    book = ForeignKeyField(Book,related_name="book_id_user_to_book",to_field="id")
    date = DateField(column_name="date_to_give")
    class Meta:
        table_name="user_to_book"