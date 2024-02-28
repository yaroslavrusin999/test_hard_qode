from django.core.exceptions import ValidationError

def validate_positiv_price(value):
    if value < 0:
        raise ValidationError(
            "Цена товара должна быть положительная",
            params={"value": value},
        )