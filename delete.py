def delete_contact(phonebook, find):
    for contact in phonebook:
        for v in contact.values():
            if find.lower() in v.lower():
                del contact