from __future__ import annotations

from typing import Iterator, Iterable, Dict, Any


def filter_by_currency(transactions: Iterable[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Yield transactions whose operation currency matches the provided code."""
    normalized_currency = currency.upper()
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency_info = operation_amount.get("currency", {})
        if currency_info.get("code") == normalized_currency:
            yield transaction


def transaction_descriptions(transactions: Iterable[Dict[str, Any]]) -> Iterator[str]:
    """Yield descriptions for each transaction in the provided sequence."""
    for transaction in transactions:
        description = transaction.get("description")
        if description is not None:
            yield description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Generate bank card numbers from start to stop inclusive in 16-digit format."""
    if start > stop:
        raise ValueError("start must be less than or equal to stop")

    for number in range(start, stop + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16]
