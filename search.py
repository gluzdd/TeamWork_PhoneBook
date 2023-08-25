def search_contact(phonebook, find):
    for contact in phonebook:
        for v in contact.values():
            if find.lower() in v.lower():
                return (f'{contact["name"]}|{contact["lastname"]}|{contact["surname"]}|{contact["phone_number"]}')