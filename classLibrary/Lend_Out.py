from classLibrary.BaseModel import BaseModel
from peewee import *

class Lend_Out(BaseModel):
    id = PrimaryKeyField(column_name="id", unique=True)
    user = CharField(column_name="user",max_length=120)
    book = CharField(column_name="book",max_length=100)
    date = DateField(column_name="date")
    class Meta:
        table_name = "lend_Out"