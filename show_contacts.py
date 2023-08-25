def show_contact(phonebook):
    if not phonebook:
        print("Пустой справочник")
        return
    for contact in phonebook:
        print(f'{contact["name"]}|{contact["lastname"]}|{contact["surname"]}|{contact["phone_number"]}')