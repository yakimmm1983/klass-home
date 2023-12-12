from classLibrary import Book,User,Lend_Out

from Dto import BookDto,Lend_OutDto,UserDto

def regUser():
    name = input("имя")
    phone = input("номер телефона")
    UserDto.RegistrationUser(phone,name)
def SeeAllBook()->str:
    _book = ""
    books = BookDto.GetAllBook()
    for book in books:
        _book+=f"{book.id} {book.description} {book.author} {book.name}\n"
    return book

def IsuueBook():
    userPhone = input("номер телефона")
    try:
        user = UserDto.ChangeUserByPhone(userPhone)
    except Exception:
        user = regUser()
    try:
        bookId = int(input("Введите номер книги"))
        book = BookDto.GetBookById(bookId)
        issueBook = Lend_OutDto.IssuedBook(user,book)
    except Exception:
        print("Не удалось получить книгу")

_mainMenu = ""
while True:
    _mainMenu = "1-регистрация, 2-посмотреть книги, 3-выдать книгу"
    choise = input(_mainMenu)
    if choise =="1":
        regUser()
    elif choise =="2":
        SeeAllBook()
    elif choise =="3":
        IsuueBook()
    else:
        continue
# registrationUser = UserDto.RegistrationUser()
#
# lend_OutUser = CreateBook()
