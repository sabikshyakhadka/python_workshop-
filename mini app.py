#simple interest or compound interest 
user_choices == ("""
          1. simple interst 
          2. compount interst 
          """)
if user_choices == "1"
         user_principle = float(input("enter principle"))
         user_time= float(input("enter time"))
         user_rate = float(input("enter rate"))
         result = (user_principle * user_rate * user_time)/100
         print (f"simple intrest = {result}")
elif user_choices =="2"
         user_principle = float(input("enter principle"))
         user_time= float(input("enter time"))
         user_rate = float(input("enter rate"))