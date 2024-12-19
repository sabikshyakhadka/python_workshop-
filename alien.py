def print_full_name(**kwargs):
    print(kwargs)
    print(f"my full name is {kwargs['first_name']} {kwargs['last_name']}")
print_full_name(first_name ="sabikshya", last_name ="khadka", middle_name ="none")
