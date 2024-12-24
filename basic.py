def convert_currency(amount, from_currency, to_currency):
user_choice = ("""
1. Temperature
2. currencies
""")

if user_choice == "1" :
    user_input = float(input("enter the celcius"))
    result_Temperature =  (user_input *9/5) + 32
    print(f"ferigheit = {result_Temperature}")

elif user_choice == "2" :
    rates = {
        'USD': 1,
        'EUR': 0.85,
        'JPY': 110
    }
if from_currency not in rates or to_currency not in rates:
    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]

         