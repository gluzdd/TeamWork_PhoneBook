from add_contact import add_contact
from show_contacts import show_contact
from search import search_contact
from delete import delete_contact
print("=====Меню=====\nВыберите действие: "
      "\n1-Показать все контакты"
      "\n2-Добавить контакт"
      "\n3-Поиск контакта"
      "\n4-Внести изменения"
      "\n5-Удалить контакт"
      "\n0-Закрыть телефонный справочник")

phonebook = []
choice = None

while choice != "0":
    choice = input("Выберите команду: 1/2/3/4/5/0: ")
    if choice == "0":
        with open("data2.txt", "a") as file:
            for contact in phonebook:
                file.write(f'{contact["name"]}|{contact["lastname"]}|{contact["surname"]}|{contact["phone_number"]}\n')
            
    elif choice == "1":
        show_contact(phonebook)

    elif choice == "2":
        name = input("name: ")
        lastname = input("lastname: ")
        surname = input("surname: ")
        phone_number = input("phone_number: ")
        add_contact(phonebook, name, lastname, surname, phone_number)
        
    elif choice == "3":
        search = input("find: ")
        print(search_contact(phonebook, search))

    elif choice == "4":
        pass

    elif choice == "5":
        search = input("delete: ")
        delete_contact(phonebook, search)

    else:
        print("Неверный выбор. Выберите пункт из списка: ")
