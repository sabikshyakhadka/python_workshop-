user_choice = input("""
1. km to miles
2. miles ti km 
3. centimeter to inch
4. inch to centiemeter
""")
if user_choice == "1" :
 user_input = float(input("enter km "))
 result = user_input *0.621371
 print(f"{user_input} km = {result} miles")
elif user_choice == "2" :
     user_input = float(input("enter miles")) 
     result = user_input * 1.60934
     print(f"{user_input} miles = {result} km")
elif user_choice =="3" :
    user_input = float(input("enter centimeter"))
    result = user_input * 0.393701
    print(f"{user_input} centimeter = {result} inch")
elif user_choice == "4" :
    user_input = float(input("enter inch"))
    result = user_input * 2.54
    print(f"{user_input} inch = {result} centimeter")
else:
    print("invalid input")
    