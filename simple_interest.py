user_choices = input ("""
1. simple intrest 
2. compound interst 
""")
if user_choices =="1":
    user_principal = float(input("enter principal"))
    user_rate = float(input("enter rate "))
    user_time = float(input("enter time"))
    result = (user_principal * user_rate * user_time) / 100
    print(f"simple interest = {result}")
elif user_choice_choice == "2":
    user_principal = float(input("enter principal"))
    user_rate = float(input("enter rate "))
    user_time = float(input("enter time"))
    result = user_principal * (1+(user_rate /100)) ** user_time
    print(f"compound interest = {result}")
else:
    print("invalid input")
