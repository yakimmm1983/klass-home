from classLibrary.Book import Book

def CreateBook():
    CreateBook = Book(name="Вишневый сад", author="Чехов А.П", description="События пьесы происходят в конце XIX века в России, в имении Раневских.")
    CreateBook.save()
    CreateBook1 = Book(name="Поэма", author="Пушкин А.С", description="гражданская, повествующая о Полтавской битве 1709 года, победе Петра и измене Мазепы")
    CreateBook1.save()
    CreateBook2 = Book(name="Бородино", author="Лермонтов М.Ю", description="войне с Наполеоном, в которой решающим стало сражение под селом Бородино")
    CreateBook2.save()


if __name__=="__main__":
    CreateBook()