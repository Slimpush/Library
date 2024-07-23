import unittest
from models import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """
        Очищаем список книг перед тестом.
        """
        self.library = Library('test_books.json')
        self.library.books = []

    def test_add_book(self):
        """
        Проверяем, что после добавления количество книг увеличивается на 1
        и что добавленная книга имеет правильные атрибуты.
        """
        self.library.add_book('Test Book', 'Test Author', 2023)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, 'Test Book')

    def test_remove_book(self):
        """
        Проверяем, что книга корректно удаляется по ее ID
        и что после удаления количество книг уменьшается на 1.
        """
        self.library.add_book('Test Book', 'Test Author', 2023)
        book_id = self.library.books[0].id
        self.assertTrue(self.library.remove_book(book_id))
        self.assertEqual(len(self.library.books), 0)

    def test_find_books(self):
        """
        Проверяем, что поиск по названию возвращает корректные результаты.
        """
        self.library.add_book('Test Book', 'Test Author', 2023)
        results = self.library.find_books(title='Test Book')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, 'Test Book')

    def test_change_status(self):
        """
        Проверяем, что статус книги корректно меняется по ее ID.
        """
        self.library.add_book('Test Book', 'Test Author', 2023)
        book_id = self.library.books[0].id
        self.assertTrue(self.library.change_status(book_id, 'выдана'))
        self.assertEqual(self.library.books[0].status, 'выдана')


if __name__ == '__main__':
    unittest.main()
