from classLibrary.BaseModel import BaseModel
from peewee import *

class Book(BaseModel):
    id = PrimaryKeyField(column_name="id", unique=True)
    name = CharField(column_name="name",max_length=120)
    author = CharField(column_name="author",max_length=100)
    description = CharField(column_name="description",max_length=500)
    class Meta:
        table_name = "book"