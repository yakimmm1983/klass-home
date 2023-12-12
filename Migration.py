from classLibrary.Lend_Out import Lend_Out
from classLibrary.User import User
from classLibrary.Book import Book

if __name__ == "__main__":
    status = "ok"
    try:
        Lend_Out.drop_table()
        Book.drop_table()
        User.drop_table()

    except Exception as e:
        status = f"Drop error {e}"
    try:
        User.create_table()
        Book.create_table()
        Lend_Out.create_table()

    except Exception as e:
        status = f"Create error {e}"
    print(f"Migration {status}")