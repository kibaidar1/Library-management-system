from library_manager import LibraryManager

library_manager = LibraryManager()


class Menu:

    ANSI_ERROR = "\033[31m Ошибка: {} \033[0m".format
    ANSI_ACCESS = "\033[32m {} \033[0m".format
    ANSI_WRONG = "\033[33m {} \033[0m".format

    def add_book_menu(self):
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = (input("Введите год издания: "))

        try:
            new_book = library_manager.add_book(title, author, int(year))
            print(self.ANSI_ACCESS(f'Книга: {new_book}, успешно добавлена!'))
        except ValueError as e:
            print(self.ANSI_ERROR(str(e)))

    def delite_book_menu(self):
        book_id = input("Введите ID (положительное число) книги, которую хотите удалить: ")

        if library_manager.delete_book(int(book_id)):
            print(self.ANSI_ACCESS('Книга удалена'))
        else:
            print(self.ANSI_WRONG('Книга с таким ID не найдена'))

    def find_bool_menu(self):
        query = input("Поиск: ")
        books = library_manager.find_books(query)
        if books:
            for book in books:
                print(self.ANSI_ACCESS(book))
        else:
            print(self.ANSI_ACCESS('Книги не найдены'))

    def get_all_books_menu(self):
        books = library_manager.get_books()
        if books:
            for book in library_manager.get_books():
                print(self.ANSI_ACCESS(book))
        else:
            print(self.ANSI_WRONG('Библиотека пуста'))

    def change_book_status_menu(self):
        book_id = (input("Введите ID книги: "))
        if book_id.isdigit():
            status = input("Введите новый статус ('в наличии' или 'на руках'): ")
            if library_manager.change_book_status(int(book_id), status):
                print('Статус книги изменен')
            else:
                print('Книга с таким ID не найдена')

        else:
            print("ID должно быть числом")


