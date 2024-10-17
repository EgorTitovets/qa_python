## Описание проекта
Этот проект содержит набор Unit Tests для класса BooksCollector, который управляет коллекцией книг.
Класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector

Частично покрыли тестами class BooksCollector

Реализованные тесты:
1. test_add_new_book_duplicate_books_does_not_added: Проверяет, что дубликаты книг не добавляются.
2. test_set_book_genre_valid_genre_assigned_genre: Проверяет, что к книге корректно присваивается жанр.
3. test_get_book_genre_existing_book_genre_returns: Проверяет, что возвращается корректный жанр для книги.
4. test_get_books_with_specific_genre_existing_genre_books_return: Проверяет, что можно получить книги по заданному жанру.
5. test_get_books_genre_correct_dictionary_returns: Проверяет, что получаем словарь с книгами (books_genre).
6. test_get_books_for_children_no_age_rating_books_without_age_rating_return: Проверяется, что можно получить книги, подходящие для детей.
7. test_add_book_in_favorites_add_one_book_book_added_in_favorites: Проверяет, что книга успешно добавляется в избранное.
8. test_delete_book_from_favorites_remove_real_book_book_removed: Проверяет удаление существующей книги из избранного.
9. test_get_list_of_favorites_books_with_real_books_list_favorites_returns: Проверяется, что получаем список Избранных книг.
