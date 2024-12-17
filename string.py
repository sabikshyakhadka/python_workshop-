a = "what's your name?"
print(a)

for x in "banana":
  print(x)

a= "hello world!"
print(len(a))

txt = " the happy moments are good!"
print("good" in txt)

b = "hello, world!"
print(b[2:5])

print(b[:-5])
print(b[:-2])
Print(b.upper())
print(b.lower())
print(b.capitalize())

b = "hello    "
print(b.strip())


b = "hello world!"
print(b.replace("world", "rujna"))

z = b.split(" , ")
print(z)


print("hello world")
name= input("enter your name")
print()



first_number= float (input("enter your first number : "))
second_number= float (input("enter your second number : "))
#first_number= int(first_number)
user_choice = input("""
               please choose your option
                + for addition
                - for substraction
                """)
if user_choice=="+":
    print("addition=", first_number + second_number)
elif user_choice=="-":
    print("substraction=", first_number - second_number)
else:
    print("invalid=", first_number and second_number is invalid)
 
 
 def convert_currency(amount, from_currency, to_currency):
    # Hardcoded exchange rates
    rates = {
        'USD': 1,
        'EUR': 0.85,
        'JPY': 110
    }
    
    # Check if both currencies are supported
    if from_currency not in rates or to_currency not in rates:
        return "Unsupported currency"
    
    # Convert the amount to USD first
    amount_in_usd = amount / rates[from_currency]
    
    # Convert USD to the target currency
    converted_amount = amount_in_usd * rates[to_currency]
    
    return converted_amount

amount_usd_to_eur = convert_currency(15000, 'USD', 'EUR')
amount_eur_to_jpy = convert_currency(10000, 'EUR', 'JPY')

print(f" USD to EUR: {amount_usd_to_eur:.2f} EUR")
print(f"EUR to JPY: {amount_eur_to_jpy:.2f} JPY")
