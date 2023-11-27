format_currency = lambda value: (
    f"R$ {value:,.2f}".replace(",", ".")[::-1].replace(".", ",", 1)[::-1]
)
models_to_dict = lambda models: list(map(lambda model: model.to_dict(), models))
