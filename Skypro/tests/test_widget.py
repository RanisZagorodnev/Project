import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card_account_only():
    text = "Счет 55555555555555555555"
    result = mask_account_card(text)
    assert result == "Счет **5555"

@pytest.mark.parametrize("text, expected", [
    ("Visa Gold 7000792289606361", "Visa Gold 7000 79** **** 6361"),
    ("Maestro 1501813273878658", "Maestro 1501 81** **** 8658"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("", ""),
    ("НеизвестныйТип 123", "НеизвестныйТип 123") # проверка устойчивости
])
def test_mask_account_card(text, expected):
    assert mask_account_card(text) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-31T23:59:59", "31.12.2023"),
    ("", "") # проверка обработки отсутствующей даты
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected