def get_mask_card_number(card_number: str) -> str:
    """ "Маскирует номер карты, скрывая средние цифры."""
    card_number = str(card_number)
    block_1 = card_number[:4]
    block_2 = card_number[4:6] + "**"
    block_3 = "****"
    block_4 = card_number[12:]

    return block_1 + " " + block_2 + " " + block_3 + " " + block_4


def get_mask_account(account_number: str) -> str:
    """ "Маскирует номер банковского счёта, оставляя только последние 4 цифры."""
    account_number = str(account_number)
    block_1 = account_number[-4:]

    return "**" + block_1


result = get_mask_card_number(card_number="2689764563647584")
print(result)

result = get_mask_account(account_number="73654108430135874305")
print(result)
