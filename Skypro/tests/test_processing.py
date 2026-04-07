import pytest
from src.processing import filter_by_state, sort_by_date

# Фикстура для тестовых данных (как просил куратор)
@pytest.fixture
def transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512317"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-16T07:33:05.745473"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
    ]

# Тест фильтрации (название начинается с test_)
def test_filter_by_state(transactions):
    result = filter_by_state(transactions, "EXECUTED")
    # Обязательно используем assert
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 2

# Тест фильтрации, когда такого статуса нет
def test_filter_by_state_empty(transactions):
    result = filter_by_state(transactions, "PENDING")
    assert result == []

# Тест сортировки по дате (по убыванию - по умолчанию)
def test_sort_by_date_desc(transactions):
    result = sort_by_date(transactions)
    assert result[0]["id"] == 1  # 2019 год новее 2018-го

# Тест сортировки по дате (по возрастанию)
def test_sort_by_date_asc(transactions):
    result = sort_by_date(transactions, descending=False)
    assert result[0]["id"] == 2  # 2018-06 самый ранний