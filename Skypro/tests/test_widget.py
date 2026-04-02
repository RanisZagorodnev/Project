import pytest
from src.widget import  mask_account_card


def test_mask_account_card_account_only():
    text = "Счет 55555555555555555555"
    result = mask_account_card(text)
    assert result == "Счет **5555"