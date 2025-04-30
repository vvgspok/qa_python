## Описание
Данный файл содержит тесты для класса BooksCollector

## Тесты

### test_add_new_book_validates_name_length
Тест проверяет добавление новой книги в коллекцию .В зависимости от длины названия книги

### test_add_new_book_add_duplicate_book_fails
Тест проверяет, что книга с тем же названием не может быть добавлена повторно

### test_set_book_genre_validates_conditions
Тест проверяет, что жанр устанавливается правильно в разных ситуациях

### test_get_book_genre_returns_genre_correct
Тест проверяет, что можно получить жанр книги после его установки

### test_get_books_with_specific_genre_filters_correct
Тест проверяет, что можно получить список книг с определённым жанром

### test_get_books_genre_returns_full_dict
Тест проверяет, что можно получить текущий словарь books_genre

### test_get_books_for_children_filters_by_children_rating
Тест проверяет, что можно получить книги, которые подходят детям

### test_add_book_in_favorites_validates_book_existence
Тест проверяет добавление книги в избранное, если книга существует в словаре books_genre

### test_add_book_in_favorites_add_duplicate_favorites_fails
Тест проверяет, что книга с тем же названием не может быть добавлена в избранное повторно

### test_delete_book_from_favorites_deletes_existing_book_correct
Тест проверяет удаление книги из списка избранного

### test_delete_book_from_favorites_delete_non_existent_book_fails
Тест проверяет удаление книги не из списка избранного

### test_get_list_of_favorites_books_returns_list_correct
Тест проверяет получение списка избранных книг 