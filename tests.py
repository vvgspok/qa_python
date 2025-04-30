import pytest
from main import BooksCollector
from data import book_names, genre_names, genre_age_rating


class TestBooksCollector:
    @pytest.mark.parametrize(
        'book_name, result',
        [
            (book_names[0], 1),
            (book_names[2], 0)
        ],
        ids = [
            'Adding a book with less than 40 symbol',
            'Adding a book containing more than 40 symbol'
        ]
    )
    def test_add_new_book_validates_name_length(self, book_name, result):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == result

    def test_add_new_book_add_duplicate_book_fails(self):
        collector = BooksCollector()
        collector.add_new_book(book_names[0])
        collector.add_new_book(book_names[0])
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'book_name, genre, result',
        [
            (book_names[0], genre_names[0], genre_names[0]),
            (book_names[1], genre_names[1], None),
            (book_names[0], genre_names[2], '')
        ],
        ids=[
            'Set genre for book from list "books_genre"',
            'Set genre for book not in list "books_genre"',
            'Set genre not from "genre" list'
        ]
    )
    def test_set_book_genre_validates_conditions(self, book_name, genre, result, collector_w_books):
        collector_w_books.set_book_genre(book_name, genre)
        assert collector_w_books.get_book_genre(book_name) == result

    def test_get_book_genre_returns_genre_correct(self, collector_w_books):
        collector_w_books.set_book_genre(book_names[0], genre_names[0])
        assert collector_w_books.get_book_genre(book_names[0]) == genre_names[0]

    def test_get_books_with_specific_genre_filters_correct(self, collector_w_books):
        collector_w_books.set_book_genre(book_names[0], genre_names[0])
        assert book_names[0] in collector_w_books.get_books_with_specific_genre(genre_names[0])

    def test_get_books_genre_returns_full_dict(self, collector_w_books):
        collector_w_books.set_book_genre(book_names[0], genre_names[0])
        expected_result = {book_names[0]: genre_names[0]}
        actual_result = collector_w_books.get_books_genre()
        assert actual_result == expected_result

    @pytest.mark.parametrize(
        'book_name, genre, result',
        [
            (book_names[0], genre_names[1], 1),
            (book_names[1], genre_names[0], 0)
        ],
        ids=[

            'Add a book for children',
            'Add a book not for children'
        ]
    )
    def test_get_books_for_children_filters_by_children_rating(self, book_name, genre, result):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        len_get_books_for_children = len(collector.get_books_for_children())
        assert len_get_books_for_children == result

    @pytest.mark.parametrize(
        'book_name, result',
        [
            (book_names[0], 1),
            (book_names[1], 0)
        ],
        ids=[
            'Adding books from the list "books_genre"',
            'Adding books not from the list "books_genre"'
        ]
    )
    def test_add_book_in_favorites_validates_book_existence(self, book_name, result, collector_w_books):
        collector_w_books.add_book_in_favorites(book_name)
        assert len(collector_w_books.get_list_of_favorites_books()) == result

    def test_add_book_in_favorites_add_duplicate_favorites_fails(self, collector_w_books):
        collector_w_books.add_new_book(book_names[0])
        assert len(collector_w_books.get_books_genre()) == 1

    def test_delete_book_from_favorites_deletes_existing_book_correct(self, collector_w_books):
        collector_w_books.add_book_in_favorites(book_names[0])
        list_favorites_before_delete = len(collector_w_books.get_list_of_favorites_books())
        collector_w_books.delete_book_from_favorites(book_names[0])
        list_favorites_after_delete = len(collector_w_books.get_list_of_favorites_books())
        assert list_favorites_before_delete != list_favorites_after_delete

    def test_delete_book_from_favorites_delete_non_existent_book_fails(self, collector_w_books):
        collector_w_books.add_book_in_favorites(book_names[0])
        list_favorites_before_delete = len(collector_w_books.get_list_of_favorites_books())
        collector_w_books.delete_book_from_favorites(book_names[1])
        list_favorites_after_delete = len(collector_w_books.get_list_of_favorites_books())
        assert list_favorites_before_delete == list_favorites_after_delete

    def test_get_list_of_favorites_books_returns_list_correct(self, collector_w_books):
        collector_w_books.add_book_in_favorites(book_names[0])
        assert collector_w_books.get_list_of_favorites_books() == [book_names[0]]





