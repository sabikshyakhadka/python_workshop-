def convert_currency(amount, from_currency, to_currency):
    rates = {
        'USD': 1,
        'EUR': 0.85,
        'JPY': 110
    }
    if from_currency not in rates or to_currency not in rates:
        return "Unsupported currency"
    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]
    return converted_amount
