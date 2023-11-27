format_conditions = lambda conditions: "[{}]".format(", ".join(
    [
        "{}: {}".format(key, f"({format_conditions(value)})" if isinstance(value, dict) else value)
        for key, value in conditions.items()
    ]
))
