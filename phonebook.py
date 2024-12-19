
def contact_list(name, number, contacts={}):    
        contacts[name.lower()] = number
        return contacts 

def store_contacts():
    contacts = {}
    while True:
        name = input("enter  name")
        number = input ("enter number") 
        contacts = contact_list(name, number, contacts)
        user_choice = input ("""
        do you want to exit
        1. yes
        2. No
        """)  
        if user_choice == "1":
            return (contacts)
            
my_contact_list = store_contacts()

def get_phone_number(name, contacts):
    return contacts.get(name.lower())
user_name = input("enter name to find phone number")
print (get_phone_number (user_name, my_contact_list))

    