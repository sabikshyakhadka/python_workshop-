user_choice = input ("""
1. circle
2. rectangle 
3. triangle 
""")
if user_choice =="1":
   user_input = float(input("enter the radius"))
   result_area = 3.14 * user_input ** 2
   print(f"area = {result_area}")
   
elif user_choice == "2":
    user_lenght = float(input("enter the lenght of rectangle"))
    user_breath = float(input("enter the breath of rectangle"))
    user_height = float(input("enter the height of rectangle"))
    result_area = user_lenght * user_breath * user_height
    print(f"area = {result_area}")

elif user_choice == "3":
  user_base = float(input("enter the base of the triangle"))
  user_height = float(input("enter the height of the triangle"))
  result_area = 1/2 * user_base * user_height
  print(f"area = {result_area}")

else :
  print("invalid input")
 