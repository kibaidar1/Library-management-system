from library_manager import LibraryManager
from menu import Menu

library_manager = LibraryManager()
menu = Menu()

ANSI_ERROR = "\033[31m Ошибка: {} \033[0m".format
ANSI_ACCESS = "\033[32m {} \033[0m".format


def main():
    while True:
        print("Меню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("0. Выйти")

        choice = input("Выберите пункт: ")

        if choice == "1":
            menu.add_book_menu()

        elif choice == "2":
            menu.delite_book_menu()

        elif choice == "3":
            menu.find_bool_menu()

        elif choice == "4":
            menu.get_all_books_menu()

        elif choice == "5":
            menu.change_book_status_menu()

        elif choice == "0":
            print("Выход из приложения")
            break


if __name__ == "__main__":
    main()

