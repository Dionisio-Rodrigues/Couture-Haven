format_currency = lambda value: (
    f"R$ {value:,.2f}".replace(",", ".")[::-1].replace(".", ",", 1)[::-1]
)
