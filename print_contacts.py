def show_contact(phonebook):
    if not phonebook:
        print("Пустой справочник")
        return
    for contact in phonebook:
        print("*" * 26)
        print(f'Имя: {contact["name"]} \nФамилия: {contact["lastname"]} \nОтчество: {contact["surname"]} \n'
              f'Номер телефона: {contact["phone_number"]}')
        print("*" * 26)
