def print_full_name(**kwargs):
    print(kwargs)
    print(f"my full name is {kwargs['first_name']} {kwargs['last_name']}")
print_full_name(first_name ="sabikshya", last_name ="khadka", middle_name ="none")




alien_message = "nella na na I .uoy era woh namH iH"
print (f"""
 alien_message = {alien_message} 
 Now Human message = {alien_message[:: -1]} 
 """)
 


print ("hello world") 
x = 5
y = "hello world"
print (id(x))
print (id(y))
print (type(x))
print (type(y))
