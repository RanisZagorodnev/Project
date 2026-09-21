import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "RUB", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


@pytest.mark.parametrize(
    "currency, expected_count",
    [("USD", 2), ("usd", 2), ("RUB", 1), ("EUR", 0)],
)
def test_filter_by_currency(transactions, currency, expected_count):
    filtered_transactions = list(filter_by_currency(transactions, currency))

    assert len(filtered_transactions) == expected_count
    assert all(tx["operationAmount"]["currency"]["code"] == currency.upper() for tx in filtered_transactions)


@pytest.mark.parametrize(
    "transactions_data",
    [
        [],
        [{"operationAmount": {"currency": {"code": "RUB"}}, "description": "Оплата"}],
        [{"description": "Без валюты"}],
    ],
)
def test_filter_by_currency_handles_empty_or_non_matching_input(transactions_data):
    result = list(filter_by_currency(transactions_data, "USD"))
    assert result == []


def test_transaction_descriptions_returns_descriptions_for_each_transaction(transactions):
    descriptions = list(transaction_descriptions(transactions))

    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
    ]


@pytest.mark.parametrize(
    "transactions_data, expected",
    [
        ([], []),
        ([{"description": "Тест 1"}, {"description": "Тест 2"}], ["Тест 1", "Тест 2"]),
        ([{"id": 1}, {"description": None}, {"description": "Тест 3"}], ["Тест 3"]),
    ],
)
def test_transaction_descriptions_empty_and_varied_input(transactions_data, expected):
    assert list(transaction_descriptions(transactions_data)) == expected


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (5, 5, ["0000 0000 0000 0005"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator_formats_range(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected


def test_card_number_generator_keeps_four_group_format():
    numbers = list(card_number_generator(12, 14))
    assert numbers == [
        "0000 0000 0000 0012",
        "0000 0000 0000 0013",
        "0000 0000 0000 0014",
    ]
    assert all(len(number) == 19 for number in numbers)
    assert all(number.count(" ") == 3 for number in numbers)


def test_card_number_generator_rejects_inverted_range():
    with pytest.raises(ValueError, match="start must be less than or equal to stop"):
        list(card_number_generator(5, 1))
