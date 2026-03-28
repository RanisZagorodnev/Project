from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(text: str) -> str:
    if not text:
        return ""

    parts = text.split()
    if len(parts) < 2:
        return text

    *names, number = parts

    if len(number) == 20:
        return f"Счет {get_mask_account(number)}"

    return " ".join(names) + " " + get_mask_card_number(number)


def get_date(date: str) -> str:
    if not date:
        return ""

    year, month, day = date[:10].split("-")
    return f"{day}.{month}.{year}"

