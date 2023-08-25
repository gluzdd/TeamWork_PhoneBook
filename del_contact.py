def del_contact(phonebook, find):
    for contact in phonebook:
        for k, v in contact.items():
            if find in v:  # проверяем есть ли ключ "from" в ключах словаря
                print('Контакт удален!')
                phonebook.remove(contact)
                break
            else:
                print("Нет такого контакта!")
                break
    return phonebook
