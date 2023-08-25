
def add_contact(phonebook, name, lastname, surname, phone_number):
    contacts = {
        "name": name,
        "lastname": lastname,
        "surname": surname,
        "phone_number": phone_number
        }
    phonebook.append(contacts)
    
    
    
    
    
    
    
    
    
    # # with open("data2.txt", "a") as file:
    #     for contact in phonebook:
    #         # file.write(f'{contact["name"]}|{contact["lastname"]}|{contact["surname"]}|{contact["phone_number"]}\n')
    #         file.write(f'{contact["name"]}|{contact["lastname"]}|{contact["surname"]}|{contact["phone_number"]}\n')
