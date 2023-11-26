format_currency = lambda value: (
    f"R$ {value:,.2f}".replace(",", ".")[::-1].replace(".", ",", 1)[::-1]
)
models_to_dict = lambda models: [model.to_dict() for model in models]
