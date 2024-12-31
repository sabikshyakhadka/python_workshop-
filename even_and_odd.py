user_choice = input("""
1. even or odd
2. prime number
""")

user_number = float(input("Enter a number: "))

if user_choice == "1":
    if user_number % 2 == 0:
        print(f"{user_number} is even")
    else:
        print(f"{user_number} is odd")
elif user_choice == "2":
    is_prime = True
    if user_number <= 1:
        is_prime = False
    else:
        for i in range(2, int(user_number)):
            if user_number % i == 0:
                is_prime = False
                break
    if is_prime:
        print(f"{user_number} is a prime number")
    else:
        print(f"{user_number} is not a prime number")
else:
    print("Invalid input")
