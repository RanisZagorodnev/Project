from masks import get_mask_card_number, get_mask_account


def mask_account_card(text: str) -> str:
    *names, number = text.split()
    if len(number) == 20:
        return f"Счет {get_mask_account(number)}"

    return " ".join(names) + " " + get_mask_card_number(number)


def get_date(date: str) -> str:
    year, month, day = date[:10].split("-")
    return f"{day}.{month}.{year}"


print(get_date("2026-03-11T02:26:18.671407"))

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
