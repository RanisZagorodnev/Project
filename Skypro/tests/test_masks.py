import pytest
from src.masks import get_mask_card_number, get_mask_account



def test_get_mask_card_number():
    card = "12345678"
    result = get_mask_card_number(card)
    assert result == "1234 56** **** "

def test_mask_card_standard():
    card = "1234567812345678"
    result = get_mask_card_number(card)
    assert result == "1234 56** **** 5678"

def test_mask_card_short():
    card = "12345678"
    result = get_mask_card_number(card)

    assert result.startswith("1234")
    assert result.endswith("")

def test_mask_card_long():
    card = "12345678901234567890"
    result = get_mask_card_number(card)

    assert result.startswith("1234")
    assert result.endswith("7890")

def test_mask_card_number_as_int():
    card = 1234567812345678
    result = get_mask_card_number(card)

    assert result == "1234 56** **** 5678"

def test_mask_card_very_short():
    card = "12"
    result = get_mask_card_number(card)

    assert result.startswith("12")

def test_mask_account_standard():
    account = "12345678901234567890"
    result = get_mask_account(account)

    assert result == "**7890"

def test_mask_account_short():
    account = "123"
    result = get_mask_account(account)

    assert result == "**123"

def test_mask_account_exact_4():
    account = "5678"
    result = get_mask_account(account)

    assert result == "**5678"

def test_mask_account_long():
    account = "1234567890123456789012345"
    result = get_mask_account(account)

    assert result == "**2345"

def test_mask_account_int():
    account = 1234567890
    result = get_mask_account(account)

    assert result == "**7890"

def test_mask_account_empty():
    account = ""
    result = get_mask_account(account)

    assert result == "**"