import pytest

# from main import BooksCollector


class TestBooksCollector:

    # @pytest.fixture
    # def collector(self):
    #     return BooksCollector()

    def test_add_new_book_duplicate_books_does_not_added(self, collector):
        collector.add_new_book("Один Дома")
        collector.add_new_book("Один Дома")
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize("book_name, genre", [
        ("Один Дома", "Комедии"),
        ("Король Лев", "Мультфильмы"),
        ("Аватар", "Фантастика")
    ])
    def test_set_book_genre_valid_genre_assigned_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    @pytest.mark.parametrize("book_name, genre", [
        ("Один Дома", "Комедии"),
        ("Король Лев", "Мультфильмы"),
        ("Аватар", "Фантастика")
    ])
    def test_get_book_genre_existing_book_genre_returns(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_existing_genre_books_return(self, collector):
        collector.add_new_book("Один Дома")
        collector.set_book_genre("Один Дома", "Комедии")
        collector.add_new_book("Король Лев")
        collector.set_book_genre("Король Лев", "Мультфильмы")
        assert "Король Лев" in collector.get_books_with_specific_genre("Мультфильмы")

    def test_get_books_genre_correct_dictionary_returns(self, collector):
        collector.add_new_book("Один Дома")
        collector.set_book_genre("Один Дома", "Комедии")
        collector.add_new_book("Король Лев")
        collector.set_book_genre("Король Лев", "Мультфильмы")

        expected_dictionary = {"Один Дома": "Комедии", "Король Лев": "Мультфильмы"}
        assert collector.get_books_genre() == expected_dictionary

    def test_get_books_for_children_no_age_rating_books_without_age_rating_return(self, collector):
        collector.add_new_book("Король Лев")
        collector.set_book_genre("Король Лев", "Мультфильмы")
        assert "Король Лев" in collector.get_books_for_children()

    def test_add_book_in_favorites_add_one_book_book_added_in_favorites(self, collector):
        collector.add_new_book("Один Дома")
        collector.add_book_in_favorites("Один Дома")
        assert "Один Дома" in collector.favorites

    def test_delete_book_from_favorites_remove_real_book_book_removed(self, collector):
        collector.add_new_book("Один Дома")
        collector.add_book_in_favorites("Один Дома")
        collector.delete_book_from_favorites("Один Дома")
        assert "Один Дома" not in collector.favorites

    def test_get_list_of_favorites_books_with_real_books_list_favorites_returns(self, collector):
        collector.add_new_book("Один Дома")
        collector.add_book_in_favorites("Один Дома")
        assert collector.get_list_of_favorites_books() == ["Один Дома"]
