import pytest

from main import BooksCollector
from data import book_names


@pytest.fixture
def collector_w_books():
    collector = BooksCollector()
    collector.add_new_book(book_names[0])
    return collector