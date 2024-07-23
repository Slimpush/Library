import json
import os
import uuid
from typing import List, Optional


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.id = str(uuid.uuid4())
        self.author = author
        self.title = title
        self.year = year
        self.status = 'в наличии'

    def to_dict(self) -> dict:
        # Преобразование объекта Book в словарь
        return {
            'id': self.id,
            'author': self.author,
            'title': self.title,
            'year': self.year,
            'status': self.status,
        }

    @staticmethod
    def from_dict(data: dict) -> 'Book':
        # Создание объекта Book
        book = Book(**{key: data[key] for key in ['title', 'author', 'year']})
        book.id = data['id']
        book.status = data['status']
        return book


class Library:
    def __init__(self, books_file: str):
        self.books_file = books_file
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        # Загрузка книг из файла, возвращает список книг
        if not os.path.exists(self.books_file):
            return []
        with open(self.books_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Book.from_dict(book_data) for book_data in data]

    def save_books(self):
        # Сохранение книги в файл
        with open(self.books_file, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books],
                      file,
                      ensure_ascii=False,
                      indent=4,
                      )

    def add_book(self, title: str, author: str, year: int):
        # Добавление книги в библиотеку
        book = Book(title, author, year)
        self.books.append(book)
        self.save_books()
        return book.id

    def remove_book(self, book_id: str) -> bool:
        # Удаление книги по ID
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return True
        return False

    def find_books(self, title: Optional[str] = None,
                   author: Optional[str] = None,
                   year: Optional[int] = None) -> List[Book]:
        # Поиск книг по названию, автору или году выпуска
        results = self.books
        if title:
            results = [book for book in results
                       if title.lower() in book.title.lower()]
        if author:
            results = [book for book in results
                       if author.lower() in book.author.lower()]
        if year:
            results = [book for book in results if book.year == year]
        return results

    def change_status(self, book_id: str, new_status: str) -> bool:
        # Изменение статуса книги
        if new_status not in ["в наличии", "выдана"]:
            print("Доступные статусы 'в наличии' или 'выдана'.")
            return False
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books()
                return True
        return False

    def display_books(self):
        # Отображение всех книг библиотеки
        for book in self.books:
            print(f"id: {book.id}, Название: {book.title}, "
                  f"Автор: {book.author}, Год издания: {book.year}, "
                  f"Статус: {book.status}")
