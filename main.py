from models import Library


def main():
    library = Library('books.json')

    while True:
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            book_id = library.add_book(title, author, year)
            print(f"Книга добавлена. ID книги: {book_id}")
        elif choice == '2':
            book_id = input("Введите ID книги для удаления книги: ")
            if library.remove_book(book_id):
                print("Книга удалена.")
            else:
                print("Книга не найдена.")
        elif choice == '3':
            title = input("Введите название книги"
                          "(или нажмите Enter, чтобы пропустить): ")
            author = input("Введите автора книги"
                           "(или нажмите Enter, чтобы пропустить): ")
            year_input = input("Введите год издания книги"
                               "(или нажмите Enter, чтобы пропустить): ")
            year = int(year_input) if year_input else None
            found_books = library.find_books(
                title or None, author or None, year)
            if found_books:
                for book in found_books:
                    print(f"ID: {book.id}, "
                          f"Title: {book.title}, "
                          f"Author: {book.author}, "
                          f"Year: {book.year}, "
                          f"Status: {book.status}")
            else:
                print("Книги не найдены.")
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            book_id = input("Введите ID книги для изменения статуса: ")
            new_status = input(
                "Введите новый статус книги (в наличии/выдана): ")
            if library.change_status(book_id, new_status):
                print("Статус книги изменен.")
            else:
                print("Книга не найдена.")
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
